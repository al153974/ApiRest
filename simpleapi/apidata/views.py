from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import TemplateView
import pandas as pd 
import io

class DataViewSet(viewsets.ModelViewSet):
    serializer_class = DataSerializers
    queryset = Data.objects.all()

class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'

    def post(self, request):
        context = {
            'messages':[]
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )

        for record in csv_data.to_dict(orient="records"):
            try:
                Data.objects.create(
                        title = record['title'],
                        location = record['location'],
                        estado = record['estado'],
                        company = record['company'],
                        salary = record['salary'],
                        description = record['description'],
                        tskills = record['tskills'],
                        sskills = record['sskills']
                )
            except Exception as e: 
                context['exceptions_raised'] = e # type: ignore
        
        return render(request, self.template_name, context)