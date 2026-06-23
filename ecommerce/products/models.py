from django.db import models
from django.db.models import Q


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=800)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        constraints = [
            models.CheckConstraint(
                condition = Q(price__gt=0),
                name = 'product_price_should_be_greater_than_zero',
            ),
            models.CheckConstraint(
                condition = Q(quantity__gte=0),
                name = 'product_quantity_should_not_be_less_than_zero',
            )
        ]
