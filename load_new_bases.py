import os
from news.models import *
# from news.models import Author, Post, Category

# Путь к каталогу с текстовыми файлами
# C:\works\2023\SkillFactory\DDKNewsPortal\0goodwork\tests\skillfactory-ddkNewsPortal
# directory_path = 'C:/news/'
print("Работа с user1:")

directory_path = './newsuser1/'

user1 = User.objects.get(username='user1')
user2 = User.objects.get(username='user2') 

author1 = Author.objects.get(user=user1)
author2 = Author.objects.get(user=user2)

author1.user = user1
# Словарь для сопоставления имен категорий с объектами категорий
category_mapping = {
    'Спорт': Category.objects.get(name='Спорт'),
    'Политика': Category.objects.get(name='Политика'),
    'Культура': Category.objects.get(name='Культура'),
    'Наука': Category.objects.get(name='Наука'),
}
# Получение списка файлов в каталоге
files = os.listdir(directory_path)

# Перебор файлов
for file_name in files:
    # Формирование полного пути к файлу
    file_path = os.path.join(directory_path, file_name)

    # Извлечение категории и заголовка из имени файла
    category_name,  post_title_with_extension = file_name.split('_', 1)
    post_title = post_title_with_extension[:-4]

    # Получение или создание категории
    # category, created = Category.objects.get_or_create(name=category_name.strip())

    # Создание автора (предположим, что у вас уже есть объект Author, например, author1)
    # author = Author.objects.get(user=author1.user)

       # Получение объекта категории из словаря
    category = category_mapping.get(category_name.strip())

    if category:

        # Чтение текста из файла
        with open(file_path, 'r', encoding='utf-8') as file:
            post_text = file.read()

        # Создание новости и добавление категории
        # post = Post.objects.create(author=author, post_type=Post.news, title=post_title.strip(), text=post_text, rating=0)
        # post.categories.add(category)
        post = Post.objects.create(author=author1, post_type=Post.news, title=post_title, text=post_text, rating=0)
        post.categories.add(category)

        # print(f'<Добавлена новость:> {post_title} <в категорию:> {category}')
        print(f'Добавлена новость: {post.title} в категорию {category.name}')
    else:
        print(f'Ошибка: Неверная категория "{category_name.strip()}" в файле {file_name}')

print("Работа с user2:")

directory_path2 = './newsuser2/'
files2 = os.listdir(directory_path2)
for file_name2 in files2:
    file_path = os.path.join(directory_path2, file_name2)
    category_name,  post_title_with_extension = file_name2.split('_', 1)
    post_title = post_title_with_extension[:-4]
    category = category_mapping.get(category_name.strip())
    if category:
        with open(file_path, 'r', encoding='utf-8') as file:
            post_text = file.read()
        post = Post.objects.create(author=author2, post_type=Post.news, title=post_title, text=post_text, rating=0)    
        post.categories.add(category)
        print(f'Добавлена новость: {post.title} в категорию {category.name}')
    else:
        print(f'Ошибка: Неверная категория "{category_name.strip()}" в файле {file_name2}')
