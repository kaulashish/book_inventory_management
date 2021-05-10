from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Store(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StoreInventory(models.Model):
    store = models.ForeignKey(Store, on_delete=CASCADE, null=True, blank=True)
    book = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    google_id = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    count = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.store) + f" (obj {self.id})"
