from django.urls import path, include

from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as user_urls
from blog.urls import urlpatterns as blog_urls
from cash.urls import urlpatterns as cash_urls
from news.urls import urlpatterns as news_urls
from chat.urls import urlpatterns as chat_urls
from dota.urls import urlpatterns as dota_urls
from cs.urls import urlpatterns as cs2_urls
from transfers.urls import urlpatterns as transfers_urls
from disputes.urls import urlpatterns as disputes_urls
from bascketball.urls import urlpatterns as bascketball_urls
from poker.urls import urlpatterns as poker_urls

app_name = 'api'

urlpatterns = []

urlpatterns += doc_urls
urlpatterns += user_urls
urlpatterns += blog_urls
urlpatterns += cash_urls
urlpatterns += news_urls
urlpatterns += chat_urls
urlpatterns += transfers_urls
urlpatterns += dota_urls
urlpatterns += disputes_urls
urlpatterns += bascketball_urls
urlpatterns += poker_urls
urlpatterns += cs2_urls
