from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import UserForm, Addbook, signUp, editProfile
from user.models import User, Book, Borrowing
from django.contrib import messages
from datetime import datetime, timedelta

books = Book.objects.all()




def loginform(request):
    form = UserForm()
    formSignUP = signUp()
    if request.method == 'GET':
        context = {'form': form, 'formSignUP': formSignUP}
        return render(request, 'user/loginForm.html', context)
    if 'signup' in request.POST:
        formSignUP = signUp(request.POST)
        if formSignUP.is_valid():
            formSignUP.save()
            match = User.objects.get(email=request.POST['email'])
            request.session['user'] = match.id
            return redirect('home')

    elif 'signin' in request.POST:
        try:
            match = User.objects.get(email=request.POST['email'])
            if match.email == request.POST['email']:
                if request.POST['password'] == match.password and match.role == 'user':
                    request.session['user'] = match.id
                    return redirect('home')
                elif request.POST['password'] == match.password and match.role == 'admin':
                    request.session['user'] = match.id
                    return redirect('admin')
                else:
                    form = UserForm(request.POST)
                    context = {'form': form}
                    messages.info(request, 'invalid user name or password')
                    return render(request, 'user/loginForm.html', context)
        except:
            form = UserForm(request.POST)
            context = {'form': form}
            messages.info(request, 'This is account not found')
            return render(request, 'user/loginForm.html', context)


def home(request):
    context = {'books': books}
    return render(request, 'user/home.html', context)


def details(request, id):
    date = datetime.now() + timedelta(days=5)
    print(date)
    b = Book.objects.get(pk=id)
    context = {'book': b}
    return render(request, 'user/details.html', context)


def borrow(request, id):
    book = Book.objects.get(pk=id)

    try:
        bor = Borrowing.objects.get(book=id)
        isBorrow = 1
        context = {'bor': bor, 'book': book, 'isBorrow': isBorrow}
        return render(request, 'user/details.html', context)
    except:
        date = datetime.now() + timedelta(days=5)
        borrowed = Borrowing.objects.create(user_id=request.session['user'], book_id=id, st_borrow=datetime.now(),
                                            return_borrow=date)
        book.avilable = 'NO'
        book.save()
        borrowed.save()
        bor = Borrowing.objects.get(book=id)
        isBorrow = 0
        context = {'bor': bor, 'isBorrow': isBorrow, 'book': book}
        return render(request, 'user/details.html', context)


def returnBook(request, id):
    book = Book.objects.get(pk=id)
    book.avilable = 'YES'
    book.save()
    books = Borrowing.objects.filter(user_id=request.session['user'])
    context = {'books': books}
    Borrowing.objects.get(book=id).delete()
    return render(request, 'user/getBorrowedBook.html', context)


def getBorrowedBook(request):
    books = Borrowing.objects.filter(user_id=request.session['user'])
    context = {'books': books}
    return render(request, 'user/getBorrowedBook.html', context)


def updateUserProfile(request):
    user = User.objects.get(pk=request.session['user'])
    form = editProfile(instance=user)
    if request.method == 'POST':
        form = editProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'user/userProfile.html', context)


def updateAdminProfile(request):
    user = User.objects.get(pk=request.session['user'])
    form = editProfile(instance=user)
    if request.method == 'POST':
        form = editProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('adminuser')
    context = {'form': form}
    return render(request, 'user/adminProfile.html', context)


def admin(request):
    books = Book.objects.filter(avilable='YES')
    bor = Borrowing.objects.all()
    context = {'books': books, 'bor': bor}
    return render(request, 'user/admin.html', context)


def adminuser(request):
    users = User.objects.all()
    context = {'users': users, 'idadmin': request.session['user']}
    return render(request, 'user/adminuser.html', context)


def viewborrow(request):
    bor = Borrowing.objects.all()
    context = {'bor': bor}
    return render(request, 'user/viewBorrowed.html', context)


def addbook(request):
    form = Addbook()
    if request.method == 'POST':
        form = Addbook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'user/addbook.html', context)


def deletebook(request, id):
    Book.objects.get(pk=id).delete()
    return redirect('admin')


def updatebook(request, id):
    book = Book.objects.get(pk=id)
    form = Addbook(instance=book)
    if request.method == 'POST':
        form = Addbook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('admin')
    context = {'form': form}
    return render(request, 'user/updatebook.html', context)


def searchuser(request):
    if request.method == 'POST':
        idstring = request.POST['search']
        id = int(idstring)
        try:
            user = User.objects.get(pk=id)
            context = {'user': user}
            return render(request, 'user/findOneUser.html', context)
        except:
            user = ''
            context = {'user': user}
            messages.info(request, 'This is ID not found')
            return render(request, 'user/findOneUser.html', context)
