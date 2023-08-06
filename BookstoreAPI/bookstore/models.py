from django.db import models

"""
    Model representing a book with title, author, and publication date fields.
"""
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
