from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cash.api import views
router = DefaultRouter()

# ################################# ###################### ################################

router.register(r'search/list_cash',views.list_cash_search_view,'list_cash-search')
router.register(r'update/list_cash',views.list_cash_update_view,'list_cash-update_org')

router.register(r'delete/cash',views.cash_delete_view,'cash-delete')
router.register(r'search/cash',views.cash_search_view,'cash-search')

urlpatterns = [
    path('cash/reg/cash/', views.cash_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
]

urlpatterns += path('cash/', include(router.urls)),