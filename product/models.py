from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    size = models.IntegerField()

    def __str__(self):
        return self.title

