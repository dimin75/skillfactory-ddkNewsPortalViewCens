# Импорт моделей
from django.contrib.auth.models import User
from news.models import *

# 1. создаем двух пользователей:
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

# 2. Создать два объекта модели Author, связанные с пользователями.
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# 3. Добавить 4 категории в модель Category.
category1 = Category.objects.create(name='Спорт')
category2 = Category.objects.create(name='Политика')
category3 = Category.objects.create(name='Культура')
category4 = Category.objects.create(name='Наука')

# 4. Добавить 2 статьи и 1 новость.
# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

post1 = Post.objects.create(author=author1, post_type=Post.article, title='Заголовок статьи 1 про спорт', text='Текст статьи 1', rating = 0)
post1.categories.add(category1, category2)
post2 = Post.objects.create(author=author2, post_type=Post.article, title='Заголовок статьи 2 про культуру', text='Текст статьи 2', rating = 0)
post2.categories.add(category3, category4)
post3 = Post.objects.create(author=author1, post_type=Post.news, title='Заголовок новости 1 про политику',  text='Текст новости 1', rating = 0)
post3.categories.add(category1, category2)

# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий к статье 1', rating = 0)
comment2 = Comment.objects.create(post=post2, user=user2, text='Комментарий к статье 2', rating = 0)
comment3 = Comment.objects.create(post=post1, user=user2, text='Комментарий к статье 1 от user2', rating = 0)
comment4 = Comment.objects.create(post=post3, user=user1, text='Комментарий к новости 1', rating = 0)

# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.

post1.like()
post2.dislike()
comment1.like()
comment2.dislike()

# 8. Обновить рейтинги пользователей.
author1.update_rating()
author2.update_rating()

# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
best_author = Author.objects.order_by('-rating').first()
print(f'Лучший пользователь: {best_author.user.username}, рейтинг: {best_author.rating}')

# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
best_post = Post.objects.filter(post_type=Post.article).order_by('-rating').first()
print(f'Дата добавления: {best_post.created_at}')
print(f'Автор: {best_post.author.user.username}')
print(f'Рейтинг: {best_post.rating}')
print(f'Заголовок: {best_post.title}')
print(f'Превью: {best_post.preview()}')

# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
comments_to_best_post = Comment.objects.filter(post=best_post)
for comment in comments_to_best_post:
    print(f'Дата: {comment.created_at}')
    print(f'Пользователь: {comment.user.username}')
    print(f'Рейтинг: {comment.rating}')
    print(f'Текст: {comment.text}')

# Вроде бы на этом можно закончить в этот раз... :)
