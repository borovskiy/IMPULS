from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import ReservedPlace
from .forms import FormBooking
from .services import check_free_place_and_number_reserved_places


class ListParkingSpace(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('login')
    model = ReservedPlace
    context_object_name = 'parking'
    template_name = 'list_booking.html'

    def get_queryset(self):
        return ReservedPlace.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        if self.request.user.is_superuser:
            context['all_booking_admin'] = ReservedPlace.objects.all()
        return context


class CreatingBooking(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('list_booking')
    model = ReservedPlace
    form_class = FormBooking
    template_name = 'add_booking.html'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        if check_free_place_and_number_reserved_places(self.request, form):
            form.save()
            return redirect(reverse_lazy('list_booking'))
        return redirect(reverse_lazy('add_booking'))


class UpdateBooking(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('list_booking')
    model = ReservedPlace
    form_class = FormBooking
    template_name = 'update_booking.html'
    success_url = reverse_lazy('list_booking')

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.date_start_parking = obj.date_start_parking.strftime('%Y-%m-%dT%H:%M')
        obj.date_finish_parking = obj.date_finish_parking.strftime('%Y-%m-%dT%H:%M')
        return obj

    def form_valid(self, form):
        form = form.save(commit=False)
        if check_free_place_and_number_reserved_places(self.request, form, id_object=form.id):
            form.save()
            return redirect(reverse_lazy('list_booking'))
        return redirect(reverse_lazy('update_booking', kwargs={'pk': self.object.pk}))


class DeleteBooking(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('list_booking')
    model = ReservedPlace
    template_name = 'delete_booking.html'
    success_url = reverse_lazy('list_booking')
