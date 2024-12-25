from django.db import models
from django.utils.timezone import now
from travel.models import Travel
from airbnb.models import Airbnb
from activity.models import Activity
from expense.models import Expense

class Trip(models.Model):
    date = models.DateField(default=now)
    duration = models.IntegerField()
    place = models.CharField(max_length=100)
    people = models.IntegerField()
    travels = models.ManyToManyField(Travel, related_name="travels_list")
    housing = models.ManyToManyField(Airbnb, related_name="airbnbs_list")
    activities = models.ManyToManyField(Activity, related_name="activities_list")
    expenses = models.ManyToManyField(Expense, related_name="expenses_list")


    def __str__(self):
        return self.place
    