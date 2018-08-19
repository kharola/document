from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from .models import FileSys
from .forms import FileSysForms

# Create your views here.

@login_required
def filelist(request):
    files = FileSys.objects.all()
    return render(request,'files_sys/list.html',{'files':files})

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = FileSysForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files_sys:list')
    else:
        form = FileSysForms()
    return render(request, 'files_sys/model_form_upload.html', {
        'form': form
    })

@login_required
def delete_file(request,pk=None):
    file = get_object_or_404(FileSys, pk=pk)
    file.delete()
    return redirect('files_sys:list')

@login_required
def file_list(request):
    MAX_OBJECTS = 20
    fl = FileSys.objects.all()
    data = {"results": list(fl.values("title", "document", "uploaded_at"))}
    return JsonResponse(data)
