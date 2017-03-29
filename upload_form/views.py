from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from upload_form.models import FileNameModel
import sys,os
from upload_form.kerasvgg16 import image_recog
UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def form(request):
    if request.method != 'POST':
        return render(request, 'upload_form/form.html')

    file = request.FILES['file']
    path = os.path.join(UPLOAD_DIR, file.name)
    destination = open(path,'wb')
    results = image_recog(file)
    results = {'results': results}
    print(results)
    for chunk in file.chunks():
        destination.write(chunk)
    insert_data = FileNameModel(file_name = file.name)
    insert_data.save()

    return render(request,'upload_form/complete.html',results)

def complete(request):
    return render(request, 'upload_form/complete.html',results)


