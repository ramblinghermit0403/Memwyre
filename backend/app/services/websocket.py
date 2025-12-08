from typing import List, Dict
from fastapi import WebSocket
from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        # Store connections as {user_id: [WebSocket]}
        self.active_connections: Dict[str, List[WebSocket]] = defaultdict(list)

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[str(user_id)].append(websocket)

    def disconnect(self, websocket: WebSocket, user_id: str):
        user_id = str(user_id)
        if user_id in self.active_connections:
            if websocket in self.active_connections[user_id]:
                self.active_connections[user_id].remove(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

    async def send_personal_message(self, message: dict, user_id: str):
        user_id = str(user_id)
        if user_id in self.active_connections:
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_json(message)
                except:
                    pass

    async def broadcast(self, message: dict):
        # Broadcast to EVERYONE
        for user_sockets in self.active_connections.values():
            for connection in user_sockets:
                try:
                    await connection.send_json(message)
                except:
                    pass
                
manager = ConnectionManager()
