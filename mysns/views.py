#coding;utf-8
from django.http import HttpResponse
from django.template import Template,Context,RequestContext
from django.shortcuts import render_to_response,redirect
import datetime
import os
import  mysns.sns_dao as s_dao
from   mysns.forms import *

from  django.contrib.auth.forms import *
from django.http import HttpResponseRedirect

	
def hello(request):
#    now = datetime.datetime.now()
	if 'id' in request.GET:
		_id=request.GET['id']
	
	_id=int(_id)
	if _id==0:
		l1=s_dao.get_all()
	else:
		l1=s_dao.get_by_id(_id)
		
	return render_to_response('index_temp_file.html', {'l_xx':l1})
	
def get_sys_info(request,ss):
	paths=os.getcwd()
	html="<html><body>%s</body></html>"% paths
	return HttpResponse(html)
def index_temp(request,input_name):
	t=Template('My name is {{name}}')	
	c=Context({'name':input_name})
	return HttpResponse(t.render(c))
def index_file(request,input_name):
	return render_to_response('page1/index_temp_file.html', {'color':input_name})
def index_sns(request,_id):
	_id=int(_id)
	if _id==0:
		l1=s_dao.get_all()
	else:
		l1=s_dao.get_by_id(_id)	
	return render_to_response('index_temp_file.html', {'l_xx':l1})
def form(request):
	if request.user.is_authenticated():
		l1=[]
		f=SnsForm()
		if request.method == 'POST':
			name=request.POST['name']
			msg=request.POST['content']
			s_dao.save(name=name,content=msg)
		l1=s_dao.get_all()
		return render_to_response('form.html',{'l1':l1,'f':f,'name':request.user.username},context_instance=RequestContext(request))
        return HttpResponseRedirect("/accounts/login/")

def del_by_id(request):
	if '_id' in request.GET:
		_id=request.GET['_id']
		s_dao.del_by_id(_id)
	return redirect('/form')
def update_by_id(request):
	if request.method == 'POST':
		_id=request.POST['n_id']
		name=request.POST['name']
		msg=request.POST['content']
		s_dao.update_by_id(_id=_id,name=name,content=msg)
	return redirect('/form')
def to_edit(request):	
	f=SnsForm()
	if '_id' in request.GET:
		_id=request.GET['_id']
		return render_to_response('edit_form.html',{'id':_id,'f':f},context_instance=RequestContext(request))
	else:	
		return redirect('/form')
	
def register(request):
	form=UserCreationForm()
	if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                        new_user = form.save()
		#	return redirect('/form')	
			return HttpResponseRedirect('/form')
	if request.method == 'GET':
		#return render_to_response('acounts/register.html',{'form':form},context_instance=RequestContext(request))
		return render_to_response('acounts/register.html',{'form':form},context_instance=RequestContext(request))
	#####
        #(r'^about_us$',about_us),
       # (r'^about_us_history$',about_us_history),
       # (r'^about_us_team$',about_us_team,
       # (r'^about_us_mission$',about_mission),
       # (r'^product_show$',product_show),
        #(r'^gallery$',gallery),
        #(r'^contact_us$',contact_us),
        #(r'^blog$',blog),
def index(request):
	return render_to_response('index.html')
def about_us_history(request):
	return render_to_response('history.html')
def about_us_team(request):
	return render_to_response('theteam.html')
def about_us_mission(request):
	return render_to_response('mission.html')
def product_show(request):
	return render_to_response('property.html')
def gallery(request):
	return render_to_response('gallery.html')
def contact_us(request):
	return render_to_response('contactus.html')
def blog(request):
	return render_to_response('blog.html')
def about_us(request):
	return render_to_response('aboutus.html')
def villa(request):
	return render_to_response('villa.html')
def bungalows(request):
	return render_to_response('bungalows.html')
def apartments(request):
	return render_to_response('apartments.html')
	
			
	
	
