from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Painting,Comment
# Create your views here.
def home(request):
    return render(request,"pages/home.html")
def contact(request):
    return render(request,"pages/contact.html")
def signup(request):
    return render(request,"pages/contact.html")

def portfolio(request):
    paintings = Painting.objects.all()
    l=[[],[],[]]
    for i in paintings:
        comments = Comment.objects.filter(painting=i)
        if(len(l[0]) == len(l[1])):
            l[0].append([i,comments])
        elif(len(l[1]) == len(l[2])):
            l[1].append([i,comments])
        else:
            l[2].append([i,comments])
    if request.method == "GET":
        return render(request,"pages/portfolio.html",{"a":l[0],"b":l[1],"c":l[2]})
    elif request.method == "POST":
        name = request.POST['name']
        comment = request.POST['comment']
        print(request.POST['painting'])
        painting = Painting.objects.get(name=request.POST['painting'])
        c = Comment(
            name = name,
            comment=comment,
            painting=painting
        )
        c.save()
        return render(request,"pages/portfolio.html",{"a":l[0],"b":l[1],"c":l[2]})
