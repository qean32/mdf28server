from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cash.api import views
router = DefaultRouter()

# ################################# ###################### ################################


urlpatterns = [
    path('cash/reg/cash/', views.cash_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    
    path('cash/search/cash/', views.cash_search_view.as_view({'get': 'list'}), name='cwasdas'),
    path('cash/search/cash/list/', views.list_cash_search_view.as_view({'get': 'list'}), name='cwasdas'),
]

urlpatterns += path('cash/', include(router.urls)),