from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Books(models.Model):
    book_name            = models.CharField(max_length=100)
    description          = models.TextField()
    author               = models.ForeignKey(Author,on_delete=models.CASCADE)
    status               = models.BooleanField(default=True)
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.book_name + "       |     "  + self.author.name