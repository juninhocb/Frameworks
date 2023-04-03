from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404
from dao.models import *
from .forms import *

class BaseService:
    model = None
    form_class = None

    def get_form_class(self):
        if not self.form_class:
            self.form_class = modelform_factory(self.model, exclude=[])
        return self.form_class
    
    #TODO method-save on repo

    def create(self, data):
        form_class = self.get_form_class()
        form = form_class(data)
        if form.is_valid():
            form.save()
            return {'status': 'success', 'message': 'Object created successfully', 'code' : 201} 
        else:
            errors = {}
            for field, messages in form.errors.items():
                errors[field] = messages[0]
            return {'status': 'failed', 'message': f'Object was not created. {errors}', 'code' : 400}
        
    def readAll(self):
        objects = self.model.objects.all()
        return list(objects.values())
    
    def read(self, idFromPathVariable): 
        queryset = self.model.objects.filter(id=idFromPathVariable)
        if queryset.exists():
            return {'status': 'success', 'message': 'Object was found', 'code' : 200, 'obj': queryset.first()}
        else:
            return {'status': 'failed', 'message': 'Object was not found', 'code' : 404, 'obj': None}

    def update(self, idFromPathVariable, newObject):
        obj = self.read(idFromPathVariable)
        if (obj['status'] == 'failed'):
            return obj
        
        form_class = self.get_form_class()
        form = form_class(newObject)
        if form.is_valid():
            form.save()
            return {'status': 'success', 'message': 'Object was updated successfully', 'code' : 204} 
        else:
            errors = {}
            for field, messages in form.errors.items():
                errors[field] = messages[0]
            return {'status': 'failed', 'message': f'Object was not updated. {errors}', 'code' : 400}

    


class PersonService(BaseService):
    model = Person
    form_class = PersonForm

class OfficeService(BaseService):
    model = Office
    form_class = OfficeForm