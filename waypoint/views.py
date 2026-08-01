from django.shortcuts import render


def home(request):
    context = {
        "greeting": "Welcome to Waypoint"
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
    q = request.GET.get("q", "")
    context = {
        "query": q
    }
    return render(request, "search.html", context)