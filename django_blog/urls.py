from django.conf.urls import patterns, include, url
from blogengine.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns( '',


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Home page
    url( r'^$', get_recent_posts ),

    # Paginated homepage
    url( r'^(?P<selected_page>\d+)/?$', get_posts ),

    # Single post by post slug
    url( r'^\d{4}/\d{1,2}/(?P<post_slug>[-a-zA-Z0-9]+)/?$', get_post ),

    # Categories
    url( r'^categories/(?P<category_slug>\w+)/?$', get_category ),
    url( r'^categories/(?P<category_slug>\w+)/(?P<selected_page>\d+)/?$', get_category ),

    # Comments
    url( r'^comments/', include( 'django.contrib.comments.urls' ) ),

    # Syndication
    url( r'^feed/posts/$', PostsFeed() ),

    # Flat page About
    url( r'', include( 'django.contrib.flatpages.urls' ) ),


)
