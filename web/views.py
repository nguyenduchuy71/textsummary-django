from django.shortcuts import render
from django.views import generic
from .forms import FileForm
from .utils import handle_uploaded_file
# Create your views here.


def index(request):
    file_form = FileForm()
    return render(request, 'web/index.html', {"form": file_form})


class SummaryView(generic.View):
    template_name = 'web/index.html'
    context_object_name = 'summary'

    def post(self, request):
        file_form = FileForm()
        text = request.POST['text']
        return render(request, 'web/index.html', {"text": text, "summary": text, "form": file_form})


class ViewUploadFile(generic.View):
    template_name = 'web/index.html'
    context_object_name = 'summary'

    def post(self, request):
        content_file = None
        file = FileForm(request.POST, request.FILES)
        if file.is_valid():
            content_file = handle_uploaded_file(request.FILES['file'])
        return render(request, 'web/index.html', {"text": content_file, "summary": content_file, "form": file})
