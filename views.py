from django.shortcuts import render
from .models import JobListening
# Create your views here.
def home(request):
    alljobs = JobListening.objects.all()
    context = {"jobs": alljobs}
    if request.method == "POST":
        posted_title = request.POST.get("title", "")   # title is from the index.html page's name property
        posted_description = request.POST.get("description", "") # description is from the index.html page's name property

        job_listing = JobListening.objects.create(
            title = posted_title,
            description = posted_description
        )
        job_listing.save()

        return render(request, "jobs_app/index.html", context)

    return render(request, "jobs_app/index.html", context)
