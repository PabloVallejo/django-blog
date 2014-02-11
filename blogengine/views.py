# Blog engine views
from django.shortcuts import render_to_response
from blogengine.models import Post, Category
from django.core.paginator import Paginator, EmptyPage
from django.template import RequestContext
from django.contrib.syndication.views import Feed


# Gets the latest posts in the blog
def get_recent_posts( request ):

    # Get all blog posts
    posts = Post.objects.all()

    # Sort posts into chronological order
    sorted_posts = posts.order_by( '-pub_date' )

    # display all the posts
    return render_to_response( 'posts.html', { 'posts': sorted_posts } )


# Gets paginated posts
def get_posts( request, selected_page = 1 ):

    # Get all blog posts
    posts = Post.objects.all().order_by( '-pub_date' )

    # Add pagination
    pages = Paginator( posts, 5 )

    # Get the specified page
    try:
        returned_page = pages.page( selected_page )
    except Exception:
        returned_page = pages.page( pages.num_pages )

    # Display all the posts
    return render_to_response( 'posts.html', { 'posts': returned_page, 'page': returned_page } )


# Gets a single post
def get_post( request, post_slug ):

    # Get specified post
    post = Post.objects.filter( slug = post_slug )

    # Display specified post
    return render_to_response( 'single.html', { 'posts': post }, context_instance = RequestContext( request ) )


# Get a category
def get_category( request, category_slug, selected_page = 1 ):

    # Get specified category
    posts = Post.objects.all().order_by( '-pub_date' )
    category_posts = []

    for post in posts:
        if post.categories.filter( slug = category_slug ):
            category_posts.append( post )


    # Add pagination
    pages = Paginator( category_posts, 5 )

    # Get the category
    category = Category.objects.filter( slug = category_slug )[ 0 ]

    # Get the specified page
    try:
        returned_page = pages.page( selected_page )

    except EmptyPage:
        returned_page = pages.page( pages.num_pages )

    # Display all the posts
    return render_to_response( 'category.html', { 'posts': returned_page.object_list, 'page': returned_page, 'category': category })


# RSS Feed
class PostsFeed( Feed ):
    title = 'My Django Blog Posts'
    link = 'feeds/posts/'
    description = 'Posts from my Django blog'

    def items( self ):
        return Post.objects.order_by( '-pub_date' )[ :5 ]

    def item_title( seld, item ):
        return item.title

    def item_description( self, item ):
        return item.text
