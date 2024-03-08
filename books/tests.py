import pytest
from django.contrib.auth.models import User
from .models import Book, Rating


@pytest.mark.django_db
def test():
    user = User.objects.create_user(username='testuser', password='testpassword')
    book = Book.objects.create(title='Test Book', author='Test Author')
    Rating.objects.create(user=user, book=book, rating=5)
    rating = Rating.objects.get(user=user, book=book)
    assert rating.rating == 5
