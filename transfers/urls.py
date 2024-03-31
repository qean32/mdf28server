from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transfers.api import views

router = DefaultRouter()
# ################################# ###################### ################################

router.register(r'search/DOTA', views.transfer_DOTA_search_view,'search_transfer_DOTA')
router.register(r'search/CS', views.transfer_CS_search_view,'search_transfer_CS')
router.register(r'search/BASCKETBALL', views.transfer_BASCKETBALL_search_view,'search_transfer_BASCKETBALL')

urlpatterns = [
    path('tranfers/reg/DOTA/', views.transfer_DOTA_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('tranfers/reg/CS/', views.transfer_CS_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('tranfers/reg/BASCKETBALL/', views.transfer_BASCKETBALL_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
]

urlpatterns += path('tranfers/', include(router.urls)),