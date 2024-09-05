from django.urls import path, include from rest_framework.routers
import DefaultRouter from .views import InvestmentFundViewSet, PriceChangeViewSet, UserInvestmentViewSet,
InvestmentHistoryViewSet router = DefaultRouter() router.register(r'investment_funds', InvestmentFundViewSet)
router.register(r'price_changes', PriceChangeViewSet)
router.register(r'user_investments', UserInvestmentViewSet)
router.register(r'investment_histories', InvestmentHistoryViewSet)
urlpatterns = [ path('', include(router.urls)), ]
