from django.shortcuts import render,get_object_or_404
from rest_framework.views import  APIView
from.models import *
import csv
import io
import base64
from rest_framework.response import Response
from rest_framework import status
from .model_helper import *
from .response_serializers import *


def ListBlog(request):
    obj=Myblog.objects.all()
    return render(request,"list.html",{"list":obj})

def DetailBlog(request,id):
    obj=get_object_or_404 (Myblog,id=id)
    return render(request,"detail.html",{"detail":obj})

def item_list(request):
    obj=Item.objects.all()
    return render(request,"list.html",{"obj":obj})

def item_detail(request,id):
    obj=get_object_or_404 (Item,id=id)
    return render(request,"detail.html",{"obj":obj})

class UploadCSV(APIView):
    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            return Response({'error': 'File is not CSV type'}, status=status.HTTP_400_BAD_REQUEST)

     
        try:
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.DictReader(io_string)

            persons = []
            for row in reader:
                serializer = PersonSerializer(data=row)
                if serializer.is_valid():
                    persons.append(serializer.save())
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'success': f'Uploaded {len(persons)} records.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class BulkUploadPerson(APIView):
    def post(self, request):
        data = request.data
        

        if 'csv_data' not in data:
            return Response({"error": "csv_data is required"}, status=400)

        csv_data = base64.b64decode(data['csv_data']).decode('utf-8')
        csv_file = io.StringIO(csv_data)

        is_first = True
        carray = list(csv.reader(csv_file))

        for row in carray:
            if is_first:
                is_first = False
                continue  

            try:
                
                name = row[0]
                age = row[1]
                city = row[2]

                if not check_if_empty(data=name):
                    raise ValueError("Name cannot be empty")

                if not age.isdigit() or int(age) < 0:
                    raise ValueError(f"Invalid age: {age}. Age must be a non-negative integer")

                if not check_if_empty(data=city):
                    raise ValueError("City cannot be empty")

            except Exception as error:
                return Response(get_validation_failure_response(None, error_message=str(error)), status=400)

        
        csv_file.seek(0)
        is_first = True

        for row in carray:
            if is_first:
                is_first = False
                continue  

            try:
                name = row[0]
                age = row[1]
                city = row[2]

                Person.objects.create(name = name,
                                      age = age,
                                      city = city)

            except Exception as error:
                return Response(get_validation_failure_response(None, error_message=str(error)), status=400)

        return Response(get_success_response("Persons' details uploaded successfully"))



