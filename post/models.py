from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

from django.db.models.signals import post_save
from django.utils.text import slugify

def user_directory_path(instance, filename):
    # this file will be uploaded to MEDIA_ROOT /user(id)/filename
    return 'user_{0}/{1}'.format(instance.user.id,filename)


class Tag(models.Model):
    title = models.CharField(max_length=75,verbose_name='Tag')
    slug = models.SlugField(null=False,unique=True)

    class Meta:
        verbose_name_plural='Tags'

    def get_absolute_url(self):
        return reverse('tags',arg=[self.slug])

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(sellf.title)
        return super().save(*args,**kwargs)

class post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    picture=models.ImageField(upload_to=user_directory_path,verbose_name='Picture',null=False)
    caption = models.TextField(max_length=1500,verbose_name='Caption')
    posted = models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField(Tag,related_name='tags')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.IntegerField()

    def get_absolute_url(self):
        return reverse('postdetails',args=[str(self.id)])
