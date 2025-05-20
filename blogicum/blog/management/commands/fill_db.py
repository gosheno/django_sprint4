from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Category, Location, Post
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Fill database with test data'

    def handle(self, *args, **options):
        fake = Faker('ru_RU')

        # Очистка старых данных
        Post.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

        # Создание пользователя
        user = User.objects.create_user(
            username='test_user',
            password='testpass123',
            email='test@example.com'
        )

        # Создание категорий
        categories = []
        for i in range(5):
            cat = Category.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text(max_nb_chars=200),
                slug=f'category-{i}',
                is_published=True
            )
            categories.append(cat)

        # Создание локаций
        locations = []
        for i in range(3):
            loc = Location.objects.create(
                name=fake.city(),
                is_published=True
            )
            locations.append(loc)

        # Создание публикаций
        for i in range(15):
            Post.objects.create(
                title=fake.sentence(nb_words=6),
                text=fake.text(max_nb_chars=1000),
                pub_date=fake.past_date(),
                author=user,
                category=fake.random_element(categories),
                location=fake.random_element(locations) if i % 2 else None,
                is_published=True
            )

        self.stdout.write(self.style.SUCCESS('Successfully filled database'))
