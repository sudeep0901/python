from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Header, Details
# Create your views here.

all_blogs = Header.objects.all()


def index(request):
    return render(request, "blogs/home.html",
                  {'nblog_header': Header.objects.count(),
                   'blog_header': all_blogs})
    # return HttpResponse("List of blogs page")


def detail(request, blog_id):
    return HttpResponse("Youa re in blog details")
