from django.shortcuts import render,redirect
from django.http import HttpResponse 
from.models import *
from django.contrib.auth import logout
import datetime
import re
from datetime import timedelta

# Create your views here.
def index(request):

    return render(request,'index.html')


def seller_log(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        a=model_seller.objects.all()
        for i in a:
            if(i.email==email and i.password==password):
                request.session['id']=i.id #global

                return redirect(seller_profile)
        else:
                return HttpResponse("faild....")
    return render(request,'seller_login.html')

def seller_reg(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        place=request.POST.get('place')
        age=request.POST.get('age')
        brand=request.POST.get('brand')
        product=request.POST.get('product')
        phonenumber=request.POST.get('phonenumber')
        photo=request.FILES.get('photo')
        email=request.POST.get('email')
        password=request.POST.get('password')
       
        a=model_seller(fullname=fullname,place=place,age=age,brand=brand,product=product,phonenumber=phonenumber,photo=photo,email=email,password=password)
        a.save()
        return redirect(seller_log)

    return render(request,"seller_reg.html")


def addpro(request):
     if request.method=='POST':
          name=request.POST.get('name')
          p_type=request.POST.get('p_type')
          size=request.POST.get('size')
          brand=request.POST.get('brand')
          price=request.POST.get('price')
          quality=request.POST.get('quality')
          photo=request.FILES.get('photo')
          color=request.POST.get('color')
          a=proadd(name=name,p_type=p_type,size=size,brand=brand,price=price,quality=quality,photo=photo,color=color)
          a.save()
          return redirect(prodview)
     return render(request,"product.html")

     

def seller_profile(request):
     id1=request.session['id']
     a=model_seller.objects.get(id=id1)
     img=str(a.photo).split('/')[-1]
     print(img)
     return render(request,'profile.html',{'data':a,'img':img})

def seller_edit(request,id):
     a=model_seller.objects.get(id=id)
     images=str(a.photo).split('/')[-1]
     if request.method=='POST':
        a.fullname=request.POST.get('fullname')
        a.place=request.POST.get('place')
        a.age=request.POST.get('age')
        a.brand=request.POST.get('brand')
        a.product=request.POST.get('product')
        a.phonenumber=request.POST.get('phonenumber')
        if request.FILES.get('photo')==None:
             a.save()
        else:
            a.photo=request.FILES.get('photo')
            a.save()
        a.email=request.POST.get('email')
        a.save()
        return redirect(seller_profile)
     return render(request,'edit_profile.html',{'data':a})


def prodview(request):
    id1=[]
    pname=[]
    pbrand=[]
    pprice=[]
    photo=[]
    pptype=[]
    psize=[]
    pquality=[]
    pcolor=[]
    a = proadd.objects.all()
    for i in a:
        id=i.id
        id1.append(id)
        p_image=str(i.photo).split('/')[-1]
        photo.append(p_image)
        p_brand=i.brand
        pbrand.append(p_brand)
        ppname=i.name
        pname.append(ppname)
        p_price=i.price
        pprice.append(p_price)
        ptype=i.p_type
        pptype.append(ptype)
    mylist=zip(pname,pbrand,pprice,photo,pptype,id1)

    return render(request,'card_view.html',{'data':mylist})



def byerreg(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        # place=request.POST.get('place')
        age=request.POST.get('age')
        # brand=request.POST.get('brand')
        # product=request.POST.get('product')
        phonenumber=request.POST.get('phonenumber')
        photo=request.FILES.get('photo')
        email=request.POST.get('email')
        password=request.POST.get('password')
       
        a=model_seller(fullname=fullname,age=age,phonenumber=phonenumber,photo=photo,email=email,password=password)
        a.save()
        return redirect(byerlog)

    return render(request,"byer_reg.html")



def byerlog(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        a=model_seller.objects.all()
        for i in a:
            if(i.email==email and i.password==password):
                request.session['u_id']=i.id #global
                request.session['fullname']=i.fullname

                return redirect(buyer_index)
        else:
                return HttpResponse("faild....")
    return render(request,'byer_log.html')



def byer_profile(request):
     id1=request.session['u_id']
     a=model_seller.objects.get(id=id1)
     img=str(a.photo).split('/')[-1]
     print(img)
     return render(request,'byer_profile.html',{'data':a,'img':img})


def byer_view(request,item):
    pname=[]
    pbrand=[]
    pprice=[]
    photo=[]
    pptype=[]
    id1=[]
    a = proadd.objects.all()
    for i in a:
        id=i.id
        id1.append(id)
        p_image=str(i.photo).split('/')[-1]
        photo.append(p_image)
        p_brand=i.brand
        pbrand.append(p_brand)
        ppname=i.name
        pname.append(ppname)
        p_price=i.price
        pprice.append(p_price)
        ptype=i.p_type
        pptype.append(ptype)
    mylist=zip(pname,pbrand,pprice,photo,pptype,id1)

    return render(request,'byer_view.html',{'data':mylist,'item':item})





def wishlist(request,id):
    a=proadd.objects.get(id=id) #(shoe...)
    id1=request.session['u_id']
    c=wishmodel.objects.all()
    for i in c:
        if id == i.prod_id and id1 == i.userid:

            return HttpResponse('Item already exist')
    else:
            b=wishmodel(prod_id=a.id,userid=id1,pname=a.name,pbrand=a.brand,price=a.price,photo=a.photo)
            b.save()
            return HttpResponse("item added successfully.....")







# def prod_wishlist(request,id):
#     a = wishmodel.objects.get(id=id)
#     id1 = request.session['id']
#     c = wishlist.objects.all()
#     for i in c:
#         if id == i.prod_id:
#             return HttpResponse('Item already exist')
#     else:
#         b = wishlist(prod_id=a.id,user_id = id1,med_name1 = a.med_name , man_name1 = a.man_name, dosage1 = a.dosage,type1=a.type,qty1=a.qty,price1=a.price,mtf1=a.mtf,med_pic1=a.med_pic)
#         b.save()
#         return HttpResponse("item added succesfully")

# def wishlist_view(request,u_id):
#     # id1 = request.session['id']
#     a = wishlist.objects.all()
#     # img = str(a.med_pic).split('/')[-1]
#     id = []
#     prod_id = []
#     user_id = []
#     man_name = []
#     med_name = []
#     dosage = []
#     type = []
#     price = []
#     qty = []
#     mtf = []
#     med_pic = []
#     for i in a:
#         userid1 = i.user_id
#         user_id.append(userid1)
#         prodid1 = i.prod_id
#         prod_id.append(prodid1)
#         id1 = i.id
#         id.append(id1)

#         man_name1 = i.man_name1
#         man_name.append(man_name1)
#         med_name1 = i.med_name1
#         med_name.append(med_name1)
#         dosage1 = i.dosage1
#         dosage.append(dosage1)
#         type1 = i.type1
#         type.append(type1)
#         price1 = i.price1
#         price.append(price1)
#         qty1 = i.qty1
#         qty.append(qty1)
#         mtf1 = i.mtf1
#         mtf.append(mtf1)
#         med_pic1 = str(i.med_pic1).split('/')[-1]
#         med_pic.append(med_pic1)
#     mylist=zip(user_id,prod_id,id,man_name,med_name,dosage,type,price,mtf,med_pic,qty)
#     return render(request,'wishlist_view.html',{'data':mylist,'id':u_id})


def wishlist_view(request):
    id3=request.session['u_id']
    a = wishmodel.objects.all()
    id1=[]
    user_id=[]
    prodid1=[]
    pname=[]
    pbrand=[]
    pprice=[]
    photo=[]
    
    for i in a:
        userid1 = i.userid
        user_id.append(userid1)
        prod_id1 = i.prod_id
        prodid1.append(prod_id1)

        0
        ids = i.id
        id1.append(ids)


        p_image=str(i.photo).split('/')[-1]
        photo.append(p_image)
        p_brand=i.pbrand
        pbrand.append(p_brand)
        ppname=i.pname
        pname.append(ppname)
        p_price=i.price
        pprice.append(p_price)
        # ptype=i.p_type
        # pptype.append(ptype)
    mylist=zip(id1,prodid1,user_id,pname,pbrand,pprice,photo)

    return render(request,'wishlist_view.html',{'data':mylist,'id':id3})


def delete_wish(request,id):
    a = wishmodel.objects.get(id=id)
    id1 = request.session['u_id']
    a.delete()
    return redirect("http://127.0.0.1:8000/ecommerce_app/wishview/")

def cart(request,id):
    a=proadd.objects.get(id=id) #(shoe...)
    id1=request.session['u_id']
    c=cartmodel.objects.all()
    for i in c:
        if id == i.prod_id and id1 == i.userid:
            i.qty +=1
            i.price=a.price * i.qty
            i.save()
            return HttpResponse('product added')
    else:
            count=1
            b=cartmodel(prod_id=a.id,userid=id1,pname=a.name,pbrand=a.brand,price=a.price,photo=a.photo,qty=count)
            b.save()
            return HttpResponse("item added successfully.....")






def cart_view(request):
    id3=request.session['u_id']
    a = cartmodel.objects.all()
    id1=[]
    user_id=[]
    prodid1=[]
    pname=[]
    pbrand=[]
    pprice=[]
    photo=[]
    qty=[]
    
    for i in a:
        userid1 = i.userid
        user_id.append(userid1)
        prod_id1 = i.prod_id
        prodid1.append(prod_id1)
        ids = i.id
        id1.append(ids)


        p_image=str(i.photo).split('/')[-1]
        photo.append(p_image)
        p_brand=i.pbrand
        pbrand.append(p_brand)
        ppname=i.pname
        pname.append(ppname)
        p_price=i.price
        pprice.append(p_price)
        qty1 = i.qty
        qty.append(qty1)

    tp1=[]
    tp2=[]
    d=cartmodel.objects.filter(userid=id3)
    for i in d:
         tp1.append(i.price)
    for i in tp1:
         tp2.append(int(i))

    total_price=sum(tp2)
    request.session['total_price']=total_price
    mylist=zip(id1,prodid1,user_id,pname,pbrand,pprice,photo,qty)
    

    return render(request,'cart.html',{'data':mylist,'id':id3,'price':total_price})







def delete_cart(request,id):
    a = cartmodel.objects.get(id=id)
    id1 = request.session['u_id']
    a.delete()
    return redirect("http://127.0.0.1:8000/ecommerce_app/cartview/")


def cartinc(request,id):
     a=cartmodel.objects.get(id=id)
     b=proadd.objects.get(id=a.prod_id)
     a.qty +=1
     a.price=b.price * a.qty
     a.save()
     return redirect(cart_view)


def cartdec(request,id):
     a=cartmodel.objects.get(id=id)
     b=proadd.objects.get(id=a.prod_id)
     a.qty -=1
     a.price=b.price * a.qty
     a.save()
     return redirect(cart_view)






def address(request):
    try:
          id2=request.session['u_id']
          b=address_buyer.objects.get(userid=id2)
          if b.u_address:
               return redirect(edit_buyer_address)
    except:


        if request.method=='POST':
                
                full_name=request.POST.get('full_name')
                phone=request.POST.get('phone')
                email=request.POST.get('email')
                u_address=request.POST.get('u_address')
                state=request.POST.get('state')
                district=request.POST.get('district')
                city=request.POST.get('city')
                pin=request.POST.get('pin')
                a=address_buyer(userid=id2,full_name=full_name,phone=phone,email=email,u_address=u_address,state=state,district=district,city=city,pin=pin)
                a.save()
                return redirect(cart_view)
        return render(request,'buyer_address.html')
    

def edit_buyer_address(request):
     id1=request.session['u_id']
     a=address_buyer.objects.get(userid=id1)
     if request.method=='POST':
          a.full_name=request.POST.get('full_name')
          a.phone=request.POST.get('phone')
          a.email=request.POST.get('email')
          a.u_address=request.POST.get('u_address')
          a.state=request.POST.get('state')
          a.district=request.POST.get('district')
          a.city=request.POST.get('city')
          a.pin=request.POST.get('pin')
          a.save()
          return redirect(cart_view)
     return render(request,'edit_buyer_address.html',{'data':a})





def details_delivery(request):
    id1 = request.session['u_id']
    a = cartmodel.objects.all()
    b = address_buyer.objects.all()

    price = request.session['total_price']
    address1 =[]
    prod_str = ''
    prod_img = ''
    ord_date = datetime.date.today()
    est_date = ord_date+timedelta(days=7)


    for i in b:
        if i.userid == id1:
            address1.append(i.u_address)
            address1.append(i.state)
            address1.append(i.district)
            address1.append(i.city)
            address1.append(i.pin)
    print(address1)
    prod_strlist=[]
    for i in a:
         if i.userid == id1:
              prod_str= "photo:"+str(i.photo).split('/')[-1]+"|pname:"+str(i.pname)+"|brand:"+str(i.pbrand)+"|price:"+str(i.price)+"|quantity:"+str(i.qty)
              prod_strlist.append(prod_str)
    print(prod_strlist)
    c=final_deliver(user_id=id1,address=address1,order_date=ord_date,est_del_date=est_date,products=prod_strlist,amount=price)
    c.save()
    for i in address1:
         print(i)

    
    return redirect(delivary_display)


def delivary_display(request):
     id2=request.session['u_id']
     fullname=request.session['fullname']
     total_amount=request.session['total_price']

     photo=[]
     price=[]
     qty=[]
     brand=[]
     pname=[]
     a=cartmodel.objects.all()
     for i in a:
          if i.userid==id2:
               photo.append(str(i.photo).split('/')[-1])
               price.append(i.price)
               qty.append(i.qty)
               brand.append(i.pbrand)
               pname.append(i.pname)
     mylist=zip(photo,price,qty,brand,pname)
     return render(request,'details_view.html',{'data':mylist,'fname':fullname,'amount':total_amount})


              


                    
     


# def cart_view(request):
#     id2 = request.session['user_id']
#     print(id2)
#     a = cart.objects.all()
#     # img = str(a.med_pic).split('/')[-1]
#     id = []
#     prod_id = []

#     man_name = []
#     med_name = []
#     dosage = []
#     type = []
#     price = []
#     qty = []
#     mtf = []
#     med_pic = []
#     userid = []

#     for i in a:
#         userid.append(i.user_id)
#         prodid1 = i.prod_id
#         prod_id.append(prodid1)
#         id1 = i.id
#         id.append(id1)

#         man_name1 = i.man_name1
#         man_name.append(man_name1)
#         med_name1 = i.med_name1
#         med_name.append(med_name1)
#         dosage1 = i.dosage1
#         dosage.append(dosage1)
#         type1 = i.type1
#         type.append(type1)
#         price1 = i.price1
#         price.append(price1)
#         qty1 = i.qty1
#         qty.append(qty1)
#         mtf1 = i.mtf1
#         mtf.append(mtf1)
#         med_pic1 = str(i.med_pic1).split('/')[-1]
#         med_pic.append(med_pic1)
#     mylist = list(zip(userid, prod_id, id, man_name, med_name, dosage, type, price, mtf, med_pic, qty))
#     return render(request, 'cart.html',{'data': mylist,'id':id1})

def buyer_index(request):
     return render(request,'buyer_index.html')
