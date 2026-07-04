import boto3
import sys

def chat_kimi_bedrock():
    # You can change to your specific region where Kimi is available
    region_name = 'us-west-2' # update as necessary
    
    try:
        client = boto3.client('bedrock-runtime', region_name=region_name)
        model_id = 'moonshotai.kimi-k2.5' 
        
        print(f"Connecting to {model_id} in region: {region_name}...")
        print("Type 'quit' or 'exit' to stop.")
        print("-" * 50)
        
        # We will keep track of the conversation history
        messages = []
        
        while True:
            try:
                user_input = input("\nYou: ")
            except EOFError:
                break
                
            if user_input.strip().lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
                
            if not user_input.strip():
                continue
                
            # Add user message to history
            messages.append({
                "role": "user",
                "content": [{"text": user_input}]
            })
            
            try:
                response = client.converse(
                    modelId=model_id,
                    messages=messages,
                    inferenceConfig={
                        "maxTokens": 1024,
                        "temperature": 0.7
                    }
                )
                
                output_text = response['output']['message']['content'][0]['text']
                
                # Add Kimi's response to history
                messages.append({
                    "role": "assistant",
                    "content": [{"text": output_text}]
                })
                
                print(f"Kimi: {output_text}")
                
            except Exception as e:
                print(f"\n--- Error during API call ---")
                print(str(e))
                # Remove the failed user message from history so we can try again
                messages.pop()
                
    except boto3.exceptions.Boto3Error as e:
        print("\n--- Boto3 Error ---")
        print(str(e))
    except Exception as e:
        print("\n--- Error setting up client ---")
        print(str(e))

if __name__ == "__main__":
    chat_kimi_bedrock()
