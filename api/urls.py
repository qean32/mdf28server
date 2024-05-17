from django.urls import path, include

from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as user_urls
from cash.urls import urlpatterns as cash_urls
from news.urls import urlpatterns as news_urls
from chat.urls import urlpatterns as chat_urls
from transfers.urls import urlpatterns as transfers_urls
from disputes.urls import urlpatterns as disputes_urls
from b_unification.urls import urlpatterns as unification_urls

app_name = 'api'

urlpatterns = []

urlpatterns += doc_urls
urlpatterns += unification_urls
urlpatterns += user_urls
urlpatterns += cash_urls
urlpatterns += news_urls
urlpatterns += chat_urls
urlpatterns += transfers_urls
urlpatterns += disputes_urls
