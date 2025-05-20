from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_filter = ('is_published',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        (_('Дополнительные параметры'), {
            'fields': ('slug', 'is_published'),
            'classes': ('collapse',),
            'description': _('Дополнительные настройки категории')
        }),
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'category', 'location')
    filter_horizontal = ()
    date_hierarchy = 'pub_date'

    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'author')
        }),
        (_('Параметры публикации'), {
            'fields': (
                'pub_date',
                'location',
                'category',
                'is_published'
            ),
            'description': _('Настройки отображения публикации')
        }),
    )
