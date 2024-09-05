from rest_framework import viewsets
from .models import InvestmentFund, PriceChange, UserInvestment, InvestmentHistory
from .serializers import InvestmentFundSerializer, PriceChangeSerializer, UserInvestmentSerializer, InvestmentHistorySerializer

class InvestmentFundViewSet(viewsets.ModelViewSet):
    queryset = InvestmentFund.objects.all()
    serializer_class = InvestmentFundSerializer

class PriceChangeViewSet(viewsets.ModelViewSet):
    queryset = PriceChange.objects.all()
    serializer_class = PriceChangeSerializer

class UserInvestmentViewSet(viewsets.ModelViewSet):
    queryset = UserInvestment.objects.all()
    serializer_class = UserInvestmentSerializer

class InvestmentHistoryViewSet(viewsets.ModelViewSet):
    queryset = InvestmentHistory.objects.all()
    serializer_class = InvestmentHistorySerializer
