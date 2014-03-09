from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from register.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	error = []
	if request.method=='POST':
		request.session.set_test_cookie()
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
		else:
			return HttpResponse("Please enable cookies and try again")
		form = LoginForm(request.POST)
		if form.is_valid():
			inp_username=request.POST['username']
			inp_password=request.POST['password']
			user_tuple = User.objects.all().filter(username = inp_username)
			if user_tuple:
				actual_pwd = user_tuple[0].password
				if inp_password ==actual_pwd:
					request.session['Loggedinside'] = True
					request.session['username'] = inp_username
					return HttpResponseRedirect('/home')
			else:
				error.append('username not found or username password not matched')
		else:
			error.append('incomplete form')
	else:
		form=LoginForm()
	return render_to_response('register/login.html',{'form':form,'error':error},RequestContext(request))

def logout(request):
	try:
		del request.session['Loggedinside']
		del request.session['username']
		request.session.flush()
	except KeyError:
		pass
	return render_to_response('register/logout.html')
