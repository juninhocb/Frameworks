from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
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
    service = OfficeService()
    dataFromClient = json.loads(request.body)
    responseFromReadingData = service.read(office_id) 
    oldObject = OfficeSerializerToJson(responseFromReadingData['obj']).data
    if (oldObject == None):
        return JsonResponse(responseFromReadingData, safe= False, status=404)
    oldObject['name'] = dataFromClient.get('name')   
    response = service.update(oldObject)


    return JsonResponse(response, safe=False, status=response['code'])

    

@csrf_exempt
@require_http_methods(['PUT'])
def update_a_person(request, person_id):
    servicePerson = PersonService()
    serviceOffice = OfficeService()
    dataFromClient = json.loads(request.body)
    responseFromReadingDataPerson = servicePerson.read(person_id) 
    responseFromReadingDataOffice = serviceOffice.read(dataFromClient.get('office_id'))
    oldPerson = PersonSerializerToJson(responseFromReadingDataPerson['obj']).data
    oldOffice = OfficeSerializerToJson(responseFromReadingDataOffice['obj']).data

    if (oldPerson == None):
        return JsonResponse(responseFromReadingDataPerson, safe= False, status=404)
    if (oldOffice == None):
        return JsonResponse(responseFromReadingDataOffice, safe= False, status=404)
    
    oldPerson['name'] = dataFromClient.get('name')
    oldPerson['age'] = dataFromClient.get('age')
    oldPerson['isRetired'] = dataFromClient.get('is_retired')
    oldPerson['idOffice'] = dataFromClient.get('office_id')

    response = servicePerson.update(oldPerson)

    return JsonResponse({'status': 'success', 'message': 'Person updated successfully'}, status=response['code'])

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_an_office(request, office_id):
    service = OfficeService()
    officeResponse = service.read(office_id)
    office = officeResponse['obj']
    if (office == None):
        return JsonResponse(officeResponse, safe= False, status=404)
    service.delete(office)
    return JsonResponse({'status': 'success', 'message': 'Office deleted successfully'})

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_a_person(request, person_id):
    service = PersonService()
    personResponse = service.read(person_id)
    person = personResponse['obj']
    if (person == None):
        return JsonResponse(personResponse, safe= False, status=404)
    service.delete(person)
    return JsonResponse({'status': 'success', 'message': 'Person deleted successfully'})