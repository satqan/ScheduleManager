from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=500, blank=False)
    contact_number = models.CharField(max_length=15, blank=False)
    email = models.EmailField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.name}, {self.address}"

    class Meta:
        verbose_name = "Gym"
        verbose_name_plural = "Gyms"
        ordering = ['name']