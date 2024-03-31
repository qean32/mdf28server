from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.api import views

router = DefaultRouter()
# ################################# ###################### ################################

router.register(r'search/news', views.post_search_view, 'news-search')

router.register(r'update/like', views.like_update_view, 'like-update')
router.register(r'search/like', views.like_search_view, 'like-search')

router.register(r'update/coment', views.coment_update_view, 'coment-update')
router.register(r'search/coment', views.coment_search_view, 'coment-search')

urlpatterns = [
    path('news/reg/like/', views.like_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('news/reg/coment/', views.coment_reg_view.as_view({
        'post': 'create'
    }), name='cwasdas'),
]

urlpatterns += path('news/', include(router.urls)),