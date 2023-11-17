from django.db import models

# Create your models here.
class register_form(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)
    
class complaint(models.Model):
    Email = models.EmailField(null=True,blank=True)
    first_name=models.CharField(max_length=50,null=True,blank=True)
    last_name=models.CharField(max_length=50,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    location=models.CharField(max_length=50)
    area=models.CharField(max_length=200)
    detail=models.TextField(max_length=2000)
    reply=models.CharField(max_length=200,null=True,blank=True)
    date = models.CharField(max_length=15,null=True,blank=True)
    time_h_m_s = models.CharField(max_length=15,null=True,blank=True)

class area(models.Model):
    Email = models.EmailField()
    doorno=models.CharField(max_length=50)
    stname=models.CharField(max_length=200)
    villcit=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    contactnumber=models.CharField(max_length=50)

class complaint_details(models.Model):
    Email = models.EmailField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    carea = models.CharField(max_length=800)
    wip = models.CharField(max_length=500)
    detail = models.CharField(max_length=2000)
    reply=models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to="image")

class Missing(models.Model):
    Email = models.EmailField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    perno = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    missedarea = models.CharField(max_length=1000)
    my_content = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="image")

class addcriminalls(models.Model):
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    carea = models.CharField(max_length=800)
    ctype = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image")
    bnname=models.CharField(max_length=100)
    def __str__(self):
        return str(self.firstname) 

class branches(models.Model):
    bnname=models.CharField(max_length=100)
    bpass=models.CharField(max_length=100)
    barea = models.CharField(max_length=800)
    profile = models.ImageField(upload_to="image")
    nopolice = models.CharField(max_length=10)
    address = models.CharField(max_length=2000)

class chatregg(models.Model):
   date = models.CharField(max_length=15)
   time_h_m_s = models.CharField(max_length=15)
   dchatt = models.CharField(max_length=2000)
   fromm = models.CharField(max_length=20)
   too = models.CharField(max_length=20)

class fileupload(models.Model):
    bnname=models.CharField(max_length=100)
    crimename=models.CharField(max_length=100)
    crimearea=models.CharField(max_length=1000)
    value=models.CharField(max_length=10)
    files = models.FileField(upload_to="file")




class Feedback(models.Model):
    title=models.CharField(max_length=50)
    feedback=models.TextField()



class News(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()



class FIR(models.Model):
    station=models.CharField(max_length=50)
    criminal=models.ForeignKey(addcriminalls,on_delete=models.CASCADE,null=True,blank=True)








    