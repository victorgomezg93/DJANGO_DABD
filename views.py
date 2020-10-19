from django.shortcuts import render
from django.views.generic import CreateView

def home(request):
	template = 'home.html'
	context = {}
	return render(request,template,context)