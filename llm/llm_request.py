import requests
import os.path
from dotenv import load_dotenv
load_dotenv()
DEEPSEEK_R1_API_KEY = str(os.getenv("DEEPSEEK_R1_API_KEY",'dummy_api_key'))
api_key = DEEPSEEK_R1_API_KEY

def get_chat_response(api_key, prompt, model="deepseek/deepseek-r1-zero:free"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}

if __name__ == "__main__":
    #Example usage:
    response = get_chat_response(api_key=api_key, prompt="tell me a joke?")
    print(response)