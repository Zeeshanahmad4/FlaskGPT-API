from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import model
import lib
import asyncio
# from celery import Celery
from celery import Celery

import datetime
app = Flask(__name__)
app.config.from_object('celeryconfig')
celery = Celery(app.name, broker=app.config['BROKER_URL'])
celery.conf.update(app.config)
api=Api(app)

class Hello(Resource):
    # @app.route('/<string:emailuser>/<string:passworduser>/<string:query>/<string:userid>/<int:chatid>/<int:account>/<string:deviceid>', methods=['POST'])
    @celery.task
    @app.route('/<string:emailuser>/<string:passworduser>/<string:query>/<string:userid>/<int:chatid>/<int:account>/<string:deviceid>', defaults={'value': 'required'}, methods=['POST'])
    def get(emailuser,passworduser,query,value,userid,chatid,account,deviceid):
      checkuser=lib.checkuserauthenticate(emailuser,passworduser)
      if(checkuser==1):
       date = datetime.date.today()
       if(account==0):
          data=lib.get_user_data_free_paid(userid,deviceid,date)
          print(data,"checking date")
          if(data<=20):  
                  if(value=="required"):
                    value='''You are an advance  Chatbot! As a sophisticated AI developed with advanced embedding technology You will use the data provided at the last paragraphs, you are expected to offer precise, detailed, and timely responses to user inquiries. Moreover, you have a responsibility to guide the conversation and ask follow-up questions to better understand user needs and provide tailored solutions. Here are some key points for your operation,Don't add (According to the text) this type of context in response:

          Guiding the Conversation: As an intelligent system, you have the ability to guide the chat and steer the conversation in a helpful direction using the provided data below stay in the contaxt. If the user provides a vague or unclear request, politely ask for more information to better assist them. For instance, 'Can you please provide more details?'
          
          Handle Specific Queries according to the data provided and give informative rich answers.
          
          Providing Prompt Responses: Speed and accuracy are key. However, the complexity of the query might affect your response time. Ensure you're optimized to manage this balance.
          Asking Follow-Up Questions: One of your key roles is to probe for more information when required. If the user's question is broad or could have multiple interpretations, ask follow-up questions to clarify their intention. For example, 'Would you like to know about the history of AI or its current applications?'
          Maintaining Context: You can understand the context of conversations while staying in the limit of the data provide . So, if a user asks for further clarification or has additional queries, you should provide suitable responses based on the ongoing context.
          .'''   
                    last_element =  model.ask_english(query,value,userid,chatid,deviceid,date)
                    return jsonify({          
                  
                  '2 Question':query,
                  '1 Answer':last_element
            
               })
                   
                            
            
              
          else:
              return jsonify({          
               'FreeMode' : 'You were in FreeMode you Free 10 Limit of Question/Answer is Ended for more Question/Answer Please Subscribe our Paid Version ,Thanks'
            
            })
                
       elif(account==1):
            data=lib.get_user_data_free_paid(userid,deviceid,date)
            if(data<=200):
                
                  if(value=="required"):
                    value='''You are an advance  Chatbot! As a sophisticated AI developed with advanced embedding technology You will use the data provided at the last paragraphs, you are expected to offer precise, detailed, and timely responses to user inquiries. Moreover, you have a responsibility to guide the conversation and ask follow-up questions to better understand user needs and provide tailored solutions. Here are some key points for your operation,Don't add (According to the tex) this type of context in response:

          Guiding the Conversation: As an intelligent system, you have the ability to guide the chat and steer the conversation in a helpful direction using the provided data below stay in the contaxt. If the user provides a vague or unclear request, politely ask for more information to better assist them. For instance, 'Can you please provide more details?'
          
          Handle Specific Queries according to the data provided and give informative rich answers.
          
          Providing Prompt Responses: Speed and accuracy are key. However, the complexity of the query might affect your response time. Ensure you're optimized to manage this balance.
          Asking Follow-Up Questions: One of your key roles is to probe for more information when required. If the user's question is broad or could have multiple interpretations, ask follow-up questions to clarify their intention. For example, 'Would you like to know about the history of AI or its current applications?'
          Maintaining Context: You can understand the context of conversations while staying in the limit of the data provide . So, if a user asks for further clarification or has additional queries, you should provide suitable responses based on the ongoing context.
          .'''   
                    last_element =  model.ask_english(query,value,userid,chatid,deviceid,date)
                    return jsonify({          
                 
                  '2 Question':query,
                  '1 Answer':last_element
            
               })
                   
  
          
              
            else:
                return jsonify({          
               'PaidMode' : 'You were in PaidMode you Free 100 Limit of Question/Answer is Ended for more Question/Answer Please Subscribe Again our Paid Version ,Thanks'
            
            })
      else:
         return jsonify({          
               'User Authentication' : 'Please Check your Email and Password'
            
            })     
            
      
          
          
          
        
   
    @app.route('/getchat/<string:userid>/<int:chatid>',methods = ['GET'])
    def getuserchat(userid,chatid,lang):
           
            data=lib.get_user_data(userid,chatid)
           
            return jsonify({
            'results': data
            
              })
    @app.route('/createuser/<string:firstname>/<string:lastname>/<string:email>/<string:password>',methods = ['POST'])
    def createuser(firstname,lastname,email,password):
      checkuser=lib.createusers(firstname,lastname,email,password)
      if(checkuser==0):
        return jsonify({          
               'Alert' : 'Invalid Email Please Enter Valid Email (user@gmail.com)'
            
            })
      elif(checkuser==1):
        return jsonify({          
               'Congratulations' : 'User Created Successfully'
            
            })
      else:
        return jsonify({          
               'Alert' : 'User Already Exist'
            
            })
      pass
if __name__=="__main__":   
  app.run(host='0.0.0.0')

