from django.http import JsonResponse
from dao.serializers import *
import json


class ErrorHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        case_handlers = {
            400: "Bad request, please check your content.",
            404: "Resource not found.",
            415: "Method not allowed."
        }

        try:
            response = self.get_response(request)
            status_code = response.status_code
            response_byte_to_string = response.content.decode('utf-8')  
            response_json_to_object = json.loads(response_byte_to_string)
            message = response_json_to_object['message']
            if status_code not in [200, 201, 204]:
                error_message = case_handlers.get(status_code)
                if (error_message == None):
                    status_code = 500
                    error_message = "A problem not expected was occoured with server."

                response_data = {
                    'error_message': f"{error_message} Err: {message}",
                }
                return JsonResponse(response_data, status=status_code)
            return response
        except Exception as e:
            error_message = str(e)
            status_code = 500
            response_data = {
                'error_message': f'Error on handling message: {error_message}',
            }
            return JsonResponse(response_data, status=status_code)
