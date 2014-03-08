from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from register.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	if request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			user = User.objects.all()
			for u in user:
				if username == u.username and password == u.password:
					return HttpResponseRedirect('/home')
			else:
				return HttpResponseRedirect('/login')
		else:
			return render_to_response('login.html',{'form':form},RequestContext(request))
	else:
		form=LoginForm()
		return render_to_response('login.html',{'form':form},RequestContext(request))