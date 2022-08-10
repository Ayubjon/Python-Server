from django.http import HttpResponse

def hello_rekruto(request):
    name = request.GET.get('name', "Rekruto")
    message = request.GET.get('message', "Давай дружить")
    rez = "Hello, {}! {}!".format(name, message)
    return HttpResponse(rez)