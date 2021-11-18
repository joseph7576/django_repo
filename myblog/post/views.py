from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

from .models import Post
from datetime import datetime
# models
from .models import  Post,Category

# نمایش تاریخ و ساعت امروز
def today_date(request):
    #request :  https://docs.djangoproject.com/en/3.2/ref/request-response/
    #view :  https://docs.djangoproject.com/en/3.2/topics/http/views/
    print(request.body)
    print(request.method)
    print(request.path_info)
    print(request.path)
    print(request.POST)
    print(request.GET)

    today = datetime.today()
    html = f'<p>today is : {today}</p>'
    return HttpResponse(html)


def my_view (request,coustom_id,name='mohammad'):

    print(coustom_id)
    print(request.path)
    print(request.GET)

    
    if (coustom_id==1):
        print('ok')
        return HttpResponse(f'my name is {name}')
    return HttpResponseNotFound('not found') #404


def my_view_2 (request,id):
    post = {
        'title':id,
        'body' : "this is first body ...",
        'today' : datetime.today()
    }

    return render(request,'first.html',post)


def detail_post (request,id):
    print('id',type('id'))
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist :
        # return HttpResponseNotFound(f'آیدی {id} موجود نیست ارباب')
        return render(request,'first.html',{'post':None})
    print(post)
    return render(request,'first.html',{'post':post})

# def detail_post(request)
#     #هدف اولیه : پستی با ایدی دو را نمایش دهیم
#     post = Post.objects.get(id=2)


def index(request):

    
    posts =Post.objects.all().order_by('-created_on')
    category = Category.objects.all()
    return render(request,
            'index.html',
            {"posts":posts,"category":category} )


def category(request) : 
    category = Category.objects.all()
    return render(request,'category.html',{'category':category})


def category_detail(request,cat_id):
    # category/id
    posts = Post.objects.filter(category__pk = cat_id)
    
    return render (request,'category_post.html',{'posts':posts})


def base_temp_view (request):
    return render (request,'base.html')