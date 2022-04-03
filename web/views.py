from django.shortcuts import render
from django.views import generic
from .forms import FileForm
from .utils import handle_uploaded_file
import tensorflow as tf
from transformers import AutoTokenizer
# Create your views here.
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)
reloaded = tf.saved_model.load('web/static/model')

def index(request):
    file_form = FileForm()
    return render(request, 'web/index.html', {"form": file_form})


class SummaryView(generic.View):
    template_name = 'web/index.html'
    context_object_name = 'summary'

    def post(self, request):
        file_form = FileForm()
        text = request.POST['text']
        example = tokenizer.encode(text, max_length = 1000,truncation="longest_first", padding = 'max_length')
        example = tf.convert_to_tensor([example], dtype=tf.int64)
        summary = tokenizer.decode(reloaded(example)[0])[4:-4]
        return render(request, 'web/index.html', {"text": text, "summary": summary, "form": file_form})


class ViewUploadFile(generic.View):
    template_name = 'web/index.html'
    context_object_name = 'summary'

    def post(self, request):
        content_file = None
        file = FileForm(request.POST, request.FILES)
        if file.is_valid():
            content_file = handle_uploaded_file(request.FILES['file'])
        return render(request, 'web/index.html', {"text": content_file, "summary": content_file, "form": file})
