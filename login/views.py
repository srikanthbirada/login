from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
def home(request):
	try:
		logged_inside = request.session['Loggedinside']
		if logged_inside:
			return render_to_response('home.html')
		else:
			return error403(request)
	except KeyError:
		return error403(request)

def error403(request):
	return render_to_response('error/error403.html', {}, RequestContext(request))
