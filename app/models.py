from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Borrower(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone = models.CharField(max_length=20, null=True, blank=True)

class Loan(models.Model):
  borrower = models.ForeignKey(
    'Borrower',
    on_delete=models.CASCADE,
    related_name='loans'
  )
  principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
  interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
  start_date = models.DateField()
  STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('ACTIVE', 'Active'),
    ('PAID', 'Paid'),
    ('DEFAULTED', 'Defaulted'),
  ]
  status = models.CharField(
    max_length=10,
    choices=STATUS_CHOICES,
    default='PENDING',
    help_text="The current status of the loan."
  )

class Investor(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone = models.CharField(max_length=20, null=True, blank=True)
  total_contributions = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

class Transaction(models.Model):
  amount = models.DecimalField(max_digits=12, decimal_places=2)
  investor = models.ForeignKey(
    Investor,
    on_delete=models.CASCADE,
    related_name='transactions'
  )
  reason = models.CharField(max_length=50)
  notes = models.CharField(max_length=100)
  created_at=models.DateTimeField(auto_now_add=True)



# class Admin(AbstractUser):