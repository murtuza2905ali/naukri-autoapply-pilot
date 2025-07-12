import json
from django.shortcuts import render
from django.http import JsonResponse
import subprocess
from pathlib import Path

# Load suggestions once at startup (unchanged)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "jobapply" / "static" / "jobapply" / "data" / "suggestions.json"
with open(DATA_FILE, encoding="utf-8") as f:
    SUGGESTIONS = json.load(f)

def index(request):
    # Handle POST request from the unified form
    if request.method == "POST":
        # Get email, password, job title, and location from form data
        email = request.POST.get("email")
        password = request.POST.get("password")
        job_title = request.POST.get("job_title")
        location = request.POST.get("location")

        # Launch the apply_jobs.py script with all four arguments
        subprocess.Popen([
            "python", "playwright/apply_jobs.py", job_title, location, email, password
        ])

        return render(request, "jobapply/index.html", {"message": "Launched!"})

    # On GET, just render the page normally
    return render(request, "jobapply/index.html")

def suggest_titles(request):
    q = request.GET.get("q", "").lower()
    matches = []
    if q:
        for title in SUGGESTIONS.get("job_titles", []):
            if q in title.lower():
                matches.append(title)
    return JsonResponse({"suggestions": matches})

def suggest_locations(request):
    q = request.GET.get("q", "").lower()
    matches = []
    if q:
        for loc in SUGGESTIONS.get("locations", []):
            if q in loc.lower():
                matches.append(loc)
    return JsonResponse({"suggestions": matches})
