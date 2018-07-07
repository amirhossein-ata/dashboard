from django.shortcuts import render
from datetime import timedelta
from .models import Categories, Services, Reserves, Review, Business, Sans, Users , TimeTable
from .forms import serviceForm
from django.shortcuts import redirect
from khayyam import *

# Create your views here.

categories = Categories.objects.all()
user = Users.objects.get(id=1)

def dashboard(request , business_id):
        business = Business.objects.get(id=business_id)
        services = Services.objects.filter(business__id=business_id)
        reviews = Review.objects.filter(business=business_id)
        reserves=[]
        date = JalaliDate.today().__str__().replace('-', '/')
        week_start_date = JalaliDate.today()-timedelta(days=JalaliDate.today().weekday())
        weekday_date=week_start_date
        this_week_days = []
        for i in range(7):
            weekday_date.__str__().replace('-','/')
            this_week_days.append(weekday_date.__str__().replace('-','/'))
            weekday_date = weekday_date + timedelta(1)

        reserves = []
        for date in this_week_days:
            reserves.append(len(Reserves.objects.filter(date = date)))
        
        total_count = sum(reserves)

        listed_reviews = []
        i = 0
        while i < len(reviews):
            if i % 3 == 0:
                if i + 2 < len(reviews):
                    listed_reviews.append([reviews[i], reviews[i + 1], reviews[i + 2]])
                    i += 3
                elif i + 1 < len(reviews):
                    listed_reviews.append([reviews[i], reviews[i + 1]])
                    i += 2
                else:
                    listed_reviews.append([reviews[i]])
                    i += 1
        categories = Categories.objects.all()
        
        return render(request , 'dashboard.html',{'business': business, 'services': services,
         'reviews': reviews, 'user': user,'categories':categories ,'dates':this_week_days , 'reserves_count' : reserves , 'total_reserves_count': total_count})

def addService(request , business_id):
    business = Business.objects.get(pk=business_id)
    timetable = TimeTable.objects.create(sans_count=10 , work_days=[0],rest_times=[1])
    # for i in range(7):
    #     j = 7
    #     while (j <= 20):
    #         sans = Sans.objects.create(start_time = j , end_time=j+1 , time_table=timetable ,weekday = i)
    #         j = j+2
    if request.method == 'POST':
    
        print('method is post')
        name = request.POST['ServiceName']
        description = request.POST['Description']
        fee = request.POST['Fee']
        capacity = request.POST['Capacity']
        print(name)
        print(description)
        print(fee)
        print(capacity)
        service = Services.objects.create(name=name,description=description,fee=fee,capacity=capacity,business = business,timetable =timetable)
        service.save()
        return redirect('editServicePage', service.id)

    return render(request, 'addServiceForm.html', {'business_id':business_id})



