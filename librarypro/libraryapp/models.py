from django.db import models

# Create your models here.
class Details_of_book(models.Model):
    book_name=models.CharField(max_length=50)
    author_name=models.CharField(max_length=50)
    publisher_name=models.CharField(max_length=50)
    email_id=models.EmailField(max_length=100,unique=True)
    price=models.FloatField()

    def __str__(self):
        return self.book_name
        
class Login_page(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
