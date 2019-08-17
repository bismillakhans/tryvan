import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Visitor,Paper

# Register your models here.

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    readonly_fields = ('joined',)
    list_display = ('name', 'phone', 'email', 'organisation', 'joined')
    list_filter = ( 'joined',)

    def download_csv(self, request, queryset):

        f = open('stud.csv', 'w')
        writer = csv.writer(f)
        l = []
        for i in (Visitor._meta.get_fields()):
            l.append(i.name)
        writer.writerow(l)
        data = Visitor.objects.all().values_list()
        for s in data:
            s = list(s)
            writer.writerow(s)
        f.close()
        f = open('stud.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Visitors.csv'
        return response


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    readonly_fields = ('entry',)
    list_display = ('name','lname' ,'phone', 'email', 'organisation', 'department','comments','file_up')
    list_filter = ( 'department','entry')

    def download_csv(self, request, queryset):

        f = open('stud.csv', 'w')
        writer = csv.writer(f)
        l = []
        for i in (Paper._meta.get_fields()):
            l.append(i.name)
        writer.writerow(l)
        data = Paper.objects.all().values_list()
        for s in data:
            s = list(s)
            writer.writerow(s)
        f.close()
        f = open('stud.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Papers.csv'
        return response