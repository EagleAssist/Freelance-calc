from django.db import models

class Rate(models.Model):
    type_choices = [('web', 'Web'), ('mobile', 'Mobile'), ('dtp', 'DTP')]
    complexity_choices = [('high', 'High'), ('medium', 'Medium'), ('low', 'Low')]

    rate_type = models.CharField(max_length=10, choices=type_choices, default='web')
    complexity = models.CharField(max_length=10, choices=complexity_choices, default='medium')
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.get_rate_type_display()} - {self.get_complexity_display()}"