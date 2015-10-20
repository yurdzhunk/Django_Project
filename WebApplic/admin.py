from django.contrib import admin
from WebApplic.models import Post, Comment, Title

# Register your models here.
class PostInline(admin.StackedInline):
    model = Comment
    extra = 2

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'date']
    inlines = [PostInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Title)


