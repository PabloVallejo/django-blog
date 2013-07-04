
# Blog engine views
from django.shortcuts import render_to_response
from blogengine.models import Post
from django.core.paginator import Paginator

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
    return render_to_response( 'single.html', { 'posts': post } )