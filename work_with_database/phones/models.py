from django.db import models
from django.utils.text import slugify



class Phone(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, null=False)  # brand будет полем CharField с макс. длинной строки = 50
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=250)    
    release_date = models.CharField(max_length=50)
    lte_exists  = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
    

# Slug – это как ярлычок 🏷️ для веб-страницы, делающий её адрес понятным и уникальным, используя только буквы, цифры и дефисы.
# Это помогает людям и поисковикам легко понять, о чём страница, даже не открывая её.

# Слуг решает проблему запутанных и непонятных URL, которые могут отпугнуть пользователей и затруднить индексацию сайта поисковыми системами.
# Это делает веб-адреса легко читаемыми и запоминающимися, улучшая взаимодействие с сайтом и его поисковую оптимизацию.

# Это упрощает написание программ, делая веб-разработку более интуитивно понятной и эффективной. Понимание того,
# как создавать и использовать слаг, помогает в структурировании информации на сайте, делая его более доступным как для пользователей,
# так и для поисковых систем.

# Пример
# Допустим, вы создаете блог на Django, где каждая статья имеет свой уникальный URL для доступа. Вместо того, чтобы использовать неудобные и
# непонятные цифровые идентификаторы в URL, например, https://example.com/articles/12345, вы решаете сделать адреса понятными и
# запоминающимися. Здесь на помощь приходит понятие slug.

# Представим, что у вас есть статья с заголовком "Как вырастить томаты на балконе". Вместо цифрового идентификатора вы используете slug,
# преобразовав заголовок в удобочитаемый формат: "kak-vyrastit-tomaty-na-balkone". Таким образом,
# URL вашей статьи превращается в https://example.com/articles/kak-vyrastit-tomaty-na-balkone, что гораздо информативнее и понятнее для
# пользователей.

# Вот как это можно реализовать в модели Django:
    
# from django.db import models
# from django.utils.text import slugify

# class Article(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     slug = models.SlugField(max_length=255, unique=True, blank=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(Article, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.title

# В этом примере при сохранении статьи (Article) в базу данных, если поле slug пустое, Django автоматически генерирует его из
# заголовка статьи с помощью функции slugify. Это делает URL не только понятным и запоминающимся, но и уникальным, что важно для SEO и
# удобства пользователей.

# Таким образом, использование slug позволяет решить проблему неудобных и непонятных URL, делая их информативными и дружелюбными как для
# пользователей, так и для поисковых систем.












