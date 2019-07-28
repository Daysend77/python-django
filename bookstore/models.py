from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(Author, default=0, on_delete=models.CASCADE)


class Comment(models.Model):
    book = models.ForeignKey(Book, default=0, null=True, on_delete=models.CASCADE)
    nick = models.CharField(max_length=50, default='Guest')
    text = models.CharField(max_length=500)
    time = models.TimeField(blank=True, null=True)
