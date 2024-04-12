# coding=utf-8

from django.db import models


class Book(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(u'Название', max_length=64, null=False)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')

    def __str__(self):
        return self.name + " " + self.author
    
# createdb -U postgres hw_django_db_book
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver