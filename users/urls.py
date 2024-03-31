from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from users.api import views

router = DefaultRouter()


router.register(r'search/user', views.UserListSearchView)
router.register(r'update/user', views.UserUpdateView)
router.register(r'search_short/user', views.UserListSearchView_short)

router.register(r'search/follow_id', views.FollowListSearchView_id)
router.register(r'search/follow', views.FollowListSearchView)
router.register(r'delete/follow', views.FollowDeleteView)

urlpatterns = [
    path('users/reg/', views.RegistrationView.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('users/reg/follow/', views.FollowRegView.as_view({
        'post': 'create'
    }), name='cwasdas'),
    path('users/change_password/', views.ChangePasswordView.as_view(), name='change_passwd'),
    path('users/change_email/', views.ChangeEmailView.as_view(), name='change_passwd'),
    path('users/token/access', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += path('users/', include(router.urls)),