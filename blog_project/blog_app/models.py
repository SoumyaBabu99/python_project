from django.db import models

#  create your model here.

# class tags(models.Model):
# #    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
#    nm=models.CharField(max_length=50,unique=True)
#    def __str__(self) :
#        return self.nm

# class taggs(models.Model):

#    nm=models.CharField(max_length=50,unique=True)
#    def __str__(self) :
#        return self.nm
class post_register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.IntegerField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.nm
    

# class add_post(models.Model):
# class add_new(models.Model):
#     userid=models.IntegerField()
#     title=models.CharField(max_length=50)
#     description=models.CharField(max_length=200)
#     tag=models.CharField(max_length=30)
#     date=models.DateTimeField()
#     def __str__(self):
#         return self.title

class my_blog(models.Model):
    userid=models.IntegerField()
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    tag=models.CharField(max_length=30)
    date=models.DateTimeField()
    def __str__(self):
        return self.title
    
class postpub(models.Model):
    puserid=models.IntegerField()
    ptitle=models.CharField(max_length=50)
    pdescription=models.CharField(max_length=200)
    ptag=models.CharField(max_length=30)
    pdate=models.DateTimeField()
    def __str__(self):
        return self.ptitle
