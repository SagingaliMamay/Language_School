from django.db import models

# Model for blog's articles

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True) # 'Category' is str because staying after Article, PROTECT --> protection from delete

    # __str__ is to return object into string

    def __str__(self):
        return self.title


# I create table Category to normalize db & optimize the search of articles by categories
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name