from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from app.models import Room, Student, Payment

# Register your models here.
# change admin site header
admin.site.site_header = 'Yotoqxona adminstrator paneli'
admin.site.site_title = 'Yotoqxona adminstrator paneli'


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'floor', 'room_type', 'students_name')
    list_filter = ('floor', 'room_type')
    search_fields = ('room_number', 'floor', 'room_type')

    def students_name(self, obj):
        students = obj.student_set.all()
        student_links = []

        for student in students:
            change_url = reverse("admin:%s_%s_change" % (student._meta.app_label, student._meta.model_name),
                                 args=[student.id])
            student_link = format_html('<a href="{}">{}</a>', change_url, student.full_name)
            student_links.append(student_link)

        return format_html(", ".join(student_links))

    students_name.short_description = 'Talabalar'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'room', 'phone', 'passport', 'group', 'region', 'address')
    list_filter = ('room__floor', 'room__room_type', 'direction', 'faculty', 'course', 'group', 'region')
    search_fields = (
        'full_name', 'phone', 'direction', 'faculty', 'course', 'group', 'passport', 'region', 'address',
        'diseases', 'room__room_number', 'room__floor', 'room__room_type')

    def save_model(self, request, obj, form, change):
        room = obj.room
        students_in_room = Student.objects.filter(room=room).count()
        max_students_per_room = int(room.room_type)

        if students_in_room >= max_students_per_room:
            message = f"{room.room_number} dagi xona {max_students_per_room} kishilik. {students_in_room} talabalar bor"
            self.message_user(request, message, level='ERROR')
            self.message_user(request, '', level='SUCCESS')
        else:
            super().save_model(request, obj, form, change)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'from_date', 'to_date', 'amount')
    list_filter = ('student__room__room_number', 'student__room__floor', 'student__room__room_type', 'from_date',
                   'to_date', 'student__group', 'student__region', 'student__address')
    search_fields = ('student__full_name', 'from_date', 'to_date', 'amount', 'student__room__room_number',
                     'student__room__floor', 'student__room__room_type', 'student__group', 'student__region',
                     'student__address', 'student__phone', 'student__direction', 'student__faculty', 'student__course',
                     'student__passport', 'student__diseases')
