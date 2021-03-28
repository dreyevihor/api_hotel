from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_hotel.auth.views import CreateUserView
from api_hotel.booking.views.tables import BookTableView, TableView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"api/auth/registration", CreateUserView)
router.register(r"api/booking/table", BookTableView)
router.register(r"api/table", TableView)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
