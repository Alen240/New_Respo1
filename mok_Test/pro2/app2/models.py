from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=52)
    product_descrip=models.CharField(max_length=300)
    product_img=models.ImageField(upload_to='imageview')