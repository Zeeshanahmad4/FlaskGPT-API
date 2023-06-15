
import datetime
import openai
import json
import json
import lib
import sys
import traceback
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone


openai.api_key = "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"

COMPLETIONS_MODEL = "text-davinci-003"
MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"

class OpenAIJSONEncoder(json.JSONEncoder):
          def default(self, obj):
             if isinstance(obj, openai.openai_object.OpenAIObject):
                 return obj.as_dict()
             return json.JSONEncoder.default(self, obj)




def ask_english(
    query: str,
    prompt:str,
    userid:str,
    chatid:int,
    deviceid:str,
    date:datetime
) -> str:
    """Answers a query using GPT and a dataframe of relevant texts and embeddings."""
    model: str = GPT_MODEL
    token_budget: int = 4096 - 500
    print_message: bool = False
   
    lib.log_message(userid, chatid,'user', query,deviceid,date)
    data=lib.get_user_data(userid,chatid)
    messages = [
        {"role": "system",
         "content":prompt},
        {"role": "user", 
         "content": str(data)},
       
    ]
    response_message= process_request(query,messages,userid,chatid,deviceid,date)
   
    
    
    return response_message


def process_request(value,message,user_id,chat_id,deviceid,date):
    
    
    model: str = GPT_MODEL
    
    try:
        
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=0.8,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=1.0,
        presence_penalty=1.0
        )
        response_message = response.choices[0].message["content"]
       
        lib.log_message(user_id, chat_id, "Assistant", response_message,deviceid,date)
        
        return response_message
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        stack = ''.join('!! ' + line for line in lines)
        
        print("handled exception\n", stack)
    
def ask_query(value):

    pinecone.init(
    api_key="0a973c09-7c6a-4481-b220-676633c15aef",  # find at app.pinecone.io
    environment="us-west1-gcp"  # next to api key in console
    )
    index_name = "embedding"
    index = pinecone.Index(index_name)
    docsearch = pinecone.Index(index_name=index_name)
    xq = openai.Embedding.create(input=value, engine=MODEL)['data'][0]['embedding']
    res = index.query([xq], top_k=5, include_metadata=True)
    matches_arr = []
    for match in res['matches']:
       match_dict = {'text': match['metadata']['text']}
       matches_arr.append(match_dict)
    return matches_arr
