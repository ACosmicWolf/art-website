import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from django.core.mail import send_mail


from .models import Art

""" all_objects = Art.objects.all()

art = []
img_list = []
img_name = []
for i in all_objects:
    art.append((i.name,i.art.name)) """

# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        hi = "Hello"
        email = request.POST['email']
        message = request.POST['message']
        message = f"Message From {name} with email: {email}\n"+message
        send_mail(
            f"{name} Contacted you on your website.",
            message,
            ['arshita10@gmail.com','arshmehta009@gmail.com'],
            fail_silently = False
        )

        return render(request,'pages/contact.html', context={'name':f"Thanks {name}!!",'message':"We received your message and will respond shortly. \n If you have provided a correct email."})
    else:
        return render(request,'pages/contact.html')


def portfolio(request):
    path = settings.MEDIA_ROOT
    if request.method == "GET":
        art = Art.objects.all()
    context = {'images' : art}
    return render(request,'pages/portfolio.html',context)

def about(request):
    return render(request, 'pages/about.html')

def notfound(request):
    return render(request, 'notfound.html')