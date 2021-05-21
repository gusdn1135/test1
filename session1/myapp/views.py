from django.shortcuts import render

# Create your views here.
def home(request):

    # 로직

    return render(request, "home.html")

