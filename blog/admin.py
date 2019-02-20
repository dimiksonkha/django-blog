from django.contrib import admin

from blog.models import Post,Tag,Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
