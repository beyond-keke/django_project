#coding:utf-8
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render,render_to_response,render_to_response,HttpResponse
from django.http import HttpResponse

# Create your views here.
#===============================================================================
# def hello(request):
#     return HttpResponse('Hello Django! current page is %s' % request.META['HTTP_USER_AGENT'])
#===============================================================================

def hello(request):
    return HttpResponse('Hello Django!')

def test1(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'test1.html', context)

def test2(request):
    context = {}
    return render(request, 'test2.html', context)

def b_strap(request):
    return HttpResponse(request, 'b_strap.html')

def url_view(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table border="1">%s</table>' % '\n'.join(html))


def request_values(request):
    values = request.META.items()
    html = []
    keys = ['HTTP_HOST', 'DJANGO_SETTINGS_MODULE', 'HTTP_USER_AGENT', 'PATH_INFO']
    for i in values:
        for k in keys:
            if k in i:
                k, v = i
                html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table border="1">%s</table>' % '\n'.join(html))

def images(request):
    image_data = open("/usr/local/webserver/nginx/conf/django_project/statics/images/logo.jpg", "rb").read()
    return HttpResponse(image_data, mimetypes="image/png")

def search(request):
    html = []
    error = False
    if 'username' in request.GET and 'email' in request.GET:
        username = request.GET['username']
        email    = request.GET['email']
        if not username or not email:
            error = True
        else:
            username_content = 'You Input username is <font color="red"><B>%s</B></font>.' % username
            email_content    = 'You Input email is <font color="blue"><B>%s</B></font>.' % email
            html.append('<tr><td>%s</td></tr>' % (username_content))
            html.append('<tr><td>%s</td></tr>' % (email_content))
            return HttpResponse('<table border="1">%s</table>' % '</br>'.join(html))
    return render_to_response('search.html', {'error': error})

def login(request):
    context = {}
    return render(request, 'login.html', context)

#===============================================================================
# def register(request):
#     curtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             username = userform.cleaned_data['username']
#             password = userform.cleaned_data['password']
#             User.objects.create(username=username,password=password)
#             User.save()
#             return HttpResponse('regist success!!!')
#         else:
#             userform = UserForm()
#         return render_to_response('regist.html',{'userform':userform})
#===============================================================================
