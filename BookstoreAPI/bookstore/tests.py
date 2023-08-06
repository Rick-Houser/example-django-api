from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

class BookApiTests(TestCase):
    """
    Test cases for the Book API views.

    - `setUp`: Sets up the test client (APIClient) for making API requests.
    - `test_create_book`: Tests creating a new book through the 'book-list-create' API endpoint.
    - `test_get_single_book`: Tests retrieving a single book through the 'book-detail' API endpoint.
    """
    def setUp(self):
        self.client = APIClient()

    def test_create_book(self):
        url = reverse('book-list-create')
        data = {'title': 'Test Book', 'author': 'Test Author', 'publication_date': '2023-07-26'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_get_single_book(self):
        book = Book.objects.create(title='Test Book', author='Test Author', publication_date='2023-07-26')
        url = reverse('book-detail', kwargs={'pk': book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')
