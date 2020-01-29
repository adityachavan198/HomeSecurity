from django.contrib import admin

# Register your models here.

from . import models
class ReviewAdmin(admin.TabularInline):
    model = models.Review
    extra = 0
class BookAdmin(admin.ModelAdmin):#used to display the title as well as other attributes of the book
    fields=['title','pages','price', 'publicationhouse']
    list_display=['title','price','pages', 'publicationhouse']
    search_fields=['title'] #to add search fields
    list_filter=['price','pages'] #to add filter functionality
    inlines = [ReviewAdmin]

class ReviewAdmini(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(models.Book,BookAdmin)#to register thr book model with admin interface and return the aclass name
admin.site.register(models.PublicationHouse)
admin.site.register(models.Review, ReviewAdmini)
admin.site.site_header = "Library Admin"
admin.site.site_title = "Aditya Chavan"
admin.site.index_title = "Aditya Chavan"
