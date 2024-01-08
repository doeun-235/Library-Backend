from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book_owned(models.Model):
    code = models.CharField(db_index=True,max_length=200,unique=True)
    title = models.CharField(max_length=200)
    author_key = models.CharField(max_length=200)
    author_all = models.TextField()
    pub_year = models.IntegerField()
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    owned_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # status - 0: 보유, 1: 대출, 2: 분실 3: 기타
    status = models.IntegerField(default=0,validators=[MinValueValidator(0),
                                                       MaxValueValidator(3)])
    memo = models.TextField(blank=True)


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
