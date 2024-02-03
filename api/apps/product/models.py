from django.db import models
from api.apps.common.models import BaseModel

sizes = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
    ('XXL', 'Extra Extra Large'),
)

color = (
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Black', 'Black'),
    ('White', 'White'),
)


class Product(BaseModel):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    deleted = models.BooleanField(default=True)
    discountPercentage = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)
    rating = models.IntegerField(default=0 )
    stock = models.IntegerField(default=0)
   
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    # thumbnail = models.ImageField(upload_to="products/thumbnails", null=True, blank=True)
    # images = models.ImageField(upload_to="products/images", null=True, blank=True)
    color = models.CharField(max_length=120, choices=color, null= True, blank=True)
    size = models.CharField(max_length=120, choices=sizes ,null= True, blank=True)

    def __str__(self):
        return self.title



class Brand(BaseModel):
    name = models.CharField(max_length=120)
    lable = models.CharField(max_length=120)
    description = models.TextField()
    

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=120)
    lable = models.CharField(max_length=120)
    description = models.TextField()
   
    def __str__(self):
        return self.name