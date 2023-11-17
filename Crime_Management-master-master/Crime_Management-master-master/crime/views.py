from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User,auth
#import mysql.connector as p
import datetime
import time
from . forms import *
import random



# Create your views here.
def Run_Here(request):
    return render(request,"Run_Here.html")

def publiccomplaint(request):
    return render(request,"publiccomplaint.html")

def Add_Complaint(request):
    #Email= request.session['email']
    #reg=register_form.objects.get(Email=Email)
    #fn=reg.Name
    return render(request,"Add_Complaint.html")
    #return render(request,"Add_Complaint.html",{'fn':fn})
def add_complaint_public(request):
    #Email= request.session['email']
    #reg=register_form.objects.get(Email=Email)
    #fn=reg.Name
    return render(request,"publiccomplaint.html")
    #return render(request,"Add_Complaint.html",{'fn':fn})

def index(request):
    #Email= request.session['email']
    #reg=register_form.objects.get(Email=Email)
    #fn=reg.Name
    return render(request,"index.html")
    #return render(request,"index.html",{'fn':fn})
def admin_index(request):
    return render(request,"addpolice.html")


def criminalview(request):
    co=addcriminalls.objects.all()
   # Email= request.session['email']
    reg=register_form.objects.all()
    #fn=reg.Name
    return render(request,"criminalview.html",{'co':co})


def addcriminals(request):
    bn=request.session['bnname']
    return render(request,"addcriminals.html",{'bn':bn})

def finish(request):
   
    bn = request.session['bnname']
    bnnam = request.POST.get('bnn')
    crimename = request.POST.get('cnn')
    fil=fileupload.objects.all()
    if fileupload.objects.filter(bnname=bnnam).exists():
        if fileupload.objects.filter(crimename=crimename).exists():
            inn=fileupload.objects.get(crimename=crimename)
            valu=inn.value
            mgg="completed"
            if valu=="2":   
                inn.value=str(3)
                inn.save();
    return render(request,"reqdoc.html",{'fil':fil,'bn':bn,'mgg':mgg})

def reqdoc(request):
    bn = request.session['bnname']
    bnnam = request.POST.get('bnn')
    crimename = request.POST.get('cnn')
    fil=fileupload.objects.all()
    if fileupload.objects.filter(bnname=bnnam).exists():
        if fileupload.objects.filter(crimename=crimename).exists():
            inn=fileupload.objects.get(crimename=crimename)
            valu=inn.value 
            if valu=="1":
                inn.value=str(2)
                inn.save();
    return render(request,"reqdoc.html",{'fil':fil,'bn':bn})

def reqdoc2(request):
    bn = request.session['bnname']
    return render(request,"reqdoc.html",{'bn':bn})

def acceptdoc(request):
    fil=fileupload.objects.all()
    bn = request.session['bnname']
    return render(request,"acceptdoc.html",{'fil':fil,'bn':bn})

def viewcomp(request):
    com=complaint_details.objects.all()
    #bn = request.session['bnname']
    return render(request,"comp.html",{'com':com})

def publiccompl(request):
    co=complaint.objects.all()
    return render(request,"viewpubliccomp.html",{'co':co})

def contact(request):
    co=Missing.objects.all()
    return render(request,"viewmisscomp.html",{'co':co})


##############################################
def upload(request):
    com=complaint_details.objects.all()
    crimename = request.POST.get('cid')
    crimearea = request.POST.get('uid')
    bnname = request.POST.get('bname')
    files = request.FILES.get('upload')
    bn=bnname
    meg="file uploaded"
    print(files)
    value=str(1)
    if fileupload.objects.filter(crimename=crimename).exists():
        fill=fileupload.objects.get(crimename=crimename)
        pid=fill.id
        fil=fileupload(id=pid,crimename=crimename,crimearea=crimearea,bnname=bnname,files=files,value=value)
    else:
        fil=fileupload(crimename=crimename,crimearea=crimearea,bnname=bnname,files=files,value=value)
    fil.save();
    return render(request,"comp.html",{'meg':meg,'com':com,'bn':bn})

def viewcomp2(request):
    try:
   # bn=request.session['bnname']
        Email = request.POST.get('email')
        com=area.objects.filter(Email=Email)
        comm=register_form.objects.get(Email=Email)
        name=comm.Name
        coo=complaint_details.objects.get(Email=Email)
        img=coo.image
        fn=coo.firstname
        ln=coo.lastname
        are=coo.carea
        wip=coo.wip
    except:
        return render(request,"comp2.html")

    print(com)
    return render(request,"comp2.html",{'com':com,'name':name,'img':img,'fn':fn,'ln':ln,'are':are,'wip':wip})

def Complaintstatus(request):
    #Email= request.session['email']
    reg=register_form.objects.all()
    #fn=reg.Name
    comp=complaint_details.objects.all()
    com=complaint_details.objects.all()
    #carea=com.carea
    #crna=com.cname
    pro="waiting for process"
    # if fileupload.objects.all():
    #     fi=fileupload.objects.all()
    #     if fileupload.objects.all():
    #        val=fi.value
    #        if val=="3":
    #            pro="Process  Finished"
    #        elif val=="2":
    #             pro="proces Ongoing"
    #        else:
    #             pass
            
    return render(request,"complainstatus.html",{'comp':comp,'pro':pro})

def missingstatus(request):
    #Email= request.session['email']
    reg=register_form.objects.all()
   # fn=reg.Name
    comp=Missing.objects.all()
    return render(request,"missingstatus.html",{'comp':comp})

def crimemissing(request):
    comp=Missing.objects.all()
    return render(request,"crimemissingstatus.html",{'comp':comp})

def AddMissing(request):
    Email= "keralapolice@gmail.com"
    reg=register_form.objects.all
    return render(request,"AddMissing.html")


def branchlogin(request):
    meg="Login sucessfully"
    comp=Missing.objects.all()
    bnname = request.POST.get('user')
    bpass = request.POST.get('Password')
    
  
    if branches.objects.filter(bnname=bnname).exists():

        if branches.objects.filter(bpass=bpass).exists():
            meg="Login sucessfully"
            reg=branches.objects.get(bnname=bnname)
            fn=reg.bnname
            request.session['bnname']=reg.bnname
            return render(request,'policehome.html',{'meg':meg,'fn':fn,'comp':comp})
        else:
            print("password is not correct")
            meg="password is not correct..."
            return render(request,'Run_Here.html',{'meg':meg})   
    else:
        print('Branch name is not there...')
        meg="Email is not there..."
        return render(request,'Run_Here.html',{'meg':meg})

def finishh(request):
    comp=Missing.objects.all()
    idd = request.POST.get('idd')
    fn = request.POST.get('fn')
    coo=Missing.objects.get(id=idd)
    coo.status ="finished"
    coo.save();
    return render(request,'policehome.html',{'fn':fn,'comp':comp})

def chatpolice(request):
    bnname=request.session['bnname']
    reg=branches.objects.all()
    return render(request,"chatpolice.html",{'bnname':bnname,'reg':reg})
    

def branch(request):
    bnname = request.POST.get('bnname')
    bpass = request.POST.get('bpass')
    barea = request.POST.get('barea')
    address = request.POST.get('address')
    nopolice = request.POST.get('nopolice')
    profile = request.FILES.get('profile')
    meg="added sucessfully"
    print("profile",profile)
    if branches.objects.filter(bnname=bnname).exists():
        braa=branches.objects.get(bnname=bnname)
        pid=braa.id
        bran=branches(id=pid,bnname=bnname,bpass=bpass,barea=barea,address=address,nopolice=nopolice,profile=profile)
        bran.save();
        return render(request,"addpolice.html",{'meg':meg})
    else:
        bran=branches(bnname=bnname,bpass=bpass,barea=barea,address=address,nopolice=nopolice,profile=profile)
        bran.save();
        return render(request,"addpolice.html",{'meg':meg})

def chatpolice2(request):
    bnname=request.session['bnname']
    bbna = request.POST.get('bbna')
    fmg=chatregg.objects.filter(fromm=bnname)
    tmg=chatregg.objects.filter(too=bnname)
    return render(request,"chatpolice2.html",{'bnname':bnname,'bbna':bbna,'fmg':fmg,'tmg':tmg})

def chatreg(request):
    bnname=request.session['bnname']
    dchatt = request.POST.get('dchatt')
    fromm = request.POST.get('bib')
    too = request.POST.get('to')
    ts = time.time()   
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    chat=chatregg(date=date,time_h_m_s=timestamp,dchatt=dchatt,fromm=fromm,too=too)
    tmg=chatregg.objects.filter(too=bnname)
    chat.save();
    fmg=chatregg.objects.filter(fromm=bnname)
    return render(request,"chatpolice2.html",{'bnname':bnname,'bbna':too,'fmg':fmg,'tmg':tmg})
def add_police(request):
    return render(request,"addpolice.html")
def admincheck(request):
    username = request.POST.get('user')
    password = request.POST.get('Password')
    user = auth.authenticate(username=username,password=password)
   
    if user is not None:
        auth.login(request,user)
        meg="Login sucessfully"
        print("working")
        return render(request,"addpolice.html",{'meg':meg})
    else:
        print("invalid credentials")
        meg="Login failed: invalid credentials"
        return render(request,'Run_Here.html',{'meg':meg}) 

def logincheck(request): 
 
    Email = request.POST.get('Email')
    Password = request.POST.get('Password')
    username = request.POST.get('user')
  
    if register_form.objects.filter(Email=Email).exists():

        if register_form.objects.filter(Password=Password).exists():
            meg="Login sucessfully"
            reg=register_form.objects.filter(Email=Email)
            
            #request.session['email'] = Email
            return render(request,'index.html',{'meg':meg})
        else:
            print("password is not correct")
            meg="password is not correct..."
            return render(request,'Run_Here.html',{'meg':meg})   
    else:
        print('Email is not there...')
        meg="Email is not there..."
        return render(request,'Run_Here.html',{'meg':meg})
 
def areas(request):
    Email= request.session['email']
    reg=register_form.objects.get(Email=Email)
    fn=reg.Name
    cursor = conn.cursor()
    cursor.execute("SELECT Email FROM crime_area ")
    myresult = cursor.fetchall() 
    if myresult!=[]:
        land=area.objects.filter(Email=Email)
        if area.objects.filter(Email=Email).exists():
            update="You Already Register Area" 
            regss="update your address"  
            return render(request,"areareg.html",{'fn':fn,'update':update,'land':land,'regss':regss})
        else:
            regs="Register Your Area"
            return render(request,"areareg.html",{'fn':fn,'regs':regs})
    else:
        regs="Register Your Area"
        return render(request,"areareg.html",{'fn':fn,'regs':regs})
    return render(request,"areareg.html",{'fn':fn})


def register(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Phone = request.POST['Phone']

        if register_form.objects.filter(Email=Email).exists():
            print('Email id is taken')
            meg="Email id is  already taken"
            return render(request,'Run_Here.html',{'meg':meg})
        elif register_form.objects.filter(Name=Name).exists():
            print('Username is  already taken')
            meg="Username is taken"
            return render(request,'Run_Here.html',{'meg':meg})
        else:
            reg = register_form(Name=Name,Email=Email,Password=Password,Phone=Phone)
            
            reg.save();
            print("user is created")
            meg="user is created"
            return render(request,"Run_Here.html",{'meg':meg})
        return render(request,'Run_Here.html')

def publiccomp(request):
    if request.method == 'POST':
        location = request.POST['location']
        area = request.POST['area']
        detail = request.POST['detail']
        ts = time.time()   
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        print(timestamp)
        print(date)
        reg = complaint(location=location,area=area,detail=detail,date=date,time_h_m_s=timestamp)
        if complaint.objects.filter(detail=detail).exists():
            msg="this sentence already stored so please paraphase your sentence"
        else:
            msg="Registered your compliant"
            reg.save();
    return render(request,"publiccomplaint.html",{'msg':msg})

def areareg(request):
    if request.method == 'POST':
        doorno = request.POST['doorno']
        stname = request.POST['stname']
        villcit = request.POST['villcit']
        district = request.POST['district']
        state = request.POST['state']
        pincode = request.POST['pincode']
        contactnumber = request.POST['contactnumber']
        Email= request.session['email']
        reg=register_form.objects.get(Email=Email)
        fn=reg.Name
        pid=reg.id
        update="You Already Register Area" 
        cursor = conn.cursor()
        cursor.execute("SELECT Email FROM crime_area")
        myresult = cursor.fetchall()
        
        land = area(id=pid,stname=stname,Email=Email,doorno=doorno,villcit=villcit,district=district,state=state,pincode=pincode,contactnumber=contactnumber)  
        if myresult!=[]:
            if area.objects.filter(Email=Email).exists():
                landy=area.objects.filter(Email=Email)
                landy.delete();
                landy=area.objects.filter(Email=Email)
                land.save();
                meg="updated sucessfully"
                return render(request,"areareg.html",{'fn':fn,'update':update,'meg':meg,'land':landy})
            else:
                meg="Register sucessfully"
                land.save();
                return render(request,"index.html",{'fn':fn,'update':update,'meg':meg})
        else:
            meg="Register sucessfully"
            land.save();
            return render(request,"index.html",{'fn':fn,'update':update,'meg':meg})

def ccomplaint(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    carea = request.POST.get('carea')
    wip = request.POST.get('wip')
    image = request.FILES.get('image')
    detail = request.POST.get('detail')
    Email="test@gmail.com"
    #regg=register_form.objects.get(Email=Email)
    fn="test@gmail.com"
    cname=firstname+" "+lastname
    if complaint_details.objects.filter(cname=cname).exists():
        cc=complaint_details.objects.get(cname=cname)
        pid=cc.id
        reg = complaint_details(id=pid,cname=cname,firstname=firstname,lastname=lastname,Email=Email,carea=carea,wip=wip,detail=detail,image=image)
    else:
        reg = complaint_details(cname=cname,firstname=firstname,lastname=lastname,Email=Email,carea=carea,wip=wip,detail=detail,image=image)
    reg.save();
    meg="complaint added "
    return render(request,'index.html',{'meg':meg,'fn':fn})

def addcrime(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    carea = request.POST.get('carea')
    ctype = request.POST.get('ctype')
    image = request.FILES.get('image')
    bnname = request.FILES.get('uid')
    meg="complaint added "
    bn=request.session['bnname']
    try:
        bnname=request.session['bnname']
        print(bnname)
        reg=branches.objects.get(bnname=bnname)
        pid=reg.id
        fn=reg.firstname
    except:
        pass
    
    reg = addcriminalls(firstname=firstname,lastname=lastname,carea=carea,ctype=ctype,image=image,bnname=bnname)
    reg.save();
    # else:
    #     reg = addcriminalls(firstname=firstname,lastname=lastname,carea=carea,ctype=ctype,image=image,bnname=bnname)
    #     reg.save();
    return render(request,"addcriminals.html",{'bn':bn,'meg':meg})

def Missing_details(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    perno = request.POST.get('perno')
    missedarea = request.POST.get('missedarea')
    image = request.FILES.get('image')
    my_content = request.POST.get('my_content')
    Email= "keralapolice@gmail.com"
    #reg=register_form.objects.get(Email=Email)
    pid=random.randint(10,100)
    fn="user"
    status="ongoing"
    reg = Missing(id=pid,status=status,firstname=firstname,lastname=lastname,Email=Email,perno=perno,missedarea=missedarea,my_content=my_content,image=image)
    reg.save();
    meg="Missing complaint added "
    return render(request,'index.html',{'meg':meg,'fn':fn})

def policehome(request):
    comp=Missing.objects.all()
    #bnname=request.session['bnname']
    return render(request,"policehome.html",{'comp':comp})


def add_complaint(request):
    
    if request.method=="POST":
        
        booking_form=ComplaintForm(request.POST)
        if booking_form.is_valid():
            #booking_form.Email=request.session['email']
            booking_form.save()
            return render(request,'complaint_form.html')
        else:
            return HttpResponse("Invalid Form")
    booking_form=ComplaintForm()
    return render(request,'complaint_form.html',{'form':booking_form})








def AddMissing_public(request):
    
    if request.method=="POST":
        
        booking_form=AddMissing_public(request.POST)
        if booking_form.is_valid():
            #booking_form.Email=request.session['email']
            booking_form.save()
            return render(request,'AddMissing_public.html')
        else:
            return HttpResponse("Invalid Form")
    booking_form=ComplaintForm()
    return render(request,'AddMissing_public.html',{'form':booking_form})




def Addcriminal_public(request):
    
    if request.method=="POST":
        
        booking_form=Addcriminal_public(request.POST)
        if booking_form.is_valid():
            #booking_form.Email=request.session['email']
            booking_form.save()
            return render(request,'Addcriminal_public.html')
        else:
            return HttpResponse("Invalid Form")
    booking_form=ComplaintForm()
    return render(request,'Addcriminal_public.html',{'form':booking_form})











def view_my_complaints(request):
    complaints=complaint.objects.all()
    print(complaints)
    return render(request,'view_compliants.html',{'complaints':complaints})


def view_all_complaint(request):
    complaints=complaint.objects.all()
    print(complaints)
    return render(request,'view_all_complaint.html',{'complaints':complaints})



def complaint_reply(request,id):
    booking=complaint.objects.get(id=id)
    print(booking)
    update_booking_form=ComplaintReply(instance=booking)
    if request.method=="POST":
        update_booking_form=ComplaintReply(request.POST,request.FILES,instance=booking)
        update_booking_form.save()
        return redirect('crime:view_all_complaint')
    return render(request,'complaint_form.html',{'form':update_booking_form})





def edit_complaint(request,id):
    booking=complaint.objects.get(id=id)
    print(booking)
    update_booking_form=ComplaintForm(instance=booking)
    if request.method=="POST":
        update_booking_form=ComplaintForm(request.POST,request.FILES,instance=booking)
        update_booking_form.save()
        return redirect('crime:view_my_complaints')
    return render(request,'complaint_form.html',{'form':update_booking_form})



def add_feedback(request):
    
    if request.method=="POST":
        
        booking_form=FeedbackForm(request.POST)
        if booking_form.is_valid():
            
            booking_form.save()
            return render(request,'feedback_form.html')
        else:
            return HttpResponse("Invalid Form")
    booking_form=FeedbackForm()
    return render(request,'feedback_form.html',{'form':booking_form})




def view_feedback(request):
    complaints=Feedback.objects.all()
    print(complaints)
    return render(request,'view_all_feedback.html',{'complaints':complaints})




def add_news(request):
    
    if request.method=="POST":
        
        booking_form=NewsForm(request.POST)
        if booking_form.is_valid():
            
            booking_form.save()
            return render(request,'news_form.html')
        else:
            return HttpResponse("Invalid Form")
    booking_form=NewsForm()
    return render(request,'news_form.html',{'form':booking_form})


def view_news(request):
    complaints=News.objects.all()
    print(complaints)
    return render(request,'view_all_news.html',{'complaints':complaints})
def view_news2(request):
    complaints=News.objects.all()
    print(complaints)
    return render(request,'view_all_news2.html',{'complaints':complaints})
def content(request):
    complaints=News.objects.all()
    print(complaints)
    return render(request,'view_all_news_content.html',{'complaints':complaints})



def add_fir(request,id):
    criminal=addcriminalls.objects.get(id=id)
    if request.method=="POST":
        
        booking_form=FIRForm(request.POST)
        if booking_form.is_valid():
            bk=FIR(station=booking_form.cleaned_data['station'],criminal=criminal)
            bk.save()
            return render(request,'fir_form.html')
        else:
            return HttpResponse("Invalid Form")
    booking_form=FIRForm()
    return render(request,'fir_form.html',{'form':booking_form})



def view_fir(request):
    fir=FIR.objects.all()
    return render(request,'view_fir.html',{'fir':fir})
