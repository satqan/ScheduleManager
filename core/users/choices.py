from django.db.models import TextChoices


class UserRoles(TextChoices):
    COACH = 'coach', 'Coach'
    CLIENT = 'client', 'Client'
    ADMIN = 'admin', 'Admin'