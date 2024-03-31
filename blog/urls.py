from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.api import views

router = DefaultRouter()
# ################################# ###################### ################################

router.register(r'reg_blog', views.post_reg_view)
router.register(r'update_blog', views.post_update_view, 'blog-update')
router.register(r'search_blog', views.post_search_view, 'blog-search')


urlpatterns = []

urlpatterns += path('blog/', include(router.urls)),