from django.db.models import TextChoices


class Weekdays(TextChoices):
    MONDAY = 'monday', 'Monday'
    TUESDAY = 'tuesday', 'Tuesday'
    WEDNESDAY = 'wednesday', 'Wednesday'
    THURSDAY = 'thursday', 'Thursday'
    FRIDAY = 'friday', 'Friday'
    SATURDAY = 'saturday', 'Saturday'
    SUNDAY = 'sunday', 'Sunday'