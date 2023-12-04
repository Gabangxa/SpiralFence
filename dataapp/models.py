from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    RENEWAL_CHOICES = [
        ('ANNUAL', 'Annually'),
        ('SEMI_ANNUAL', 'Semi-Annually'),
        ('QUARTERLY', 'Quarterly'),
        ('MONTHLY', 'Monthly'),
        ('ONCE_OFF', 'Once-off')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    first_payment_date = models.DateField()
    renewal_type = models.CharField(max_length=12, choices=RENEWAL_CHOICES)
    auto_renew = models.BooleanField(default=False)
    auto_renew_date = models.DateField(null=True, blank=True)
    custom_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dataapp:detail', kwargs={'pk': self.pk})