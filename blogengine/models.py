from django.db import models
from django.contrib.auth.models import User



# Category Model
class Category( models.Model ):
    title = models.CharField( max_length = 200 )
    slug = models.SlugField( max_length = 40, unique = True )
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__( self ):
        return self.title

    def get_absolute_url( self ):
        return '/categories/{}'.format( self.slug )


# Post model
class Post( models.Model ):
    title = models.CharField( max_length = 200 )
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField( max_length = 40, unique = True )
    author = models.ForeignKey( User )

    def __unicode__( self ):
        return self.title

    # Absolute URL
    def get_absolute_url( self ):
        return '/%s/%s/%s' % ( self.pub_date.year, self.pub_date.month, self.slug )


# Category To Post
class CategoryToPost( models.Model ):
    post = models.ForeignKey( Post )
    category = models.ForeignKey( Category )
