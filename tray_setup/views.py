from django.shortcuts import render

# Create your views here.

def main_tray_view(request):
    return render(request, "tray_setup/main_tray.html")
