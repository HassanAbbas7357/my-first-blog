from django.contrib import admin
from .models import user,Category,Post,Comment,Manage_Blog_Images,Contact,About
# Register your models here.
admin.site.register(user)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Manage_Blog_Images)
admin.site.register(Contact)
admin.site.register(About)
