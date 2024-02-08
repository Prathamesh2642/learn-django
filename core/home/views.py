from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

# names={'prathamesh':21,'abc':22,'zxc':44}
names=[{'name':'prathamesh','age':21},{'name':'sanjay','age':51},{'name':'alka','age':42},{'name':'tejas','age':17}]

random_text="Lorem ipsum dolor sit, amet consectetur adipisicing elit. Earum dolores atque tempore, aliquam natus vero temporibus aperiam recusandae modi iste adipisci voluptates velit. Placeat praesentium dolores nobis libero hic ipsum!Facilis, harum? Itaque at id veniam, modi quas nobis fuga animi porro quam, maiores, aliquid pariatur expedita fugiat assumenda autem quis! Totam, adipisci omnis iusto laudantium nam quasi quae itaque?"

Attendance=['Prathamesh','sanjay','alka','tejas']

def home(request):
    # return HttpResponse("<h1>Hello this is django server</h1>")
    return render(request,"index.html",context={'names':names,'random_text':random_text,'attendance':Attendance,'page':'homepage'})

def contact(request):
    # return HttpResponse("<h1>Hello this is django server</h1>")
    return render(request,"contacts.html",context={'page':'contact'})

def about(request):
    # return HttpResponse("<h1>Hello this is django server</h1>")
    return render(request,"about.html",context={'page':'about'})

def success_page(requests):
    print("*"*10)
    return HttpResponse("<p> This is a new page</p>")