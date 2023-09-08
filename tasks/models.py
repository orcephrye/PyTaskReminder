import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import now


# Create your models here.
class Tasks(models.Model):
    twentyFourHour = "day"
    sevenDays = "week"
    oneMonth = "month"
    oneYear = "year"
    length_of_time_choices = [
        (twentyFourHour, "Within this Day"),
        (sevenDays, "Within this Week"),
        (oneMonth, "Within this Month"),
        (oneYear, "Within this Year"),
    ]
    lengthMap = {
        twentyFourHour: 24,
        sevenDays: 168,
        oneMonth: 5040,
        oneYear: 60480
    }
    name = models.CharField(max_length=28)
    description_text = models.CharField(max_length=4000)
    persistence = models.BooleanField(default=False)
    time_from = models.DateTimeField(default=now)
    length = models.CharField(max_length=28, choices=length_of_time_choices, default=twentyFourHour)

    def __str__(self):
        return self.name

    def is_valid(self):
        return self.time_from >= timezone.now() - datetime.timedelta(hours=self.lengthMap.get(self.length, 24))
