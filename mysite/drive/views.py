# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from forms import CoachForm,UserCreationForm
from models import Coach,School
def update_coach(request,id=u'0'):
	if id != None:
		coach=Coach.objects.get(id=int(id))
	else:
		coach=None

	if request.method == 'POST':
		form = CoachForm(request.POST,request.FILES,instance=coach)
		if form.is_valid():
			if request.FILES.has_key('photo'):
				handle_uploaded_file(request.FILES['photo'])
			form.save()
		
	else:
		form = CoachForm(instance=coach)
			
	return render_to_response('drive/update_coach.html', RequestContext(request, {'form': form}))



def handle_uploaded_file(f):
	import os
	file_name = '/tmp/tmp.pic'
	with open(file_name, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
		os.remove(file_name)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/drive/update_coach.html")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html",  RequestContext(request, {
        'form': form}))		
