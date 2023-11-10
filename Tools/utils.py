def parse_output(response):
    if(isinstance(response, dict)):
        if('answer' in response):
            response = response['answer']
        elif response['role']=='assistant':
            response = response['content']
    return response

def formatLHCResponse(message, data=None):
    print(f"\n\n data --->: {data=}\n")
    
    # simple text response
    if data and len(data):
        i =0
        x =[
            {
                "_id":"i_hope_you_find_joy",
                "type":"text",
                "content":{"text":"These are few properties found according to your requirements: "}
            },
            {
                "_id": "1TGygGOgG",
                "type": "generic",
                "content": {
                    "text": "text 23 utils",
                    "list": []
                }
            },
            {
                "_id": "JGt7t28Fs",
                "type": "buttons",
                "content": {
                    "text": "mother texttt",
                    "buttons": [
                        {
                            "_id": "SAJGpXrVp",
                            "type": "url",
                            "content": {
                                "name": "VIEW ALL",
                                "payload": "graana.com"
                            }
                        }
                    ]
                }
            }
        ]
        for card in data:
            print(f"\n\n card --->: {card['image']=}\n")
            
            i+=1
            j = {
                "_id": "zwvE6hbxs"+str(i),
                "type": "button",
                "content": {
                    "img": card['image'],
                    "title": card['customTitle'],
                    "subtitle": card['price'],
                    "payload": "",
                    "subbuttons": []
                }
            }
            x[1]['content']['list'].append(j)
        import json

        x= json.dumps(x)
        return {"trigger_body":x}
    
    return {"trigger_body": "[\n    {\n        \"_id\": \"QC_snqpzy\",\n        \"type\": \"text\",\n        \"content\": {\n        \"text\": \""+message+"\"\n        }\n    }\n   ]"}




#     return {"trigger_body": "[\n    {\n        \"_id\": \"QC_snqpzy\",\n        \"type\": \"text\",\n        \"content\": {\n        \"text\": \""+message+"\"\n        }\n    }\n   ]"}
# x =[{
#     "_id":"againnn??",
#     "type":"text", 
#     "content":{"text":"ghodaaa"}

# },
# {
#     "_id": "1TGygGOgG",
#     "type": "generic",
#     "content": {
#         "text": "dabanggai",
#         "list": [
#             {
#                 "_id": "zwvE6hbxs",
#                 "type": "button",
#                 "content": {
#                     "img": "https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&w=1000&q=80",
#                     "title": "zinger",
#                     "subtitle": "burger",
#                     "payload": "",
#                     "subbuttons": []
#                 },
#                 "buttons": [
#                     {
#                         "_id": "2EYkPBcbq",
#                         "type": "url",
#                         "content": {
#                             "name": "New button zzz",
#                             "payload": "google.com"
#                         }
#                     }
#                 ]
#             },
#             {
#                 "_id": "PfdyGBRzX",
#                 "type": "none",
#                 "content": {
#                     "img": "https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&w=1000&q=80",
#                     "title": "x second ",
#                     "subtitle": "again why thi",
#                     "payload": "",
#                     "subbuttons": []
#                 }
#             },
#             {
#                 "_id": "6oW3B5Mj0",
#                 "type": "updatechat",
#                 "content": {
#                     "img": "https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&w=1000&q=80",
#                     "title": "3 title zinger",
#                     "subtitle": "bugerer",
#                     "payload": "",
#                     "subbuttons": []
#                 }
#             }
#         ]
#     }
# },
# {
#     "_id": "zrgdyX17M",
#     "type": "list",
#     "content": {
#         "text": "",
#         "buttons_options": {
#             "message": "hi",
#             "btn_title": "welcome"
#         },
#         "buttons": [
#             {
#                 "_id": "kywUn6Df0",
#                 "type": "url",
#                 "content": {
#                     "name": "url",
#                     "payload": "http://google.com"
#                 }
#             },
#             {
#                 "_id": "rmn-xksJo",
#                 "type": "trigger",
#                 "content": {
#                     "name": "executre triggers please",
#                     "payload": "11"
#                 }
#             }
#         ],
#         "list_options": {
#             "no_highlight": False
#         },
#         "list": [
#             {
#                 "_id": "In4eYUfa6",
#                 "type": "none",
#                 "content": {
#                     "img": "https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&w=1000&q=80",
#                     "title": "hi there",
#                     "subtitle": "\\\\subttile",
#                     "payload": "",
#                     "subbuttons": []
#                 },
#                 "buttons": [
#                     {
#                         "_id": "r6MIs1Bud",
#                         "type": "updatechat",
#                         "content": {
#                             "name": "New button",
#                             "payload": ""
#                         }
#                     }
#                 ]
#             }
#         ],
#         "quick_replies": [
#             {
#                 "_id": "6QpDpSa20",
#                 "type": "button",
#                 "content": {
#                     "name": "this button",
#                     "payload": ""
#                 }
#             },
#             {
#                 "_id": "NAD_siW1p",
#                 "type": "updatechat",
#                 "content": {
#                     "name": "button 2",
#                     "payload": ""
#                 }
#             }
#         ]
#     }
# }
# ]

# import json

# x= json.dumps(x)
# return {"trigger_body":x}