from django.shortcuts import render
from django.http import JsonResponse
import time

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

#api for returning list of posts
def posts(request):

    start = int(request.GET.get("start"))
    end = int(request.GET.get("end"))

    data = []

    #call from javascript always give 1 to 20, we have
    #to change to 21 to really get twenty posts
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    #simulate loading time
    time.sleep(1)

    return JsonResponse({
        "posts": data
    })
    