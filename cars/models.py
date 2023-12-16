from django.db import models
from django.contrib.auth.models import User
from brands.models import Brands
# Create your models here.


class Car(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='cars/media/uploads', blank=True, null=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    buyers = models.ManyToManyField(
        User, related_name='bought_cars', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)



