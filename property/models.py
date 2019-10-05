from django.db import models

# Create your models here.

#property type is choices so we have to create choices like this -- hitesh
property_type = (
    ('Sale' , "sale"),
    ('Rent' , "rent")
)

class Property(models.Model):
    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type, max_length=10)
    price = models.IntegerField()
    category = models.ForeignKey('Category' ,null = True, on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2 ,max_digits= 10 )
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null = True) #upload to property folder -hitesh
    location = models.CharField(max_length=50, null=True)

# to have the property name as it is in admin section instead of having default name like property object1 -hitesh
    def __str__(self):
        return self.name

#To fix the name from Propertys to Property or Properties    - hitesh
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category/', null = True)

    # to have the category name as it is in admin section instead of having default name like category object1 -hitesh
    def __str__(self):
        return self.category_name

    #To fix the name from Categorys to Category or Categories - hitesh
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Reserve(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name


