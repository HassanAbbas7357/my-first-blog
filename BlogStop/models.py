from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_pic = models.ImageField(upload_to='profile_pic')
    def __str__(self):
        return str(self.user)

class Category(models.Model):
    #about = models.TextField(default="Hello world")
    name = models.CharField(max_length=20,verbose_name='Categories')
    slug = models.SlugField(unique=True)
    objects = models.Manager()
    def __str__(self):
        return self.name
    def get_cat_url(self):
        return f"/blog/{self.slug}/cat"

class Post(models.Model):
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    slug = models.SlugField(unique=True)
    title = models.CharField(unique=True,max_length=200)
    content_1 = models.TextField(unique=True)
    post_image_url = models.URLField(null=True,max_length=400)
    post_image_caption = models.CharField(default="Every thing we do" ,max_length=250)
    content_2 = models.TextField(default='lorem lorem lorem ')
    post_published_date = models.DateTimeField(auto_now=False)
    
    objects = models.Manager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    def get_cat_url(self):
        return f"/blog/{self.slug}/cat"
    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    comment_text = models.TextField()
    comment_published_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    objects = models.Manager()
    def __str__(self):
        return self.name
    
class Manage_Blog_Images(models.Model):
    home_background_image = models.ImageField(upload_to='home_background_image')
    detail_background_image = models.ImageField(upload_to='detail_background_image')
    book_background_image = models.ImageField(upload_to='book_background_image')
    book1_image = models.ImageField(upload_to='suggested_books')
    book2_image = models.ImageField(upload_to='suggested_books')
    book3_image = models.ImageField(upload_to='suggested_books')
    book4_image = models.ImageField(upload_to='suggested_books')
    objects = models.Manager()
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    objects = models.Manager()
    def __str__(self):
        return self.name

class About(models.Model):
    about = models.TextField(default="Hello world")    
