from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(Base):
    tag = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tag


class Room(Base):
    room_name = models.CharField(max_length=100)
    room_price = models.IntegerField()
    room_tag = models.ManyToManyField(Tag,related_name='tags')
    room_description = models.TextField()
    room_image = models.ImageField(upload_to='rooms')

    def __str__(self) -> str:
        return self.room_name


class Room_images(Base):
    room = models.ForeignKey(Room , on_delete=models.CASCADE)
    images = models.ImageField(upload_to='rooms')

    def __str__(self) -> str:
        return self.room.room_name