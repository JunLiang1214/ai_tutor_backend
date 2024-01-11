import os 
import requests
from Tools import gpt_model_config

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


class GPTLLm:
    def __init__(self) -> None:
        self.conversation_history = []
        self.gpt_model_name = gpt_model_config.get_model_config(gpt_model_config.ModelConfigKeysEnum.CURRENT_MODEL)
        pass

    def add_message(self, role, content):
        content=str(content)
        message = {"role": role, "content": content}
        self.conversation_history.append(message)

    def chat_completion_request(self, messages, functions=None):
        """
        call chat_completion endpoint with messages [], functions
        """
        model = self.gpt_model_name
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + OPENAI_API_KEY,
        }
        json_data = {"model": model, "messages": messages}
        
        if functions is not None:
            json_data.update({"functions": functions})
        try:
            
            response = requests.post("https://api.openai.com/v1/chat/completions",headers=headers,json=json_data,)
            # print('--------------------------------------');
            # print('response.json()=',response.json());
            # print('--------------------------------------');
            
            return response.json()['choices'][0]['message']
        except Exception as e:
            print("Unable to 136")
            print(f"Exception: {e}")
            return e
    
    def display_conversation(self):
        for message in self.conversation_history:
            print(f"{message['role']}: {message['content']}\n\n")