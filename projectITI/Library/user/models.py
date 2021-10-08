from django.db import models


class Book(models.Model):
    CATECORY = (
        ('c++', 'c++'),
        ('python', 'python'),
        ('Java', 'Java'),
        ('algorithm', 'algorithm')
    )
    AVILABLE =(
        ('YES' , 'YES'),
        ('NO' , 'NO')
    )
    name = models.CharField(max_length=20, null=True)
    author = models.CharField(max_length=20, null=True)
    img = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATECORY)
    des = models.CharField(max_length=200, null=True)
    avilable = models.CharField(max_length=20, choices= AVILABLE ,default='YES')

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=20, null=True,unique=True)
    email = models.EmailField(max_length=100, null=True,unique=True)
    password = models.CharField(max_length=20, null=True)
    confirm = models.CharField(max_length=20, null=True)
    ROLE = (
        ('user', 'user'),
        ('admin', 'admin')
    )
    role = models.CharField(max_length=20, default='user', choices=ROLE)
    books = models.ManyToManyField(Book, through='Borrowing')

    def __str__(self):
        return self.username


class Borrowing(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    st_borrow = models.DateField(null=True)
    return_borrow = models.DateField(null=True)
