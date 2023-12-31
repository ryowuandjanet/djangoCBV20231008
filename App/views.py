from typing import Any
from django.db.models.query import QuerySet
from App.models import Candidate
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q

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
    paginate_by = 3
    def get_queryset(self):
        q = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by')  # Get the sort parameter from the URL

        if q:
            object_list = self.model.objects.filter(
                Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) |
                Q(gender__icontains=q) | Q(career__icontains=q)
            )
        else:
            object_list = self.model.objects.all()

        # Add sorting logic based on 'sort_by' parameter
        if sort_by == 'name_asc':
            object_list = object_list.order_by('name')
        elif sort_by == 'name_desc':
            object_list = object_list.order_by('-name')

        return object_list

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
