from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from matplotlib.pyplot import connect
import mysql.connector

def main_login(request):
    template = loader.get_template("login_page.html")
    return HttpResponse(template.render({}, request))

def detection(request):
    pass

