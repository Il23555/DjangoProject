from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from cinemaApp.views import SeanceView, HallView, BookingView, MovieView, GenreView, PlaceView, \
    SeanceViewList, PlaceViewList, HallViewList, GenreViewList, MovieViewList, BookingViewList, UserCreate, ProfileView
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('seance/', SeanceViewList.as_view()),
    path('seance/<int:pk>', SeanceView.as_view()),
    path('booking/', BookingViewList.as_view()),
    path('booking/<int:pk>', BookingView.as_view()),
    path('movie/', MovieViewList.as_view()),
    path('movie/<int:pk>', MovieView.as_view()),
    path('genre/', GenreViewList.as_view()),
    path('genre/<int:pk>', GenreView.as_view()),
    path('hall/', HallViewList.as_view()),
    path('hall/<int:pk>', HallView.as_view()),
    path('place/', PlaceViewList.as_view()),
    path('place/<int:pk>', PlaceView.as_view()),
    path('signup/', UserCreate.as_view(), name='account-create'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('profile/', ProfileView.as_view()),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
