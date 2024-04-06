from django.db import models
from .choices import Weekdays


class Schedule(models.Model):
    coach = models.ForeignKey("coaches.Coach", related_name="schedules",  on_delete=models.CASCADE)
    gym = models.ForeignKey('gyms.Gym', related_name="schedules", on_delete=models.CASCADE)
    weekday = models.CharField(max_length=10, choices=Weekdays.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.weekday.title()}: {self.coach.user.get_full_name()} at {self.gym.name}"

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"
        ordering = ['weekday', 'start_time', 'coach__user__last_name', 'coach__user__first_name']


class Record(models.Model):
    client = models.ForeignKey("users.User", related_name='client_records', on_delete=models.CASCADE)
    coach = models.ForeignKey("coaches.Coach",  related_name='coach_records', on_delete=models.CASCADE)
    gym = models.ForeignKey("gyms.Gym",  related_name='gym_records', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} - {self.gym.name} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"
        ordering = ['-start_time', 'client__last_name', 'client__first_name']



