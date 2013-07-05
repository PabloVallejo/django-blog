# Admin
import models
from django.contrib import admin
from django.contrib.auth.models import User


# Category
class CategoryAdmin( admin.ModelAdmin ):
    prepopulated_fields = { 'slug': ( 'title', ) }


# Category inline
class CategoryToPostInline( admin.TabularInline ):
    model = models.CategoryToPost
    extra = 1


# Register Post model
class PostAdmin( admin.ModelAdmin ):
    prepopulated_fields = { 'slug': ( 'title', ) }
    exclude = ( 'author', )
    inlines = [ CategoryToPostInline ]

    # Save
    def save_model( self, request, obj, form, change ):
        obj.author = request.user
        obj.save()


# Register in admin interface
admin.site.register( models.Post, PostAdmin )
admin.site.register( models.Category, CategoryAdmin )