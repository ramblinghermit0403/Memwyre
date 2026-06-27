export const projects = [
  {
    id: 'agent-bridge',
    title: 'AgentBridge',
    description: 'Fullstack framework for Remote MCP servers. Build and deploy enterprise-grade agents with real-time SSE streaming.',
    icon: '/agentbridge.ico',
    tags: ['MCP', 'AI Agents', 'Developer Tool', 'FastAPI'],
    github: 'https://github.com/ramblinghermit0403/agent_bridge',
    tech: ['Python', 'FastAPI', 'Vue.js', 'Tailwind', 'PostgreSQL'],
    images: [
      '/projects/agentbridge/agentbridge-1.png',
      '/projects/agentbridge/agentbridge-2.png',
      '/projects/agentbridge/agentbridge-3.png',
      '/projects/agentbridge/agentbridge-4.png'
    ],
    longDescription: `
Agent Bridge is a powerful AI agent platform that connects LangChain agents with MCP (Model Context Protocol) servers, enabling intelligent automation and tool execution through a modern web interface.

### Features
- **AI Agent Integration**: Built on FastAPI with LangChain for intelligent agent orchestration.
- **MCP Server Support**: Connect and manage multiple MCP servers for extended functionality.
- **Real-time Updates**: WebSocket support for live agent interactions.
- **Modern UI**: Beautiful Vue.js frontend with Tailwind CSS and Element Plus.
- **Secure Auth**: JWT-based authentication with fine-grained tool permissions.
    `
  },
  {
    id: 'memwyre',
    title: 'Memwyre',
    description: 'Universal memory layer for AI interactions. Captures, organizes, and retrieves knowledge across tools and models.',
    icon: '/favicon-192.png',
    tags: ['AI Memory', 'Chrome Extension', 'MCP Server', 'Knowledge Base'],
    github: 'https://github.com/ramblinghermit0403/Memwyre',
    demo: 'https://memwyre.tech',
    tech: ['FastAPI', 'ChromaDB', 'Vue 3', 'LangChain', 'MCP'],
    images: [
      '/projects/memwyre/memwyre-1.png',
      '/projects/memwyre/memwyre-2.png',
      '/projects/memwyre/memwyre-3.png',
      '/projects/memwyre/memwyre-4.png',
      '/projects/memwyre/memwyre-5.png'
    ],
    longDescription: `
Memwyre is a universal memory layer for AI—designed to capture, organize, and retrieve your knowledge across tools, conversations, and large language models.

Instead of losing context every time you switch between ChatGPT, Gemini, Claude, editors, or agents, Memwyre becomes the persistent brain that follows you everywhere.

### Key Features
- **Unified Memory Vault**: Store chat outputs, documents, web research, and notes in one place.
- **Smart Memory**: Semantic chunking, auto-generated embeddings, and context-aware retrieval.
- **Contextual Retrieval Engine**: Grounded answers using vector search and top-K relevance ranking.
- **LLM-Agnostic**: Works across ChatGPT, Gemini, Claude, and local models via MCP and browser extensions.
- **Intelligent Inbox**: Review and approve memories before they are committed to long-term storage.
    `
  },
  {
    id: 'broadsapp',
    title: 'Broadsapp',
    description: 'A full-featured WhatsApp outreach platform built on the WhatsApp Business API. Handles bulk messaging and campaigns.',
    icon: '/broadsapp-icon.png',
    tags: ['WhatsApp API', 'Automation', 'SaaS', 'Node.js'],
    tech: ['Node.js', 'WhatsApp Business API', 'PostgreSQL', 'Redis'],
    images: [
      '/projects/broadsapp/broadsapp-1.png',
      '/projects/broadsapp/broadsapp-2.png',
      '/projects/broadsapp/broadsapp-3.png',
      '/projects/broadsapp/broadsapp-4.png',
      '/projects/broadsapp/broadsapp-5.png'
    ],
    longDescription: `
Broadsapp is a comprehensive WhatsApp outreach platform designed for businesses to manage large-scale communication campaigns.

### Capabilities
- **Bulk Messaging**: Send thousands of messages securely via the official API.
- **Campaign Management**: Schedule and track performance of various outreach efforts.
- **Delivery Tracking**: Real-time analytics on message delivery, read rates, and engagement.
- **Automation**: Build automated workflows to handle customer responses and follow-ups.
    `
  }
];
