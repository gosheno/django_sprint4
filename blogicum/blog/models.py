from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Заголовок')
    )
    description = models.TextField(
        verbose_name=_('Описание')
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        verbose_name=_('Идентификатор'),
        help_text=_('Идентификатор страницы для URL; '
                    + 'разрешены символы латиницы, '
                    + 'цифры, дефис и подчёркивание.'))
    is_published = models.BooleanField(
        default=True,
        verbose_name=_('Опубликовано'),
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Добавлено')
    )

    class Meta:
        verbose_name = _('категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name=_('Название места')
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name=_('Опубликовано'),
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Добавлено')
    )

    class Meta:
        verbose_name = _('местоположение')
        verbose_name_plural = _('Местоположения')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Заголовок')
    )
    text = models.TextField(
        verbose_name=_('Текст')
    )
    pub_date = models.DateTimeField(
        verbose_name=_('Дата и время публикации'),
        help_text=_('Если установить дату и '
                    + 'время в будущем — можно делать отложенные публикации.'))
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Автор публикации')
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Местоположение')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Категория')
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name=_('Опубликовано'),
        help_text=_('Снимите галочку, чтобы скрыть публикацию.')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Добавлено')
    )
    image = models.ImageField(
        upload_to='media/',
        verbose_name=_('Изображение'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('публикация')
        verbose_name_plural = _('Публикации')
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Комментарий',
        related_name='comments',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created_at',)

    def __str__(self) -> str:
        return self.text
