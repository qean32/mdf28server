from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.api import views

router = DefaultRouter()
# ################################# ###################### ################################


urlpatterns = [
    path('chat/reg/message/', views.message_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('chat/search/message/', views.message_search_view.as_view({'get': 'list'}), name='cwasdas'),
]

urlpatterns += path('chat/', include(router.urls)),