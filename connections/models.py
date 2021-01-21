from django.db import models


class Publisher(models.Model):
    pub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.pub_title


class Book(models.Model):
    title = models.CharField(max_length=100)
    publishing = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Description(models.Model):
    book = models.OneToOneField(Book,
                                on_delete=models.CASCADE,
                                primary_key=True)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.text


class Author(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
