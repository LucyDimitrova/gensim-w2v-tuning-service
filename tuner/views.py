from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from tuner.services import create_iteration, get_iteration, create_param, get_performance


class IterationCreateApi(APIView):
    def post(self, request):
        params = request.data.get("params")
        # sort by key
        sorted_params = sorted(params.keys())
        # create unique config string
        config = ";".join(map((lambda key: f'{key}:{params[key]}'), sorted_params))
        try:
            iteration = create_iteration(config)
            # normalize and save config data
            for param in params:
                create_param(param, params[param], iteration)
            return Response({"success": True, "message": "Iteration created.", "iterationId": iteration.id})
        except ValidationError:
            # todo - fetch iteration by config string
            return Response({"success": False, "message": "Iteration with such config already exists."})


class IterationStartApi(APIView):
    def post(self, request):
        pass


class PerformanceGetApi(APIView):
    def get(self, request):
        iteration_id = request.get("iteration_id")
        iteration = get_iteration(iteration_id)
        performances = get_performance(iteration)
        return Response({"data": "success"})
