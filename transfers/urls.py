from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transfers.api import views

router = DefaultRouter()
# ################################# ###################### ################################

urlpatterns = [
    path('transfers/reg/', views.transfer_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('transfers/search/', views.transfer_search_view.as_view({'get': 'list'}), name='cwasdas'),
]

urlpatterns += path('transfers/', include(router.urls)),