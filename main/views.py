from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactMessage
def index(request):
    return render(request, 'index.html')


def submit_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"})

