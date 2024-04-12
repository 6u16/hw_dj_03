from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort')  # Берём параметр sort из опционального GET запроса для сортировки страницы
    
    # Сортировка в запросах к БД
    if sort_by is None: phone_objects = Phone.objects.all()
    if sort_by == 'name': phone_objects = Phone.objects.order_by('name')
    if sort_by == 'min_price': phone_objects = Phone.objects.order_by('price')
    if sort_by == 'max_price': phone_objects = Phone.objects.order_by('price').reverse()
    
    context = {
        'phones':phone_objects
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)  # Читаем из БД позиции
    context = {
        'phone':phone[0]  # Нужна распаковка QuerySet чтобы достать объект <QuerySet [<Phone: Phone object (3)>]>
        }
    return render(request, template, context)
