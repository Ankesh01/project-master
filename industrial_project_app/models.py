from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

from django.db.models.signals import post_save
from django.utils.text import slugify

def user_directory_path(instance, filename):
    # this file will be uploaded to MEDIA_ROOT /user(id)/filename
    return 'user_{0}/{1}'.format(instance.user.id,filename)






class State(models.Model):
    StateName = models.CharField(max_length=50,unique=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate= models.DateTimeField(auto_now_add=True)


class Courses(models.Model):
    CourseName = models.CharField(max_length=250,unique=True)
    UniqueId = models.CharField(max_length=50,unique=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate= models.DateTimeField(auto_now_add=True)



class Technical(models.Model):
    TechnicalName = models.CharField(max_length=250,unique=True)
    TechnicalUniqueId = models.CharField(max_length=250,unique=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate= models.DateTimeField(auto_now_add=True)



class NonTechnical(models.Model):
        NonTechnicalName = models.CharField(max_length=250,unique=True)
        NonTechnicalUniqueId = models.CharField(max_length=250,unique=True)
        CreatedDate = models.DateTimeField(auto_now_add=True)
        UpdateDate= models.DateTimeField(auto_now_add=True)



class City(models.Model):
    CityName = models.CharField(max_length=50,unique=True)
    CityState = models.ForeignKey(State,on_delete=models.CASCADE)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate= models.DateTimeField(auto_now_add=True)




class College(models.Model):
    CollegeName = models.CharField(max_length=250)
#    User = models.OneToOneField(User,on_delete=models.CASCADE)
    CollegeAddress = models.TextField(max_length=500)
    CollegeEmail = models.EmailField(max_length=250,unique=True)
    CollegePhoneNo = models.IntegerField(unique=True)
    State_Name = models.ForeignKey(State,related_name='College_state',on_delete=models.CASCADE)
    Courses_Provide = models.ManyToManyField(Courses)
    city_Name = models.ForeignKey(State,related_name='City',on_delete=models.CASCADE)
    Password = models.CharField(max_length = 20,)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate= models.DateTimeField(auto_now_add=True)




class School(models.Model):
    SchoolName = models.CharField(max_length=250)
#    User = models.OneToOneField(User,on_delete=models.CASCADE)
    SchoolAddress = models.TextField(max_length=500)
    SchoolEmail = models.EmailField(max_length=250,unique=True)
    SchoolPhoneNo = models.IntegerField(unique=True)
    State_Name = models.ForeignKey(State,related_name='School_State',on_delete=models.CASCADE)
    Courses_Provide = models.ManyToManyField(Courses)
    city_Name = models.ForeignKey(State,related_name='College_City',on_delete=models.CASCADE)
    Password = models.CharField(max_length = 20)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate= models.DateTimeField(auto_now_add=True)



class User_Table(models.Model):
    FirstName = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    UserName = models.OneToOneField(User,on_delete=models.CASCADE)
    College_info = models.ForeignKey(College,related_name='College_information',on_delete=models.CASCADE,blank=True)
    School_info = models.CharField(max_length=50 ,blank=True)
    Email = models.EmailField(unique=True)
#   Qualification_info = models.Fore
    PhoneNo = models.IntegerField(unique=True)
    TechnicalField = models.ForeignKey(Technical,None,blank=True)
    NonTechnicalField = models.ForeignKey(NonTechnical,None,blank=True)
    Age = models.IntegerField()
    State_Name = models.ForeignKey(State,related_name='User_stateName',on_delete=models.CASCADE)
    City_Name = models.ForeignKey(City,related_name='User_cityName',on_delete=models.CASCADE)
    #ClassStudy
    BirthDate = models.DateField()
    CreatedDate = models.DateField()
    UpdateDate = models.DateField()
    Job_Status = models.BooleanField(default=0)




class Content(models.Model):
    Image = models.ImageField(null=True)
    Text = models.TextField(null=True)
    CreatedDate = models.DateField()
    UpdateDate = models.DateField()



class post(models.Model):
    #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    #picture=models.ImageField(upload_to=user_directory_path,verbose_name='Picture',null=False)
#    tags=models.ManyToManyField(Tag,related_name='tags')
    User = models.ForeignKey(User_Table,null=True,blank=True,on_delete=models.CASCADE)
    Post_Title = models.CharField(max_length=50,default = User)
    Post_Content = models.ForeignKey(Content,null=True,on_delete=models.CASCADE)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateField(null=True)


class Like(models.Model):
    User = models.ForeignKey(User_Table,None,blank=True)
    Post=models.ForeignKey(post,None,blank=True)
    LikeCount = models.IntegerField(default=0)


class UnLike(models.Model):
    User = models.ForeignKey(User_Table,None,blank=True)
    Post=models.ForeignKey(post,None,blank=True)
    UnLikeCount = models.IntegerField(default=0)



class Comment(models.Model):
    Post_comment = models.TextField(max_length=250)
    User = models.ForeignKey(User_Table,None,blank=True)
    Post = models.ForeignKey(post,None,blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate= models.DateTimeField(auto_now_add=True)
#    flag = models.ChoiceField(racist,abusive)



class FriendRequest(models.Model):
    ToUser = models.ForeignKey(User_Table,related_name='friendrequests',on_delete=models.CASCADE)
    FromUser = models.ForeignKey(User_Table,related_name='Request_Sent',on_delete=models.CASCADE)
    Status = models.BooleanField(default=0)


class Followers_User(models.Model):
    User = models.OneToOneField(User_Table,related_name='Followers',on_delete=models.CASCADE)
    Followers = models.ManyToManyField(User_Table,blank=True)



class Followig_User(models.Model):
    User = models.OneToOneField(User_Table,related_name='Followings',on_delete=models.CASCADE)
    Following = models.ManyToManyField(User_Table,blank=True)
