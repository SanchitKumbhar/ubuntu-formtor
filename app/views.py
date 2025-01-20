from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
import json
import pandas as pd
from django.forms.models import model_to_dict
import os
from dotenv import load_dotenv
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def configure():
    load_dotenv()

def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        position = request.POST.get("position")
        user = CustomUser.objects.create(email=email)
        user.set_password(password)
        user.save()

        if user is not None:
            login(request, user)

            return redirect("/")
        


    return redirect("/app")

def loginuser(request):
    if request.method == 'POST':
        email = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        previous_url = request.META.get('HTTP_REFERER', None)
        print(type(previous_url))
        if user is not None:
            login(request, user)
            return redirect('/app')
        else:
            return redirect("/")

def auth(request):
    return render(request,"auth.html")

def home(request):
    return render(request,"home.html")


def app(request):
    if request.user.is_authenticated:
        return render(request,"formextend.html",{'data':FormInfo.objects.filter(user=request.user)})
    else:
        return redirect('/auth')


def PreprocessData(formapi, file):
    schema = []
    for index in range(len(formapi)):
        key = formapi[index]
        schema.append(key.get("question"))

    df = pd.DataFrame(columns=schema)

    # # # Save the DataFrame to an Excel file
    df.to_excel(f'files/{file}', index=False)

    print("Excel file created successfully!")


def submit_form(request, pk):
    try:
        # Parse the JSON data from the request body
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        # Do something with the data (e.g., save to database, process further)
        event_instance = FormInfo.objects.get(id=pk)

        form_data = FormData(data=data, customuser=request.user, event=event_instance)
        form_data.save()

        # PreprocessData(data, file)

        # Send a response back to the client
        return JsonResponse({"status": "success", "received": data})

    except json.JSONDecodeError as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)

@login_required
def create_form(request, pk):

    return render(request, "manager_form.html", {'pk': pk})
    # return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@login_required
def event_info(request):
    if request.method == "POST":
        eventname = request.POST.get("eventname")
        eventorganizer = request.POST.get("eventOrganizer")
        eventday = request.POST.get("eventday")
        eventdate = request.POST.get("eventdate")
        eventtime = request.POST.get("eventtime")
        eventabout = request.POST.get("eventabout")

        eventobj = FormInfo(eventname="eventname", eventorganizer=eventorganizer, eventday=eventday, eventdate=eventdate,
                                    eventtime=eventtime, eventabout=eventabout, user=request.user)
        eventobj.save()

        return redirect(f"/create_form/{eventobj.pk}")

    return render(request, "form-registration.html")


def form_render(request,pk):
    if FormData.objects.get(event=pk).timestamp ==  date.today():
        return HttpResponse("Page Closed")   
    else:
        return render(request,"client-form.html",{'id':pk})


def formapi(request,pk):
    if request.method=='GET':
        eventinstance=FormInfo.objects.get(pk=pk)
        get_instance=FormData.objects.get(event=pk)
        return JsonResponse(model_to_dict(get_instance))



# this feature editing is stopped for a while
def Draft(request):
    jsondata = json.loads(request.body)
    eventinstance=FormInfo.objects.get(pk=jsondata.get('pk'))

    draftinstance=DraftModel.objects.filter(event=eventinstance).exists()

    if draftinstance is False:
        DraftModel.objects.create(user=request.user,event=eventinstance,data=jsondata.get('data'))
    else:
        draftinstance=DraftModel.objects.filter(event=eventinstance)
        DraftModel.data=jsondata.get('data')
        DraftModel.event=draftinstance
        DraftModel.user=request.user

    return JsonResponse({
        'success' : 200
    })

import openai
# large dataIntegration code:
def dataItegration(request):

    configure()
    if request.method == 'POST':
        jsonMsg=json.loads(request.body)
        print(jsonMsg.get("msg"))

    return JsonResponse({
        'succ' : 'ok'
        })



# def GetDraft(request,pk):
#     if request.method == 'GET':
#         eventinstance=EventInformation.objects.get(pk=pk)
#         draftinstance=DraftModel.objects.get(event=eventinstance)
#         return JsonResponse({draftinstance.data[0]})

def AnswerAPI(request,id):
    jsondata=json.loads(request.body)
    print(jsondata)
    eventinstance=FormInfo.objects.get(pk=id)
    Answers.objects.create(answer=jsondata,event=eventinstance,username="Test",user=eventinstance.user)

    return JsonResponse({
        'success' : 200
    })

@login_required
def  Responses(request,id):
    var=FormInfo.objects.get(pk=id)
    if var.user!=request.user:
        return HttpResponse("No responses")
    else:
        return render(request,"responses.html",{'responses':Answers.objects.filter(event=id).filter(event=id)})

@login_required
def Answer(request,id):
    return render(request,"answer.html",{
        "id" : id
    })

def logoutuser(request):
    logout(request)
    return redirect("/")    

from django.core import serializers
def AnswerRender(request,id):
    data=Answers.objects.get(pk=id,user=request.user).answer
    return JsonResponse({
        
        'data' : data
    })
