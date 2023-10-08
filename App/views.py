from App.models import Candidate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# (C) Create
class Create(SuccessMessageMixin, CreateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')
    success_message = "Candidate: %(name)s created successfully !"

# (R) Read
class Read(ListView):
    model = Candidate
    queryset = Candidate.objects.all()

# (U) Upate
class Update(SuccessMessageMixin, UpdateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')
    success_message = "Candidate: %(name)s update successfully !"

# (D) Delete
class Delete(DeleteView):
    model = Candidate
    def get_success_url(self):
        messages.success(self.request, "Candidate deleted successfully !")
        return reverse("read")
