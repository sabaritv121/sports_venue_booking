from django.db import models

# Create your models here.

#venue table
class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    choices = (
        ('football','football'),('cricket','cricket'),('hockey','hockey')
    )
    type = models.CharField(choices=choices,max_length=25)

    def __str__(self):
        return self.name

#user table
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#Booking table
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timing = (
        ('4PM', '4PM'),('5PM', '5PM'),('6PM', '6PM'),('7PM', '7PM'),('8PM', '8PM'),('9PM', '9PM'),('10PM', '10PM'),('11PM', '11PM')
    )
    time_slot = models.CharField(choices=timing,max_length=25)
    date = models.DateField()



