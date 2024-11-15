from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from books.models import Book
# Create your views here.
def home(request):
    context={'name':'Arun','age':27}
    return render(request,'home.html',context)
@login_required
def add_books(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        pa=request.POST['pa']
        l=request.POST['l']

        c=request.FILES['i']
        f=request.FILES['f']

        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=c,pdf=f)
        b.save()
        return view_books(request)
    return render(request,'add.html')
@login_required()
def view_books(request):
    # k=con.execute('select * from Book')  reads all records from table Book and assigns it to k
    k=Book.objects.all()
    return render(request,'view.html',{'book':k})
@login_required()
def detail(request,p):
    k=Book.objects.get(id=p)
    return render(request,'detail.html',{'book':k})
@login_required()
def edit(request,m):
    k = Book.objects.get(id=m)
    if (request.method == "POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.pages=request.POST['pa']
        k.language=request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES['i']

        if(request.FILES.get('f')==None):
            k.save()
        else:
            k.pdf=request.FILES['f']

        k.save()

        return view_books(request)

    return render(request,'edit.html',{'book':k})

@login_required()
def delete(request,i):
    k=Book.objects.get(id=i)
    k.delete()
    return view_books(request)

from django.db.models import Q
def search(request):
    k=None
    if(request.method=="POST"):
        query=request.POST['q']
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request,'search.html',{'book':k})
