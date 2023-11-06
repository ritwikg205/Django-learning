from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Ritwik Gupta',
        'title' : 'Blog Post 1',
        'content' : 'First Post',
        'date_posted' : '21-01-2005'
    },
    {
        'author' : 'Anand Garv',
        'title' : 'Blog Post 2',
        'content' : 'Second Post',
        'date_posted' : '10-10-2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
