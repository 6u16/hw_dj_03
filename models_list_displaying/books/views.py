from django.shortcuts import render
from books.models import Book
from books.converters import DateConverter
from django.core.paginator import Paginator
from pprint import pprint


# Образец: catalog_1.png
def books_view(request):
    template = 'books/books_list.html'
    
    book_obj = Book.objects.all()
    dc_01 = DateConverter(name='dc_01')  # Создаём объект класса конвертер
    
    # Изменяем формат отображения даты публикации: <class 'datetime.date'> - берётся в таком виде из БД на <class 'str'> - для использования в качестве URL
    for elem in book_obj:
        dc_01.to_url(value=elem.pub_date)
        #print(type(dc_01.to_url(value=elem.pub_date)))
        elem.pub_date = dc_01.to_url(value=elem.pub_date)
        
    context = {
        'books':book_obj
    }
        
    return render(request, template, context)


# Образец: catalog_2.png
def books_pub_date(request, date):  # date - параметр функции из динамического URL, дату публикации книги, http://127.0.0.1:8000/books/2018-09-07/ и получим книги по фильтру публикации
    template = 'books/books_pub_date.html'

    ## Запрашиваем книги по фильтру даты публикации
    dc_02 = DateConverter(name='dc_02')  # Создаём объект класса конвертер
    convert_data = dc_02.to_python(value=date)  # Конвертируем URL(<class 'str'>) дату публикации в <class 'datetime.date'> для нахождения книг по фильтру даты публикации, в БД дата хранится в формате <class 'datetime.date'>
    
    book_obj = Book.objects.filter(pub_date=convert_data)  # получаем книги по фильтру даты публикации
    
    # Изменяем формат отображения даты публикации: <class 'datetime.date'> - берётся в таком виде из БД на <class 'str'> - для использования в качестве URL
    for elem in book_obj:
        dc_02.to_url(value=elem.pub_date)
        #print(type(dc_01.to_url(value=elem.pub_date)))
        elem.pub_date = dc_02.to_url(value=elem.pub_date)
    
    
    ## Запрашиваем для пагинации по датам список дат публикации
    book_obj_01 = Book.objects.values('pub_date')
    
    dc_03 = DateConverter(name='dc_03')  # Создаём объект класса конвертер
    
    l_date = []
    for elem in book_obj_01:  # Конвертируем даты в формат <str> и создаём список для пагинации
        dc_03.to_url(value=elem.get('pub_date'))
        elem = dc_03.to_url(value=elem.get('pub_date'))
        l_date.append(elem)
    
    # Убираем дубликаты дат из списка
    l_wthout_dublic = []
    for elem in l_date:
        if l_wthout_dublic.count(elem): continue
        else: l_wthout_dublic.append(elem)
    
    context = {
        'books':book_obj,
        'dates':l_wthout_dublic,
    }
    
    return render(request, template, context)