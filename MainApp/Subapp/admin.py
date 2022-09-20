from django.contrib import admin
from Subapp.models import Admission
from Subapp.models import Contact,Course,Campus,Team,Testimonials
# Register your models here.
admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Campus)
admin.site.register(Admission)
admin.site.register(Team)
admin.site.register(Testimonials)
