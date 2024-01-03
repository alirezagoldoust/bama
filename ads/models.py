from django.db import models
import datetime

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    type = models.CharField(max_length=20, choices=(("car", "car"), 
                                                    ("bicycle", "bicycle"),
                                                    ("motor", "motor"), 
                                                    ("heavy_car", "heavy_car")), default = 'car')
    acceleration = models.FloatField()
    power = models.IntegerField()
    fuel = models.CharField(max_length=20, choices=(('petrol','petrol'), 
                                                    ('electricity', 'electricity'), 
                                                    ('gasoline', 'gasoline')), default = 'petrol')
    def __str__(self) -> str:
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=(('shakhsi', 'shakhsi'),
                                                    ('bongah', 'bongah'),
                                                    ('namayeshgah','namayeshgah')), default='shakhsi')
    phone_number=models.CharField(max_length=11)
    verified = models.BooleanField()
    def __str__(self) -> str:
        return self.name

class Ads(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    kilometer = models.IntegerField()
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=20)
    posting_time = models.DateTimeField(editable=False, default=datetime.datetime.now())
    nardebam = models.BooleanField()