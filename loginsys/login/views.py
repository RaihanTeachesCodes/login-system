from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import encryption_data

import mysql.connector

#from login.models import encryption_data

"""connected = True

try:
    if connected:
        db = mysql.connector.connect(host="localhost", user="raihan",password="1234", auth_plugin='mysql_native_password')
        mycursor = db.cursor()
except:
    connected = False
    """

user_id = {}

def main_login(request):
    template = loader.get_template("login_page.html")
    return HttpResponse(template.render({}, request))

def detection(request):
    login = False
    username = request.POST["user"]
    password = request.POST["password"]
    correct_template = loader.get_template("correct_move_on.html")
    wrong_template = loader.get_template("wrong_move_on.html")
    user_data = encryption_data.objects.all().values()

    
    for i in list(range(len(list(user_data)))):
        if user_data[i]["username_in"] == username and user_data[i]["password_in"] == password:
            user_data2 = user_data[i]["id"]
            context = {"check_id": str(user_data2), }
            user_id["ids"] = str(user_data2) 
            login = True
        else:
            login = False

    

    if login:
        return HttpResponse(correct_template.render(context, request))
    else:
        return HttpResponse(wrong_template.render({}, request))

def main_app(request):
    template3= loader.get_template("main_screen.html")

    return HttpResponse(template3.render({}, request))
    

def register_page(request):
    template2 = loader.get_template("register_page.html")
    return HttpResponse(template2.render({}, request))

def reg_process(request):
    nusername = request.POST["nuser"]
    npassword = request.POST["npassword"]
    
    data_check = encryption_data(username_in=nusername, password_in=npassword)
    data_check.save()
    return HttpResponseRedirect(reverse('login'))

def see_database(request):
    mymembers = encryption_data.objects.all().values()
    Template3 = loader.get_template("database.html")
    context = {
        "mymembers": mymembers
    }
    return HttpResponse(Template3.render(context, request))

def delete(request, id):
  row = encryption_data.objects.get(id=id)
  row.delete()
  return HttpResponseRedirect(reverse('database'))





