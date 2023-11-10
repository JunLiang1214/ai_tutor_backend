import os 
import requests

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['model_name'] = "gpt-3.5-turbo-0613"

class GPTLLm:
    def __init__(self) -> None:
        self.conversation_history = []
        # self.model_name = "gpt-4-0613"
        self.model_name = "gpt-4"
        # self.model_name = "gpt-3.5-turbo-0613"

        # self.llm = OpenAI(
        #         max_tokens=300,
        #         model_name=self.model_name,
        #         temperature=0.1
        #     )
        pass


    def add_message(self, role, content):
        content=str(content)
        message = {"role": role, "content": content}
        self.conversation_history.append(message)

    def chat_completion_request(self, messages, functions=None):
        """
        call chat_completion endpoint with messages [], functions
        """
        model = self.model_name
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + OPENAI_API_KEY,
        }
        json_data = {"model": model, "messages": messages}
        
        if functions is not None:
            json_data.update({"functions": functions})
        try:
            
            response = requests.post("https://api.openai.com/v1/chat/completions",headers=headers,json=json_data,)
            print('--------------------------------------');
            print('response.json()=',response.json());
            print('--------------------------------------');
            
            return response.json()['choices'][0]['message']
        except Exception as e:
            print("Unable to 136")
            print(f"Exception: {e}")
            return e
    
    def display_conversation(self):
        for message in self.conversation_history:
            print(f"{message['role']}: {message['content']}\n\n")