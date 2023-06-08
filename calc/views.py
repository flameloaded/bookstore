from django.shortcuts import render
from django.http import HttpResponse
from .models import Page

def index(request):
   # return HttpResponse('Hello World')
    return render(request, "base.html")

def calc_page(request):
    return render(request, "calc/base.html")  
# Create your views here.
def calc_pages(pagename):
    pagename = '/' + pagename
    pg = Page.object.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_upadted': pg.updated_date,
        
    }

    return render('calc/base.html', context)