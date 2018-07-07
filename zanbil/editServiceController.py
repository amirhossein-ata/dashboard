from django.shortcuts import render
from khayyam import JalaliDate
from datetime import timedelta
from zanbil.models import Services, Sans, Reserves, Review, Business , TimeTable
from zanbil.views import user

def Render(request, service_id):
        service = Services.objects.get(id=service_id)
        timetable  = TimeTable.objects.get(pk = service.timetable.id)
        lastSans =service.lastSans 
        for i in range(7):
            j = service.firstSans

            while (j <= lastSans):
                sans = Sans.objects.create(start_time = j , end_time=j+1 , time_table=timetable ,weekday = i)
                sans.save()
                j = j+2
        date = JalaliDate.today().__str__().replace('-', '/')
        week_start_date = JalaliDate.today()-timedelta(days=JalaliDate.today().weekday())
        weekday_date=week_start_date
        this_week_days = []
        for i in range(7):
            weekday_date.__str__().replace('-','/')
            this_week_days.append(weekday_date.__str__().replace('-','/'))
            weekday_date = weekday_date + timedelta(1)
        selected_sanses = Sans.objects.filter(time_table=service.timetable.id).order_by('start_time')
        print(len(selected_sanses))
        days = [[],[],[],[],[],[],[]]
        for i in range(7):
            for sans in selected_sanses:
                if sans.weekday == i:
                    days[i].append(sans)
    

        return render(request, 'editServicePage.html',
                      {'service': service, 'days': days, 'date': date,
                       'user': user})