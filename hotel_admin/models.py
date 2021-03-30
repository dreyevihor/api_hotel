from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Table(models.Model):
    capacity = models.IntegerField(default=2)


class Room(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    capacity = models.IntegerField(default=2)


class Dish(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    weight = models.IntegerField()
    description = models.CharField(max_length=1255)


class DishOrder(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    count = models.IntegerField(default=1)


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    destination_time = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish, through=DishOrder)


class RoomService(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination_time = models.DateTimeField()


class TableBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    destination_time = models.DateTimeField()


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField()
