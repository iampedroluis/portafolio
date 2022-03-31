from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
import time

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html',{'projects':projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_detail.html',{"project": project})

def enviarcorreo(request):
    if request.method == 'POST':
        subject= request.POST['asunto']
        
   
        
        message = "| FULL NAME = " + request.POST['nombre'] +"\n" + "| EMAIL =" + request.POST['correo'] + "\n"  + "| MENSAJE = " + request.POST['mensaje']
        
        email_from = settings.EMAIL_HOST_USER
        
        recipent_list=["pedroluisgutierrez15@gmail.com"]
        
        send_mail(subject, message, email_from, recipent_list)
        
        messages.success(request, ' se ha enviado el mensaje')
        
        return redirect("/gracias")
        

    
    return render(request, 'contacto.html')


def gracias(request):
    
    return render(request, 'gracias.html')