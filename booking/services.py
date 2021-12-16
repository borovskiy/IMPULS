from django.contrib import messages
from django.db.models import Q

from .models import ReservedPlace


def check_free_place_and_number_reserved_places(request, form, id_object=None):
    if form.date_start_parking > form.date_finish_parking:
        messages.add_message(request, messages.INFO, 'Дата старта брони должна быть раньше чем конечная дата')
        return False

    elif len(ReservedPlace.objects.filter(user=request.user)) > 2:
        messages.add_message(request, messages.INFO, 'У вас уже лимит на бронирование мест')
        return False

    parking = ReservedPlace.objects.filter(parking_space=form.parking_space)
    if id_object:
        parking = parking.exclude(id=id_object)
    if bool(parking.filter(
            Q(date_finish_parking__range=(form.date_start_parking, form.date_finish_parking)) &
            Q(date_start_parking__range=(form.date_start_parking, form.date_finish_parking)))):
        messages.add_message(request, messages.INFO, 'В этом диапазоне дат уже есть забронированые места1')
        return False
    elif bool(parking.filter(
            Q(date_finish_parking__gte=form.date_start_parking) &
            Q(date_start_parking__lte=form.date_finish_parking))):
        messages.add_message(request, messages.INFO, 'В этом диапазоне дат уже есть забронированые места2')
        return False
    return True
