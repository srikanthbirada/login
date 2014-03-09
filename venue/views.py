from django.shortcuts import render,render_to_response
from login.views import error403
from django.template import RequestContext
from django.http import HttpResponse
from venue.models import *
from venue.forms import *

# Create your views here.
def list(request):
	try:
		logged_inside = request.session['Loggedinside']
		if logged_inside:
			venue_list_tuple = VenueList.objects.all()
			return render_to_response('venue/viewall.html',{'venuelist':venue_list_tuple},RequestContext(request))
		else:
			return error403(request)
	except KeyError:
		return error403(request)
def add(request):
	if request.method == 'POST':
		request.session.set_test_cookie()
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
		else:
			return HttpResponse("Please enable cookies and try again")
		venueform = AddVenue(request.POST)
		ownerform = AddOwner(request.POST)
		is_valid_venueform = venueform.is_valid()
		is_valid_ownerform = ownerform.is_valid()
		if is_valid_venueform and is_valid_ownerform:
			new_venue_id = VenueList.Objects.all().count() +1
			new_owner_id = Owner.objects.all().count()+1
			new_v_n = 'sdfs'
			new_v_a = 'asd'
			new_o_n = "oadfjs"
			new_o_m = 123
			new_o_e = "a@g.com"


			owner_data = ownerform.save(commit=False)
			owner_data.owner_id = new_owner_id
			venue_data = venueform.save(commit=False)
			venue_data.venue_id = new_venue_id
			Owner(owner_id = 101,name = new_o_n,mobile_number = new_o_m,email=new_o_e).save()
			VenueList(venue_data).save()
			return HttpResponse("Added Successul")
		else:
			return render_to_response('venue/add.html',{'v':venueform,'o':ownerform},RequestContext(request))
	else:
		venueform = AddVenue()
		ownerform = AddOwner()
                return render_to_response('venue/add.html',{'v':venueform,'o':ownerform},RequestContext(request))

