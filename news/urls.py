from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.api import views

router = DefaultRouter()
# ################################# ###################### ################################

router.register(r'delete/like', views.like_update_view, 'like-update')

urlpatterns = [
    path('news/search/news/', views.post_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('news/reg/like/', views.like_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('news/search/like/', views.like_search_view.as_view({'get': 'list'}), name='cwasdas'),

    path('news/reg/coment/', views.coment_reg_view.as_view({'post': 'create'}), name='cwasdas'),
    path('news/search/coment/', views.coment_search_view.as_view({'get': 'list'}), name='cwasdas'),
]

urlpatterns += path('news/', include(router.urls)),