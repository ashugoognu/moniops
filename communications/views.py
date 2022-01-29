from django.shortcuts import render

# Create your views here.

import plivo
from django.conf import settings                                                                                                                                                      
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class CallApi():
    def __init__(self, from_number=None, to_number=None, url=None, message=None):
        print('init called')
        self.from_number = from_number
        self.to_number = to_number
        self.url = url
        self.message = message

    def voice_call(self):
        client = plivo.RestClient('MANZCWMGRIZJGZYJA1OT', 'ZTlmNzczMTcxNDRjOTE0YmRlMDY1ZmM5MDRiN2Jj')
        
        print(self.to_number)
        print(self.from_number)
        print(self.url)
        return "success"         #Temp Rtn comment if not in use
        for i in self.to_number:
            response = client.calls.create(
                from_= self.from_number,
                to_= i,
                answer_url= self.url,
                answer_method='GET', )
            print(response)
        return "success"
        
    def sms_api(self):
        client = plivo.RestClient('MANZCWMGRIZJGZYJA1OT', 'ZTlmNzczMTcxNDRjOTE0YmRlMDY1ZmM5MDRiN2Jj')
        print(self.to_number)
        print(self.from_number)
        print(self.message)
        return "success"     #Temp Rtn comment if not in use
        for i in self.to_number:
            response = client.messages.create(
            src = self.from_number,
            dst = i, 
            text= self.message)
        
        return "Success Send Message"
    
    def email_api(self):
                
        return "Empty Email Function...."
        




# import sys

# sys.path.append(".")

# from APIClass import CallApi as Communication

# from_number = "NUmber"
# to_number = ['To Number']
# url = 'https://s3.amazonaws.com/plivosamplexml/speak_url.xml'
# message = "Text Message"

# obj1 = Communication(from_number, to_number, url, message)
# responce = obj1.voice_call()
# print(responce)

# print("---------------")
# responce = obj1.sms_api()
# print(responce)
