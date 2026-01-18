import asyncio
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from app.core.aws_config import AWS_CONFIG

async def test_bedrock():
    print("Testing Bedrock Connection...")
    print(f"AWS Config: {AWS_CONFIG}")
    
    try:
        llm = ChatBedrock(
            model_id="apac.amazon.nova-pro-v1:0", 
            model_kwargs={"temperature": 0}, 
            config=AWS_CONFIG
        )
        print("Initialized LLM. Invoking...")
        
        messages = [HumanMessage(content="Hello, say test.")]
        res = await llm.ainvoke(messages)
        print(f"Response: {res.content}")
        print("SUCCESS")
    except Exception as e:
        print(f"FAILURE: {e}")

if __name__ == "__main__":
    asyncio.run(test_bedrock())
