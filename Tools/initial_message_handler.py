"""
This is the first place where user message will arrive.
identify intent

"""
from OpenAILM.gpt import GPTLLm
from OpenAILM.handle_functions import chat_completion_with_function_execution
from Tools.functions.function_definitions import functions

def init_message_handle(user_message,  app, conversation:GPTLLm, chat_history=[]):
    # if role!="system":
    conversation.add_message("user",user_message)
    # The model first prompts the user for the information it needs to use the weather function

    chat_response = chat_completion_with_function_execution(conversation=conversation,
        messages=conversation.conversation_history, functions=functions
    )
    app.logger.info('%s logged in ', chat_response)
    try:
        assistant_message = chat_response["choices"][0]["message"]["content"]
        conversation.add_message('assistant',str(assistant_message))
        print(f"\n\n initial_message_handler 19 chat_response --->: {chat_response=}\n")
        if "choices" in chat_response and len(chat_response["choices"]) > 0 and "message" in chat_response["choices"][0] and "content1" in chat_response["choices"][0]["message"]:
            return chat_response

    except Exception as e:
        print(e)    
        print(chat_response)
        app.logger.info('%s logged in ', e)
        assistant_message="Please rephrase your question"
    
    return assistant_message
