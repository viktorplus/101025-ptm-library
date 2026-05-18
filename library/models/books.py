from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone

"""1. Строковое отображение моделей

Обновите каждую модель так, чтобы при работе в админ панели, а так же при
отображении объекта модели было более описательное отображение.

Ожидаемое поведение:

- Author отображается как имя и фамилия автора.
- Book отображается как название книги.
- User отображается как username.
- Membership отображается как связь пользователя и библиотеки.
- Library отображается как название библиотеки.
- Publisher отображается как название издателя.
- Category отображается как название категории.
- Posts отображается как заголовок поста.
- Borrow отображается как выдача книги пользователю.
- Event отображается как название события и дата события.
- EventParticipant отображается как регистрация на событие.
- Review отображается как отзыв на книгу с указанием книги, пользователя и рейтинга.

Метод не должен падать, если часть необязательных полей пустая."""

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )
    libraries = models.ManyToManyField(
        'Library',
        related_name='books'
    )
    description= models.TextField(
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    discounted_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    pages = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(1500)],
        null=True,
        blank=True
    )
    publisher = models.ForeignKey(
        'Publisher',
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    owner = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books',
    )
    published_date = models.DateField(default=timezone.now)


def __str__(self):
    return self.name