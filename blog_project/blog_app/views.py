from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        a=post_register.objects.all()
        for i in a:
            if(i.username==username and i.password==password):
                request.session['id']=i.id
                return redirect(post_blog)
        else:
                
                return HttpResponse('failed...')

    return render(request,'login.html')

def register(request):
    if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          mobile=request.POST.get('mobile')
          username=request.POST.get('username')
          password=request.POST.get('password')

          a=post_register(name=name,email=email,mobile=mobile,username=username,password=password)
          a.save()
          return redirect(login)
    return render(request,"register.html")

def post_blog(request):
    if request.method=="POST":
        userid=request.session['id']
        title=request.POST.get('title')
        description=request.POST.get('description')
        tag=request.POST.get('tag')
        date=request.POST.get('date')
        a=my_blog(userid=userid,title=title,description=description,tag=tag,date=date)
        a.save()
        return redirect(display)
    
    
    return render(request,"post.html")
        



# def reg_login(request):
#         if "register" in request.method=='POST':
#           name=request.POST.get('name')
#           email=request.POST.get('email')
#           mobile=request.POST.get('mobile')
#           username=request.POST.get('username')
#           password=request.POST.get('password')

#           a=post_register(name=name,email=email,mobile=mobile,username=username,password=password)
#           a.save()
#           return HttpResponse("Register success...")
          
#         elif "login" in request.method=='POST':
#            username=request.POST.get('username')
#            password=request.POST.get('password')
#            a=post_register.objects.all()
#            for i in a:
#               if(i.username==username and i.password==password):
#                 return HttpResponse('success...')
#            else:
                
#                 return HttpResponse('failed...')
#         else:

#            return render(request,'login.html')
def display(request):
     title=[]
     description=[]
    #  tag=[]
     date=[]
     a=my_blog.objects.all()
     for i in a:
          ptitle=i.title
          title.append(ptitle)
          pdescription=i.description
          description.append(pdescription)
        #   ptag=i.tag
          #tag.append(ptag)
          pdate=i.date
          date.append(pdate)
     mylist=zip(title,description,date)
     
     return render(request,'display.html',{'post':mylist})

def publish(request):
     if request.method=="POST":
        userid=request.session['id']
        title=request.POST.get('title')
        description=request.POST.get('description')
        tag=request.POST.get('tag')
        date=request.POST.get('date')
        a=postpub(puserid=userid,ptitle=title,pdescription=description,ptag=tag,pdate=date)
        a.save()
        
        
     
     



     return render(request,"publish.html")
          
               