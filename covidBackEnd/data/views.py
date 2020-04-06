from rest_framework import generics
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

import requests


class GetDataLast7Days(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        response = requests.get("https://us-central1-virtual-bonito-170805.cloudfunctions.net/covidCaseTrends")
        if response.status_code == 200:
            data = response.json()
            response_data = {"results": []}
            for i in range(6, -1, -1):
                day = ""
                confirmed = -1
                tested = -1
                discarded = -1
                recovered = -1
                treatment = -1
                deceased = -1
                if 0 <= i < len(data["labels"]):
                    day = data["labels"][i]
                if data['datasets']:
                    if data['datasets'][0]['data'] and 0 <= i < len(data['datasets'][0]['data']):
                        tested = data['datasets'][0]['data'][i]
                    if data['datasets'][1]['data'] and 0 <= i < len(data['datasets'][1]['data']):
                        discarded = data['datasets'][1]['data'][i]
                    if data['datasets'][2]['data'] and 0 <= i < len(data['datasets'][2]['data']):
                        confirmed = data['datasets'][2]['data'][i]
                    if data['datasets'][3]['data'] and 0 <= i < len(data['datasets'][3]['data']):
                        recovered = data['datasets'][3]['data'][i]
                    if data['datasets'][4]['data'] and 0 <= i < len(data['datasets'][4]['data']):
                        treatment = data['datasets'][4]['data'][i]
                    if data['datasets'][5]['data'] and 0 <= i < len(data['datasets'][5]['data']):
                        deceased = data['datasets'][5]['data'][i]
                response_data["results"].append({"day": day,
                                                 "tested": tested,
                                                 "discarded": discarded,
                                                 "confirmed": confirmed,
                                                 "recovered": recovered,
                                                 "treatment": treatment,
                                                 "deceased": deceased,
                                                 })
            return Response(response_data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class GetDataSummary(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        response = requests.get("https://us-central1-virtual-bonito-170805.cloudfunctions.net/covidSummary")
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=status.HTTP_404_NOT_FOUND)


class GetDataLocations(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        response = requests.get("https://us-central1-virtual-bonito-170805.cloudfunctions.net/covidLocations")
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=status.HTTP_404_NOT_FOUND)


class GetDataLocationsTrends(APIView):
    permission_classes = ()

    def get(self, request, format=None):
        response = requests.get("https://us-central1-virtual-bonito-170805.cloudfunctions.net/covidRegionalTrends")
        if response.status_code == 200:
            data = response.json()
            response_data = {"results": []}
            for i in range(6, -1, -1):
                day = ""
                if 0 <= i < len(data["labels"]):
                    day = data["labels"][i]
                data_regions = []
                for region in data["datasets"]:
                    number = -1
                    if region["data"][i]:
                        number = region["data"][i]
                    data_regions.append({"name": region["label"], "cases": number})
                response_data["results"].append({"day": day,
                                                 "results": data_regions
                                                 })
            return Response(response_data)
        return Response(status=status.HTTP_404_NOT_FOUND)
