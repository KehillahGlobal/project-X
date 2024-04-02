from django.shortcuts import render


# Test endpoint
def home(request):
    return render(request, "pages/homepage.html")
