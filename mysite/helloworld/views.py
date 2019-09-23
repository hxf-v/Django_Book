from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# 测试第一个hello world能否正常显示
def index(request):
    return HttpResponse("hello world")

# 从数据库获取书本列表
def detail(request):
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'helloworld/detail.html', context)

# 增加书
def addBook(request):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

    from django.utils import timezone
    temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    temp_book.save()

    # 重定向
    return HttpResponseRedirect(reverse('helloworld:detail'))

# 删除书
def deleteBook(request, book_id):
    bookID = book_id
    Book.objects.filter(id=bookID).delete()
    return HttpResponseRedirect(reverse('helloworld:detail'))
