from django.shortcuts import render,reverse
from .models  import UploadForm,Upload,UploadFilter
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core import serializers
# Create your views here.
def home(request):
    upload=Upload.objects.all().order_by('-id')
    paginator = Paginator(upload, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params={'upload':page_obj}
    return render(request,'main/home.html',params)

@login_required(login_url='acc_login')
def create_upload(request):
    if request.method=='POST':
        upload=Upload(user=request.user)
        form=UploadForm(request.POST,instance=upload)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    else:
        form=UploadForm()
    return render(request,'main/upload/create_upload.html',{'form':form})

def search(request):
    upload=Upload.objects.all()
    filter=UploadFilter(request.GET,queryset=upload)
    return render(request,'main/search/search.html',{'filter':filter,'upload':filter.qs})

@login_required(login_url='acc_login')
def delete_upload(request,uid,vid):
    if request.user.id==uid:
        obj=request.user.upload.get(id=vid)
        obj.delete()
        print("working")
    return HttpResponseRedirect(reverse('acc_user_upload'))

@login_required(login_url='acc_login')
def like_upload(request,vid):
    print(request.user.username)
    upload=Upload.objects.get(id=vid)
    upload.like.add(request.user)
    upload.save()
    a={"count":upload.like.count()}
    return JsonResponse(a)

def trending(request):
    upload=Upload.objects.all().order_by("-id")
    paginator = Paginator(upload, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params={'upload':page_obj}
    return render(request,'main/trending/trending.html',params)


def aboutsite(request):
    return render(request,'aboutsite.html')

    