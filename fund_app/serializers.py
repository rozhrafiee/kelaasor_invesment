from rest_framework import serializers
from .models import InvestmentFund, PriceChange, UserInvestment, InvestmentHistory

class InvestmentFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentFund
        fields = ['id', 'name', 'backing', 'created_at']

class PriceChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceChange
        fields = ['id', 'fund', 'month', 'year', 'price']

class UserInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInvestment
        fields = ['id', 'user', 'fund', 'initial_amount', 'start_date', 'end_date']

class InvestmentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentHistory
        fields = ['id', 'user_investment', 'calculated_amount', 'calculation_date']
