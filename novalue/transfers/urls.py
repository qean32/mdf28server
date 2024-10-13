from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transfers.api import views

router = DefaultRouter()
# ################################# ###################### ################################

router.register(r'search', views.transfer_search_view,'search_transfer')

urlpatterns = [
    path('transfers/reg/', views.transfer_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
]

urlpatterns += path('transfers/', include(router.urls)),