from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import *
from .services import *
from dao.models import *
from dao.serializers import *

import json

@require_http_methods(['GET'])
def hello_world(request):
    return JsonResponse({'message': 'Hello world!'})

@csrf_exempt
@require_http_methods(['POST'])
def create_office(request):

    dataFromClient = json.loads(request.body)
    service = OfficeService()
    response = service.create(dataFromClient)
    return JsonResponse(response, status=response['code']) 

@csrf_exempt
@require_http_methods(['POST'])
def create_person(request):

    dataFromClient = json.loads(request.body)
    service = PersonService()
    response = service.create(dataFromClient)
    return JsonResponse(response, status=response['code'])  


@require_http_methods(['GET'])
def read_all_offices(request):
    service = OfficeService()
    offices = service.readAll()
    return JsonResponse({'message': 'query succesful', 'offices': offices}, safe=False)

@require_http_methods(['GET'])
def read_an_office(request, office_id):
    service = OfficeService()
    office = service.read(office_id)
    serialized_office = OfficeSerializerToJson(office['obj']).data
    office['obj'] = serialized_office
    return JsonResponse(office, safe=False)

@require_http_methods(['GET'])
def read_all_persons(request):
    service = PersonService()
    people = service.readAll()
    return JsonResponse({'message': 'query succesful', 'people': people}, safe=False)

@require_http_methods(['GET'])
def read_a_person(request, person_id):
    service = PersonService()
    person = service.read(person_id)
    serialized_person = PersonSerializerToJson(person['obj']).data
    person['obj'] = serialized_person
    return JsonResponse(person, safe=False)

@csrf_exempt
@require_http_methods(['PUT'])
def update_an_office(request, office_id):
    dataFromClient = json.loads(request.body)
    service = OfficeService()
    return JsonResponse(service.update(office_id, dataFromClient), safe=False)

    

@csrf_exempt
@require_http_methods(['PUT'])
def update_a_person(request, person_id):

    old_person = get_object_or_404(Person, id=person_id)

    dataFromClient = json.loads(request.body)

    nameFromRequest = dataFromClient.get('name')
    ageFromRequest = dataFromClient.get('age')
    is_retiredFromRequest = dataFromClient.get('is_retired')
    office_idFromRequest = dataFromClient.get('office_id')
    office = get_object_or_404(Office, id=office_idFromRequest)

    old_person.name = nameFromRequest
    old_person.age = ageFromRequest
    old_person.isRetired = is_retiredFromRequest
    old_person.idOffice = office

    old_person.save()

    return JsonResponse({'status': 'success', 'message': 'Person updated successfully'})

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_an_office(request, office_id):
    office = get_object_or_404(Office, id=office_id)
    office.delete()
    return JsonResponse({'status': 'success', 'message': 'Office deleted successfully'})

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_a_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return JsonResponse({'status': 'success', 'message': 'Person deleted successfully'})