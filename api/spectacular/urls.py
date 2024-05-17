from django.urls import path

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]