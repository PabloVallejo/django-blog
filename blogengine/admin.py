# Admin
import models
from django.contrib import admin


# Register Post model
class PostAdmin( admin.ModelAdmin ):
    prepopulated_fields = { 'slug': ( 'title', ) }
    exclude = ( 'author', )

    # Save
    def save_model( self, request, obj, form, change ):
        obj.author = request.user
        obj.save()

admin.site.register( models.Post, PostAdmin )