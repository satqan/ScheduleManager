from django.db import models


class Coach(models.Model):
    user = models.OneToOneField("users.User", related_name="coach", on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=False)
    gender = models.CharField(max_length=10, blank=False)
    gyms = models.ManyToManyField('gyms.Gym', related_name="coaches", blank=True)

    class Meta:
        verbose_name = "Coach"
        verbose_name_plural = "Coaches"
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
