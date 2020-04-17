from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 60)
    slug = models.SlugField(max_length=30, unique=True)
    cost = models.IntegerField()
    available = models.IntegerField()

    def __str__(self):
        return self.name

ORDERSTATUS = [
    (0,'Created'),
    (1,'Paid')
]

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    orderded = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=ORDERSTATUS,default=0)

    def __str__(self):
        all_books = self.books.all().values()
        return str(self.customer.username)+str([all_books[j]['slug'] for j in [i for i in range(len(all_books))]])