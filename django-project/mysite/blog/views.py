from datetime import date
from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        'slug': 'first-post',
        'image': 'https://picsum.photos/200/251',
        'author': 'CoreyMS',
        'date': date(2023, 8, 27),
        'title': 'My First Blog Post',
        'excerpt': 'This is my first blog post with more content inside',
        'content': "Lorem ipsum dolor sit amet consectetur adipisicing elit.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum"
     },{
        'slug': 'second-post',
        'image': 'https://picsum.photos/200/249',
        'author': 'CoreyMS',
        'date': date(2023, 8, 28),
        'title': 'My second Blog Post',
        'excerpt': 'This is my first blog post with more content inside',
        'content': "Lorem ipsum dolor sit amet consectetur adipisicing elit.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum"
     },{
        'slug': 'third-post',
        'image': 'https://picsum.photos/200/255',
        'author': 'CoreyMS',
        'date': date(2023, 8, 29),
        'title': 'My third Blog Post',
        'excerpt': 'This is my third blog post with more content inside',
        'content': "Lorem ipsum dolor sit amet consectetur adipisicing elit.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum"
     }
]

def get_date(post):
    return post['date']

def starting_page(request): 
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts,
    })
   

def post_detail(request, slug):
    next_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': next_post
    })        
   