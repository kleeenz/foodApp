from django.db import models

#creating the object in database with the food as the name of the table, and listosfood as column name
class food(models.Model):
    listoffood = models.CharField(max_length=100)
