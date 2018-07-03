from django.shortcuts import render

from zanbil.models import Business, Categories
from zanbil.views import user, categories


class BusinessSelectPage:
    def Render(request, category_id):
        category_Businesses = Business.objects.filter(category_id=category_id).order_by('-score')
        category_name = Categories.objects.get(pk=category_id).name
        return render(request, 'BusinessSelectPage.html',
                      {'category_name': category_name, 'category_businesses': category_Businesses,
                       'categories': categories, 'user': user})
