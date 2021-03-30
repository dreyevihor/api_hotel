from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_hotel.auth.views import CreateUserView
from api_hotel.booking.views.tables import BookTableView, TableView
from api_hotel.booking.views.dishes import DishView, OrderView
from api_hotel.booking.views.services import RoomServiceView
from api_hotel.booking.views.news import NewsView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"api/auth/registration", CreateUserView)
router.register(r"api/booking/table", BookTableView)
router.register(r"api/tables", TableView)
router.register(r"api/orders", OrderView)
router.register(r"api/dishes", DishView)
router.register(r"api/news", NewsView)
router.register(r"api/rooms/service", RoomServiceView)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
