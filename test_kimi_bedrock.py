import boto3
import json
import sys

def test_kimi_bedrock():
    # You can change to your specific region where Kimi is available
    region_name = 'us-west-2' # update as necessary, e.g., us-east-1, us-west-2
    
    try:
        # Create Bedrock Runtime client
        # Requires valid AWS credentials configured (e.g., via 'aws configure' or environment variables)
        client = boto3.client('bedrock-runtime', region_name=region_name)
        
        # Kimi K2 model ID. 
        # Alternatives: 'moonshot.kimi-k2-thinking'
        model_id = 'moonshotai.kimi-k2.5' 
        
        questions = [
            "What is the capital of France?",
            "How many planets are in the solar system?",
            "What is the boiling point of water in Celsius?",
            "Who wrote Hamlet?",
            "What is the largest ocean on Earth?"
        ]
        
        print(f"Attempting to invoke model: {model_id} in region: {region_name} for {len(questions)} requests...\n")
        
        for i, question in enumerate(questions, 1):
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": question
                        }
                    ]
                }
            ]
            
            print(f"--- Request {i} ---")
            print(f"Question: {question}")
            
            response = client.converse(
                modelId=model_id,
                messages=messages,
                inferenceConfig={
                    "maxTokens": 512,
                    "temperature": 0.7
                }
            )
            
            # Parse and print response
            output_text = response['output']['message']['content'][0]['text']
            print(f"Response:\n{output_text}\n")
        
    except boto3.exceptions.Boto3Error as e:
        print("\n--- Boto3 Error ---")
        print(str(e))
    except Exception as e:
        print("\n--- Error invoking Kimi on Bedrock ---")
        print(str(e))
        print("\nPlease verify:")
        print("1. Your AWS credentials are valid and active.")
        print("2. You have explicitly requested and been granted access to Moonshot Kimi models in the AWS Bedrock console for this region.")
        print(f"3. Kimi is supported in the '{region_name}' region.")

if __name__ == "__main__":
    test_kimi_bedrock()
