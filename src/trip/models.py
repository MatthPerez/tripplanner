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
    
    @property
    def travel_total(self):
        return sum(travel.price for travel in self.travels.all())
    
    @property
    def housing_total(self):
        return sum(airbnb.charges + airbnb.price * self.duration for airbnb in self.housing.all())
    
    @property
    def activity_total(self):
        return sum(activity.price_person for activity in self.activities.all())
    
    @property
    def expense_total(self):
        return sum(expense.price for expense in self.expenses.all())
    
    @property
    def total_price(self):
        return self.travel_total + self.housing_total + self.activity_total + self.expense_total
