from django.shortcuts import render
from django.http import HttpResponse

from .models import Painting,Comment
# Create your views here.
def home(request):
    return render(request,"pages/home.html")
def contact(request):
    return render(request,"pages/contact.html")

def portfolio(request):
    if request.method == "GET":
        paintings = Painting.objects.all()
        print(len(paintings))
        l=[[],[],[]]
        for i in paintings:
            if(len(l[0]) == len(l[1])):
                comments = Comment.objects.filter(painting=i)
                for n in comments:
                    print(n.comment)
                l[0].append([i,comments])
            elif(len(l[1]) == len(l[2])):
                comments = Comment.objects.filter(painting=i)
                print(comments)
                l[1].append([i,comments])
            else:
                comments = Comment.objects.filter(painting=i)
                print(comments)
                l[2].append([i,comments])
        return render(request,"pages/portfolio.html",{"a":l[0],"b":l[1],"c":l[2]})