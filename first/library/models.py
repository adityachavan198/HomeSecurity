from django.db import models

# Create your models here.
class PublicationHouse(models.Model):
    name = models.CharField(max_length=50)
    ratings = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=40)#class level attributes
    price=models.FloatField()
    pages=models.IntegerField()
    publicationhouse = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title #changes the name to the title

class Review(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)



class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    def __str__(self):
        return self.username
