from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "No Unnecessary Purchases",
    "february": "Cold Shower Every Day",
    "march": "No Social Media",
    "april": "Read for 30 Minutes Each Day",
    "may": "No Snooze Button",
    "june": "One Act of Kindness Per Day",
    "july": "Drink 1 Gallon of Water Everyday",
    "august": "30 Minutes of Exercise Each Day",
    "september": "Run 30 Miles in 30 Days",
    "october": "No Sweets",
    "november": "Things Im Proud Of",
    "december": None
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())


    return render(request,"challenge/index.html",{"months": months})

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenge/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
