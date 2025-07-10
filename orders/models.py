from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Order(models.Model):
     STATUS_CHOICES = {
          "pnd":"pending",
          "prc":"processing",
          "dsp":"dispatched",
          "dlv":"delivered",
     }

     order_id = models.IntegerField(unique=True)
     username = models.ForeignKey(User, on_delete=models.CASCADE)
     phone_number = models.CharField(max_length=12)
     status = models.CharField(max_length=3, choices=STATUS_CHOICES, default="pnd")
     comment = models.TextField(blank=True, null=True)


     def __str__(self):

          return self.username.username+"#" + str(self.order_id)


class Ticket(models.Model):
     ticket_code = models.CharField(max_length=30)
     item_code = models.CharField(max_length=30)
     order = models.ForeignKey(Order, on_delete=models.CASCADE)

     #status

