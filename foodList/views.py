from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import food
from django.contrib import messages
from django.core.exceptions import PermissionDenied

#form handler for posting to the databse and a function to check the count of food objects in database
def foodView(request):
    if food.objects.count() >= 10:
        raise PermissionDenied
    new_food = food(listoffood = request.POST['val'])
    new_food.save()
    messages.success(request, 'successfully added')
    return HttpResponseRedirect('/')

#function that displays food objects
def allFood(request):
    allofFood = food.objects.all()
    context = {'foodies': allofFood}
    return render(request, 'foodList/index.html', context)

#function that deletes food objects
def deleteFood(request, id):
    foodDel = food.objects.get(pk = id)
    foodDel.delete()
    return redirect('allFood')









