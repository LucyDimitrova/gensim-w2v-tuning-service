from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import random
import itertools

from tuner.services import create_iteration, get_iteration, start_iteration, create_model, get_models, get_performance, create_param_value


class IterationCreateApi(APIView):
    def post(self, request):
        params = request.data.get("params")
        # sort by key
        sorted_params = sorted(params)
        # create unique config string
        config = ";".join(map((lambda key: f'{key}:{params[key]}'), sorted_params))
        try:
            iteration = create_iteration(config)
            # create random sample of 10 values for ranges and list for the values to be used in a cartesian product
            param_values = {key: random.sample(range(params[key][0], params[key][1]), 10) if type(
                eval(params[key])) == list else list(params[key]) for key in sorted_params}
            # find all param combinations
            combinations = itertools.product(param_values.values())
            for combination in combinations:
                model = create_model(iteration)
                for index, value in enumerate(combination):
                    create_param_value(param=sorted_params[index], value=value, model=model)
            return Response({"success": True, "message": "Iteration created.", "iterationId": iteration.id})
        except ValidationError:
            # todo - fetch iteration by config string and return id
            return Response({"success": False, "message": "Iteration with such config already exists."})


class IterationStartApi(APIView):
    def post(self, request, iteration_id):
        try:
            iteration = get_iteration(iteration_id)
            start_iteration(iteration)
            models = get_models(iteration)
            # todo
            # spawn a process for each model
            # update iteration finish time after the last process is done
            return Response({"success": True, "message": "Iteration started successfully."})
        except ObjectDoesNotExist:
            return Response({"success": False, "message": "Iteration with such id does not exist."})


class PerformanceGetApi(APIView):
    def get(self, request, iteration_id):
        iteration = get_iteration(iteration_id)
        performances = get_performance(iteration)
        return Response({"data": "success"})
