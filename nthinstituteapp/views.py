from django.shortcuts import render
from.models import CoursesData,ContactData,CommentData
from.forms import ContactForm, CommentForm
from django.contrib.auth.models import User
def homepage(request):
    return render(request,'homepage.html')

def contactpage(request):
    if request.method =='GET':
        form=ContactForm()
        return render(request,'contactpage.html',{'form':form})
    else:
        form=ContactForm(request.POST)
        if form.is_valid():
            ContactData(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            location=request.POST.get('location'),
            courses=request.POST.get('courses'),
            referred_by=request.POST.get('referred_by')
            ).save()
            form=ContactForm()
            return render(request,'contactpage.html',{'form':form})


def servicespage(request):
    courses=CoursesData.objects.all()
    return render(request,'servicespage.html',{'courses':courses})

def feedbackpage(request):
    if request.method =="GET":
        form=CommentForm()
        return render(request,'feedbackpage.html',{'form':form})
    else:
        form=CommentForm(request.POST or None)
        if form.is_valid():
            content=request.POST.get('content')
            user=request.user
            
            data=CommentData.objects.create(user = user, content = content)
            data.save()
            return render(request,'feedbackpage.html',{'form':form})

def gallerypage(request):
    return render(request,'gallerypage.html')


# Create your views here.
