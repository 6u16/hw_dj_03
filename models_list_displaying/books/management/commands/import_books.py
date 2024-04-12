import json
from pprint import pprint

from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f) # функция обрабочик: преобразует в словарь

        for book in json_data:
        
            book_obj = Book(
                id = book.get('pk'),
                name = book.get('fields').get('name'),
                author = book.get('fields').get('author'),
                pub_date = book.get('fields').get('pub_date'),
                )
            book_obj.save()
            
# python manage.py import_books

    
    