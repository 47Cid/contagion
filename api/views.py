from django.http import JsonResponse
from .models import User, TravelRecord, InfectionRecord, Location
import json
from django.utils import timezone
from .update import updateRecords


def listUsers(request):
    users = User.objects.all()
    resp_data = [{"username": q.username,
                  "infection_probability": q.infection_probability,
                  "creation_date": q.creation_date.strftime("%B-%d-%Y")}
                 for q in users]
    return JsonResponse(resp_data, safe=False)


def userData(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'status_code': 404,
            'error': 'User does not exist'
        })
    return JsonResponse(
        {"username": user.username,
         "infection_probability": user.infection_probability,
         "creation_date": user.creation_date.strftime("%B-%d-%Y")},
        safe=False)


def addUser(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        user = User(
            username=req["username"],
            infection_probability=req["infection_probability"],
            creation_date=timezone.now())
        user.save()
        return JsonResponse({"user_id": user.id}, safe=False)
    else:
        return JsonResponse({
            'status_code': 404,
            'error': 'Post method was expected'
        })


def deleteUser(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'status_code': 404,
            'error': 'User does not exist'
        })
    id = user.id
    user.delete()
    return JsonResponse({"user_id": id}, safe=False)


def addTravelRecord(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            usr = User.objects.get(pk=req["user_id"])
        except User.DoesNotExist:
            return JsonResponse({
                'status_code': 404,
                'error': 'User does not exist'
            })
        try:
            location = Location.objects.get(pk=req["location_id"])
        except Location.DoesNotExist:
            return JsonResponse({
                'status_code': 404,
                'error': 'Location does not exist'
            })
        record = TravelRecord(
            location=location,
            arrived_at=req["arrived_at"],
            user=usr)
        record.save()
        return JsonResponse({"travel_record_id": record.id}, safe=False)
    else:
        return JsonResponse({
            'status_code': 404,
            'error': 'Post method was expected'
        })


def addInfectionRecord(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        try:
            usr = User.objects.get(pk=req["user_id"])
        except User.DoesNotExist:
            return JsonResponse({
                'status_code': 404,
                'error': 'User does not exist'
            })
        record = InfectionRecord(
            infected_at=req["infected_at"],
            user=usr)
        record.save()
        updateRecords(record.id)
        return JsonResponse({"infection_record_id": record.id}, safe=False)
    else:
        return JsonResponse({
            'status_code': 404,
            'error': 'Post method was expected'
        })


def deleteTravelRecord(request, travel_id):
    try:
        record = TravelRecord.objects.get(pk=travel_id)
    except TravelRecord.DoesNotExist:
        return JsonResponse({
            'status_code': 404,
            'error': 'Travel record does not exist'
        })
    id = record.id
    record.delete()
    return JsonResponse({"travel_record_id": id}, safe=False)


def deleteInfectionRecord(request, infection_id):
    try:
        record = InfectionRecord.objects.get(pk=infection_id)
    except InfectionRecord.DoesNotExist:
        return JsonResponse({
            'status_code': 404,
            'error': 'Infection record does not exist'
        })
    id = record.id
    record.delete()
    return JsonResponse({"infection_record_id": id}, safe=False)
