from django.db import models


# Create your models here.
class Room(models.Model):
    floors = {
        '1': '1 etaj',
        '2': '2 etaj',
        '3': '3 etaj',
        '4': '4 etaj'
    }

    room_type = {
        '2': '2 kishilik',
        '3': '3 kishilik',
        '4': '4 kishilik',
    }

    room_number = models.CharField(max_length=255, verbose_name='Xona raqami')
    floor = models.CharField(max_length=255, choices=floors.items(), verbose_name='Qavat')
    room_type = models.CharField(max_length=255, choices=room_type.items(), verbose_name='Xona turi')

    def __str__(self):
        return f'{self.room_number} xona {self.room_type} kishilik {self.floor} qavat'

    class Meta:
        verbose_name = 'Xona'
        verbose_name_plural = 'Xonalar'


class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='F.I.SH')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Xona')
    phone = models.CharField(max_length=255, verbose_name='Telefon raqami', null=True, blank=True)
    direction = models.CharField(max_length=255, verbose_name='Yo\'nalish', null=True, blank=True)
    faculty = models.CharField(max_length=255, verbose_name='Fakultet', null=True, blank=True)
    course = models.CharField(max_length=255, verbose_name='Kurs', null=True, blank=True)
    group = models.CharField(max_length=255, verbose_name='Guruh', null=True, blank=True)
    passport = models.CharField(max_length=255, verbose_name='Passport', null=True, blank=True)
    region = models.CharField(max_length=255, verbose_name='Viloyat', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Manzil', null=True, blank=True)
    diseases = models.CharField(max_length=255, verbose_name='Kasalliklar', null=True, blank=True)

    def __str__(self):
        return f"{self.room} dagi {self.full_name} talaba"

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'
