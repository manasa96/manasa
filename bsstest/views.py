from django.shortcuts import render, render_to_response, RequestContext
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect , HttpResponse
def bsstest(request):
    if request.method=='POST':
    	form = bssForm(request.POST or None)
	if form.is_valid():
            u_name=form.cleaned_data['first_name']
	    passwd=form.cleaned_data['password']
	    u = User()
	    u.set_password('passwd')
	    usr = User(username=u_name)
	    
            form.save()
	    u = User()
	    usr.save()
	    u.set_password('passwd')
	    
	    return render(request,"bsstest/sam.html",{"form":form})
    else:
	form = bssForm()
    	return render(request,"bsstest/bss_file.html",{"form":form})
def index(request):
    context =RequestContext(request)
    return render_to_response("bsstest/index.html",context)
def register(request):
    context = RequestContext(request)
    registered = False
    if request.method =='POST':
        user_form = UserForm(request.POST or None)
        
        if user_form.is_valid() :
            
            user = user_form.save()
            
	    user.set_password(user.password)
	    user.save()
            
	    registered = True
	    return render(request,"bsstest/bss_file.html")
	else:
	    print user_form.errors
    else:
	user_form = UserForm()
        
    return render_to_response( 'bsstest/register.html' , {'user_form':user_form ,'registered':registered}, context)   

'''def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            
            if user.is_active:
               
                login(request, user)
                return HttpResponseRedirect('/bsstest/')
            else:
               
                return HttpResponse("Your bss account is disabled.")
        else:
            
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    
    else:
        return render_to_response('bsstest/login.html', {}, context) '''
