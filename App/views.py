from App.models import Candidate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# (C) Create
class Create(CreateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')

# (R) Read
class Read(ListView):
    model = Candidate
    queryset = Candidate.objects.all()

# (U) Upate
class Update(UpdateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')

# (D) Delete
class Delete(DeleteView):
    queryset = Candidate.objects.all()
    success_url = reverse_lazy('read')
