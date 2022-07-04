import string
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import mysql.connector

db = mysql.connector.connect(host="localhost", user="raihan",password="1234", auth_plugin='mysql_native_password')
mycursor = db.cursor()

def main_login(request):
    template = loader.get_template("login_page.html")
    return HttpResponse(template.render({}, request))

def detection(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    return HttpResponse(str(mycursor.execute("SHOW DATABASES")))



