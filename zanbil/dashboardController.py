from django.shortcuts import render
from datetime import timedelta
from .models import Categories, Services, Reserves, Review, Business, Sans, Users
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
