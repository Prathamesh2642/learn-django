from django.shortcuts import render,redirect

from .models import *
# Create your views here.

def receipes(request):
    if request.method=='POST':
        #obtain data into backend 
        data=request.POST
        receipe_image=request.FILES.get("receipe_image")
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')

        # store it in db
        Receipe.objects.create(receipe_name=receipe_name,
                                receipe_description=receipe_description,
                                 receipe_image=receipe_image)
        
        return redirect('/receipes')

        # print(receipe_name,receipe_description,receipe_image)
    queryset=Receipe.objects.all()
    context={'receipe':queryset} # context is key value pair
    return render(request,"receipes.html",context)


