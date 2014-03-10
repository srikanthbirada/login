from django.shortcuts import render
from django.shortcuts import render, render_to_response
from login.views import error403
from django.template import RequestContext
from django.http import HttpResponse
from venuemonk.forms import *
from venuemonk.models import *
# Create your views here:

def list(request):
        try:
                logged_inside = request.session['Loggedinside']
                if logged_inside:
                        venue_list_tuple = VenueList.objects.all()
                        return render_to_response('Venue/viewall.html',{'Venuelist':venue_list_tuple},RequestContext(request))
                else:
                        return error403(request)
        except KeyError:
                return error403(request)

	

	

def add_venue(request):
	try:
		logged_inside = request.session['Loggedinside']
                if logged_inside:
			if request.method=='POST':
                        	request.session.set_test_cookie()
                                if request.session.test_cookie_worked():
                                	request.session.delete_test_cookie()
                                else:
                                	return HttpResponse("Please enable cookies and try again")
                                venue_form = venuemonkForm(request.POST)
                                is_valid_venueform = venue_form.is_valid()
                                if is_valid_venueform:
                                	v = venue_form.save(commit=False)
                                        v.save()
                                        return HttpResponse("added")
                                else:
                               		return render_to_response('Venue/addVenue.html',{'Venue':venue_form},RequestContext(request))
			else:
                        	venue_form = venuemonkForm()
                                return render_to_response('Venue/addVenue.html',{'Venue':venue_form},RequestContext(request))
		else:
                	return HttpResponse("no")
	except KeyError:
		return error403(request)

