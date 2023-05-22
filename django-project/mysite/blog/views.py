from django.shortcuts import render

# Create your views here.
posts = [
    {
        'slug': 'first-post',
        'image': 'https://picsum.photos/200/300',
        'author': 'CoreyMS',
        'date': 'August 27, 2018',
        'title': 'My First Blog Post',
        'excerpt': 'This is my first blog post with more content inside',
        'content': "Lorem ipsum dolor sit amet consectetur adipisicing elit.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum.Quisquam, voluptatum. Quisquam, voluptatum. Quisquam, voluptatum"
     }
]
def starting_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/all-posts.html')
   

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')        
   