from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.api import views

router = DefaultRouter()
# ################################# ###################### ################################


router.register(r'update/message', views.message_update_view, 'message-update')
router.register(r'search/message', views.message_search_view, 'message-search')

router.register(r'delite/like', views.like_delite_view)



urlpatterns = [
    path('chat/reg/like/', views.like_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('chat/reg/message/', views.message_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
]

urlpatterns += path('chat/', include(router.urls)),