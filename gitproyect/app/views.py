from django.shortcuts import render,HttpResponse,redirect
from app.models import Movie
from django.views.decorators.csrf import csrf_exempt,requires_csrf_token

@csrf_exempt
@requires_csrf_token
def index(request):
	if request.method == "POST":
		print(1)
		a = Movie(title = "Divide", description = "Ed Sheeran", release_date = "2012-12-12" , duration = 20)
		a.save()
		return redirect("/request")

	return HttpResponse("Hola Mundo!! :)")
