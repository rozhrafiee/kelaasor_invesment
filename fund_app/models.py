from django.db import models
from django.contrib.auth.models import User

class InvestmentFund(models.Model):
    name = models.CharField(max_length=100)
    backing = models.CharField(max_length=20)  # Updated to store backing as a string
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PriceChange(models.Model):
    fund = models.ForeignKey(InvestmentFund, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.fund.name} - {self.month} {self.year}"

class UserInvestment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fund = models.ForeignKey(InvestmentFund, on_delete=models.CASCADE)
    initial_amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

class InvestmentHistory(models.Model):
    user_investment = models.ForeignKey(UserInvestment, on_delete=models.CASCADE)
    calculated_amount = models.FloatField()
    calculation_date = models.DateField()
