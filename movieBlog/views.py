from django.shortcuts import render, redirect, get_object_or_404  #404는 서버가 요청한 페이지를 찾을 수 없다.
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm

def homeHtml(request):
    blogObject = Blog.objects.all()   
    # blogObject = Blog.objects.order_by("-pub_date") # 최신글 순서대로 저장

    paginator = Paginator(blogObject, 3) # 넣어야 하는 페이지 개수
    page = request.GET.get('page')  # GET 정보가 오지 않아도 넘어감. 페이지의 정보를 받음.
    blogObject = paginator.get_page(page)
    return render(request, 'home.html', {'blogObject':blogObject})

def detailHtml(request, id):  # Read
    blogModel = get_object_or_404(Blog, pk = id)  # pk = Primary Key (데이터베이스의 식별자), Table의 row 하나하나를 구별하는 ID값
    return render(request, 'detail.html', {'blogModel':blogModel})

def new(request):  #new.html을 보여줌.
    if request.method == 'POST':
        post_form = BlogForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)  # 임시저장
            new_post.save()
            return redirect('homeHtml')
    else:
        post_form = BlogForm()
        return render(request, 'new.html', {'post_form':post_form})

def edit(request, id):  # edit.html을 보여줌. 
    edit_post = get_object_or_404(Blog, pk=id)
    if request.method == 'GET':
        post_form = BlogForm(instance = edit_post)
        return render(request, 'edit.html', {'post_form':post_form})
    else:
        post_form = BlogForm(request.POST, request.FILES, instance = edit_post)
        if post_form.is_valid():
            edit_post = post_form.save(commit=False)  # 임시저장
            edit_post.save()
            return redirect('detailHtml', edit_post.id)      

def deletePost(request, id):    # Delete
    delete_post = Blog.objects.get(id=id)
    delete_post.delete()
    return redirect('homeHtml') 