from django.db import models

class Book_owned(models.Model):
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author_key = models.CharField(max_length=200)
    author_all = models.TextField()
    pub_year = models.IntegerField()
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    owned_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.TextField()
    memo = models.TextField()


class Book_disposal(models.Model):
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author_all = models.TextField()
    pub_year = models.IntegerField()
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    owned_at = models.DateTimeField(auto_now_add=True)
    disposed_at = models.DateTimeField(auto_now=True)
    memo = models.TextField()

# Create your models here.
