from django.shortcuts import render


def home(request):
    context = {
        "message": "Welcome to the Waypoint homepage."
    }
    return render(request, "home.html", context)


def report(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        trail = request.POST.get("trail", "")
        note = request.POST.get("note", "")

        context = {
            "name": name,
            "email": email,
            "trail": trail,
            "note": note,
        }
        return render(request, "thank_you.html", context)

    return render(request, "report.html")


def search(request):
    query = request.GET.get("q", "")
    context = {
        "query": query
    }
    return render(request, "search.html", context)


def catalog(request):
    trails = [
        {"name": "Bruce Trail", "distance": 12.4, "elevation": 320, "difficulty": "easy", "is_open": True},
        {"name": "Rattlesnake Point", "distance": 8.7, "elevation": 210, "difficulty": "moderate", "is_open": True},
        {"name": "Dundas Peak", "distance": 6.2, "elevation": 180, "difficulty": "expert", "is_open": False},
        {"name": "Kelso Loop", "distance": 10.5, "elevation": 260, "difficulty": "moderate", "is_open": True},
        {"name": "Mono Cliffs", "distance": 14.1, "elevation": 400, "difficulty": "expert", "is_open": True},
        {"name": "Hilton Falls", "distance": 5.9, "elevation": 120, "difficulty": "easy", "is_open": False},
    ]

    context = {
        "trails": trails
    }
    return render(request, "catalog.html", context)