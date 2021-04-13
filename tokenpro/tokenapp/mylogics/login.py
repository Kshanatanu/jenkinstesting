from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import JsonResponse,HttpResponse
from bson import ObjectId
import requests
import datetime
import time
import base64
import json
import jwt
from cryptography.fernet import Fernet
from tokenpro.settings import db

# Create your views here.
def hello(request):
    a=db.testcollection.find({})
    for i in a:
        print(i)
    key = Fernet.generate_key()
    f = Fernet(key)
    private_key=f.encrypt(b"Hello india")
    json_data = {
                  "access_token":"MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
                 "token_type":"bearer",
                 "expires_in":3600,
                 "refresh_token":"IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
                 "scope":"create"
                }
    token=jwt.encode(json_data,private_key, algorithm="HS256")
    print(token)
    dtoken=jwt.decode(token,private_key, algorithm="HS256")
    print(dtoken)
    return HttpResponse("hello")

def login_page(request):
    
    if 'email' in request.session:
        del request.session['email']

    emailId = request.POST.get('email')
    #password = base64.b64encode(bytes(request.POST.get('password'), 'utf-8'))
    #password = str(password, 'utf-8')
    password = request.POST.get('password')

    usersDB = dbwallet.superadmin.find(
        {'email': emailId, 'password': password})
    if usersDB.count() > 0:

        for user in usersDB:
            
            if IS_AUTH_SERVER == 1 or IS_AUTH_SERVER == "1":
                json_data = {
                    "userId": str(user['_id']),
                    "userType": "admin",
                    "multiLogin": "true",
                    "AllowedMax": "5",
                    "immediateRevoke": "false",
                    "metaData": {},
                    "accessTTL": "48h",
                    "refreshTTL": "180h"
                }
                auth_server_response = requests.post(AUTH_SERVRE+"accessKeys", json=json_data, verify=False)
                
            
            
            request.session['email'] = emailId
            request.session['timezone'] = request.POST.get('timezone')
            #request.session['accessToken'] = '123456'
            request.session['accessToken'] = auth_server_response.json()['data']['accessToken']
            request.session['refreshToken'] = auth_server_response.json()['data']['refreshToken']
            '''
            else:
                
                request.session['email'] = emailId
                request.session['timezone'] = request.POST.get('timezone')
                request.session['accessToken'] = "0123456789"
            '''
        return redirect('dashboard')
    else:
        return render(request, 'wallet/login.html', context={"emptyflag": 1})
    