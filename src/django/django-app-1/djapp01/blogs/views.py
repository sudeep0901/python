from django.shortcuts import render
from django.http import HttpResponse, Http404
from blogs.models import Header, Details
# Create your views here.

all_blogs = Header.objects.all()


def index(request):
    return render(request, "blogs/home.html",
                  {'nblog_header': Header.objects.count(),
                   'blog_header': all_blogs})
    # return HttpResponse("List of blogs page")


def detail(request, blog_id):
    try:
        blog_details = Details.objects.filter(
            blog_id=blog_id).order_by('line_no')

    except Details.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, "blogs/details.html",
                  {'nblog_detail': blog_details.count(),
                   'blog_details': blog_details})
