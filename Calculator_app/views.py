from django.shortcuts import render,redirect
from django.http import HttpResponse 
from.models import *
from.forms import *
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.views import generic

# it is used in django to get a text response in our web page

# Create your views here.
def first(request):
    return HttpResponse("My First Django Page....")

#second
def second(request):
    return HttpResponse("My Second Django Page...")

# render : is a function used to connect your function with templates
#           to return a user interface layer 

def third(request):
    return render(request,'third.html')

def fourth(request):
    return render(request,'fourth.html')
def reg_form(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        address=request.POST.get('Address')
        date=request.POST.get('dob')
        password=request.POST.get('password')
        confpassword=request.POST.get('confpassword')
        if password==confpassword:
            a=register(fname=fname,lname=lname,username=username,email=email,phoneno=phone,address=address,gender=gender,dob=date,password=password)
            a.save()
            return HttpResponse("Registration success...")
        else:
            return HttpResponse("Incorrect password....")
    return render(request,'reg_form.html')

# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         a=register.objects.all()  #it is an ORM query that is used to fetch a table in our model field
#         for i in a:
#             if (i.email==email and i.password==password):
#                 return HttpResponse("login successfully....")
#         else:
#             return HttpResponse("login failed...")
#     return render(request,'login.html')


def home(request):
    return render(request,'home.html')
def file(request):
    if request.method=='POST':
        filename=request.POST.get('filename')
        fileimage=request.FILES.get('fileimage')
        description=request.POST.get('description')
        b=fileupload(filename=filename,fileimage=fileimage,description=description)
        b.save()
        return HttpResponse("Success....")
    return render(request,'file_upload.html')

def emp_reg(request):
    if request.method=='POST':
        empname=request.POST.get('empname')
        email=request.POST.get('email')
        comname=request.POST.get('companyname')
        designation=request.POST.get('designation')
        phone=request.POST.get('phone')
        a=emp(empname=empname,email=email,comname=comname,designation=designation,phone=phone)
        a.save()
        return HttpResponse(" Employee Registration success....")
    return render(request,'emp_reg.html')

def emp_search(request):
    if request.method=='POST':
        empname=request.POST.get('empname')
        phone=request.POST.get('phone')
        a=emp.objects.all()
        for i in a:
            if (i.empname==empname and int(i.phone)==int(phone)):
                return HttpResponse(" Registred user....")
        else:
            return HttpResponse("Not a registred user...")

    return render(request,'emp_search.html')

def product(request):
        if request.method=='POST':
            proname=request.POST.get('proname')
            proprize=request.POST.get('proprize')
            companyname=request.POST.get('companyname')
            quantity=request.POST.get('quantity')
            expiry=request.POST.get('expiry')
            description=request.POST.get('description')
            a=pro(proname=proname,proprize=proprize,companyname=companyname,quantity=quantity,expiry=expiry,description=description)
            a.save()
            return HttpResponse(" product Added success....")

        return render(request,'product.html')
def pro_search(request):
    if request.method=='POST':
        proname=request.POST.get('proname')
        companyname=request.POST.get('companyname')
        a=pro.objects.all()
        for i in a:
            if (i.proname==proname and i.companyname==companyname):
                return HttpResponse(" get  product....")
        else:
            return HttpResponse("Not get product...")

    return render(request,'pro_search.html')

def upload_files(request):
    if request.method=='POST':
        audioname=request.POST.get('audioname')
        audiofile=request.FILES.get('audiofile')
        videoname=request.POST.get('videoname')
        videofile=request.FILES.get('videofile')
        pdfname=request.POST.get('pdfname')
        pdffile=request.FILES.get('pdffile')
        
        b=files(audioname=audioname,audiofile=audiofile,videoname=videoname,videofile=videofile,pdfname=pdfname,pdffile=pdffile)
        b.save()
        return HttpResponse("Success....")
    return render(request,"upload_files.html")

def check_select(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        Malayalam=request.POST.get('Malayalam')
        if Malayalam=='on':
            Malayalam=True
        else:
            Malayalam=False
        English=request.POST.get('English')
        if English=='on':
            English=True
        else:
            English=False
        Hindi=request.POST.get('Hindi')
        if Hindi=='on':
            Hindi=True
        else:
            Hindi=False
        state=request.POST.get('state')
        b=select(fname=fname,Malayalam=Malayalam,English=English,Hindi=Hindi,state=state)
        b.save()
        return HttpResponse("success......")
    return render(request,'check_select.html')


def display(request):
    a=register.objects.all()
    return render(request,'display.html',{'data':a})
def empdis(request):
    b=emp.objects.all()
    return render(request,'emp_display.html',{'data':b})
def filedis(request):
    id=[]
    filename=[]
    fileimage=[]
    description=[]

    c=fileupload.objects.all()
    for i in c:
        id1=i.id
        id.append(id1)
        name1=i.filename
        filename.append(name1)
        image1=str(i.fileimage).split('/')[-1]
        fileimage.append(image1)
        des=i.description
        description.append(des)
    mylist=zip(id,filename,fileimage,description)#it returns a list of tuples
    return render(request,'file_display.html',{'data':mylist})


def uploaddis(request):
    id=[]
    audioname=[]
    audiofile=[]
    videoname=[]
    videofile=[]
    pdfname=[]
    pdffile=[]
    c=files.objects.all()
    for i in c:
        id1=i.id
        id.append(id1)
        audioname1=i.audioname
        audioname.append(audioname1)
        audio1=str(i.audiofile).split('/')[-1]
        audiofile.append(audio1)
        videoname1=i.videoname
        videoname.append(videoname1)
        video1=str(i.videofile).split('/')[-1]
        videofile.append(video1)
        pdfname1=i.pdfname
        pdfname.append(pdfname1)
        pdf1=str(i.pdffile).split('/')[-1]
        pdffile.append(pdf1)

    mylist=zip(id,audioname,audiofile,videoname,videofile,pdfname,pdffile)#it returns a list of tuples
    return render(request,'upload_display.html',{'data':mylist})



# create an html file audio name,audio,video name,video,pdf name,pdf
#cintext:is a dictionary in django which is used to pass our datas from backend to frontend


def update_data(request,id):
    a=register.objects.get(id=id)
    if request.method=='POST':
        a.fname=request.POST.get('firstname')
        a.lname=request.POST.get('lastname')
        a.username=request.POST.get('username')
        a.email=request.POST.get('email')
        a.phoneno=request.POST.get('phone')
        
        if str(request.POST.get('gender'))=='female' or str(request.POST.get('gender'))=='male':
            a.gender=request.POST.get('gender')
        else:
            a.save()
        a.save()
        return redirect(display)
    
    return render(request,'edit_profile.html',{'data':a})


def update_emp(request,id):
    a=emp.objects.get(id=id)
    if request.method=='POST':
        a.empname=request.POST.get('empname')
        a.email=request.POST.get('email')
        a.comname=request.POST.get('companyname')
        a.designation=request.POST.get('designation')
        a.phone=request.POST.get('phone')
        
        a.save()
        return redirect(empdis)
    
    return render(request,'edit_emp.html',{'data':a})



def img_edit(request,id):
    a=fileupload.objects.get(id=id)
    image=str(a.fileimage).split('/')[-1]
    if request.method=='POST':
        a.filename=request.POST.get('filename')
        a.fileimage=request.FILES['fileimage']
        a.description=request.POST.get('description')
   
        a.save()
        return redirect(filedis)
    
    return render(request,'edit_img.html',{'data':a,'img':image})


def files_edit(request,id):
    a=files.objects.get(id=id)
    if request.method=='POST':
        a.audioname=request.POST.get('audioname')
        if request.FILES.get('audiofile')==None:
            a.save()
        else:
            a.audiofile=request.FILES.get('audiofile')
            a.save()

        a.videoname==request.POST.get('videoname')
        if request.FILES.get('videofile')==None:
            a.save()
        else:
            a.videofile=request.FILES.get('videofile')
            a.save()

        a.pdfname=request.POST.get('pdfname')
        if request.FILES.get('pdffile')==None:
            a.save()
        else:
            a.pdffile=request.FILES.get('pdffile')
            a.save()
        a.save()
        return redirect(uploaddis)
    return render(request,"files_edit.html",{'data':a})


def profile_delete(request,id):
    a=register.objects.get(id=id)
    a.delete()
    return redirect(display)



def userregistration(request):
    if request.method=='POST':
        a=userreg(request.POST)
        if a.is_valid():
            us=request.POST.get('username')
            em=request.POST.get('email')
            fname=request.POST.get('first_name')
            lname=request.POST.get('last_name')
            password=request.POST.get('password')

            # cleaned_data=form cleaned data is where all validated fields are stored it returns a dictionary od validated fom input fields and the values
       
            b=User.objects.create_user(first_name=fname,last_name=lname,username=us,email=em,password=password)
            b.save()
            return HttpResponse(" Authenticated user added...")
        else:
            return HttpResponse("User not added....")
        
    else:
        form=userreg()
        return render(request,'user_form.html',{'form':form})
    

def userregis(request):
    if request.method=='POST':
        a=userform(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            em=a.cleaned_data['email']
            fname=a.cleaned_data['first_name']
            lname=a.cleaned_data['last_name']
            password=a.cleaned_data['password']
            conf=a.cleaned_data['conf']
            if password==conf:

            # cleaned_data=form cleaned data is where all validated fields are stored it returns a dictionary od validated fom input fields and the values
       
                b=User.objects.create_user(first_name=fname,last_name=lname,username=us,email=em,password=password)
                b.save()
                return HttpResponse(" Authenticated user added...")
            else:
                return HttpResponse("dosn't match...")
        
        else:
            return HttpResponse("failed")
    else:
        form=userform()
        return render(request,'auth_user.html',{'form':form})
    
# def custom_login(request):
#     if request.method=='POST':
#         form = userlogin(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user = authenticate(request,username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return HttpResponse('logged successfully...')
#             else:
#                 return HttpResponse('invalid username or password')
#         else:
#             return HttpResponse('invalid username or password')
#     else:
#         form=userlogin()
#         return render(request,'userlogin.html')
    

# # reverse_lazy
# # it is used to imply a lazy implementation of url
# #  used to redirect 


# class register(generic.CreateView):
#     form_class = regform
#     template_name='auth_user.html'
#     success_url=reverse_lazy('login')

# class login(generic.View):
#     form_class = logform
#     template_name = 'userlogin.html'
#     def get(self,request):
#         form = self.form_class
#         return render(request,self.template_name,{'form':form})
#     def post(self,request):
#         if request.method == 'POST':
#             a=logform(request.POST)
#             if a.is_valid():
#                 em=a.cleaned_data['email']
#                 ps=a.cleaned_data['password']
#                 b=regmodel.objects.all()
#                 for i in b:
#                     if em==i.email and ps==i.password:
#                         return HttpResponse("login success..")
#                 else:
#                     return HttpResponse("login failde...")
#             return HttpResponse("I nvalid credentials..")

    

    


# # redirect():is a method that is used to redirect from one function to another functions or ur