from django.db import models

class Tag(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Product(models.Model):
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    size = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews')
    text = models.TextField()

    def __str__(self):
        return f"{self.product.title} - {self.text}"
