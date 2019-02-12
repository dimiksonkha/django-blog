from django.contrib import admin

from blog.models import Post, Comment,Reply, UserProfileInfo,Tag,Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfileInfo)
admin.site.register(Reply)
admin.site.register(Tag)
admin.site.register(Category)
