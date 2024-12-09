from rest_framework import serializers
from .models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age', 'city']


def get_validation_failure_response(errors, error_message="Invalid Params", status_code=0, message_duration='S'):
    print(errors)
    res = {}
    res["success"] = False
    res["status"] = "Bad Request"
    
    res["status_code"] = status_code
    res["message_duration"] = message_duration
    
    res["error_message"] = error_message
    if errors != None:
        pass
    return res

def get_success_response(message=None, status=None, details=None):
    
    if status == None:
        status = "Request processed Successfully"
    res = {}
    res["success"] = True
    res["status"] = status
    res["message"] = message
    if details != None:
        res["details"] = details
    return res
