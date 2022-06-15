from django.contrib import admin
from .models import Details_of_book

# Register your models here.
admin.site.register(Details_of_book)
'''@admin.register(Details_of_book)
class AdminDetails_of_book(admin.ModelAdmin):
    list_display=['id','book_name','author_name','publisher_name','email_id','price']
'''
