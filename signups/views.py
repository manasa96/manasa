from django.shortcuts import render, render_to_response, RequestContext
from .forms import *
"""
def home(request):
    

    return render_to_response("signups.html",
                               locals(),
                               context_instance=RequestContext(request))
"""
# Create your views here.

def Custom(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
    return render(request,"signups/sample.html",{"form":form})
