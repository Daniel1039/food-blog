from django.contrib import admin
from .models import Post,  Contact

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug', 'status', 'created_on')
    list_filter =('status',)
    search_fields=['title','content']
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_on')
    search_fields = ['name', 'email', 'message']   
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)