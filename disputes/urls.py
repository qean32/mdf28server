from django.urls import path, include
from rest_framework.routers import DefaultRouter
from disputes.api import views

router = DefaultRouter()
# ################################# ###################### ################################

router.register(r'update/message', views.message_update_view, 'message-update')
router.register(r'search/message', views.message_search_view, 'message-search')

router.register(r'update/disput_for_org', views.disput_update_view_for_org, 'disput-update_for_org')
router.register(r'search/disput', views.disput_search_view, 'disput-search')
router.register(r'search_short/disput', views.disput_search_view_short, 'disput-search_short')

urlpatterns = [
    path('disputes/reg/disput/', views.disput_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('disputes/reg/message/', views.message_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
]

urlpatterns += path('disputes/', include(router.urls)),