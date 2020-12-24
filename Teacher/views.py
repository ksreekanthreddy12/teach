from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,"index.html")
def home(request):
	return render(request,"home.html")
def contact(request):
	return render(request,"contact.html")
def services(request):
	return render(request,"services.html")
def register(request):
    return render(request,"register.html")