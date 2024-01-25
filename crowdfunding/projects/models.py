from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model
from django.utils import timezone 

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects')
    timezone = models.CharField(max_length=63, default='UTC')
    
    def total_amount_received(self):
        total_amount = self.pledges.filter(date_created__lte=self.date_created).aggregate(Sum('amount'))['amount__sum']
        return total_amount or 0
    
    def __str__(self):
        return self.title

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supported_pledges'
    )
    pledge_timezone = models.CharField(max_length=63, default='UTC')

    def __str__(self):
        return f"{self.supporter} - {self.amount} AUD on {self.project.title}"