from django.core.exceptions import ObjectDoesNotExist

from tuner.models import Iteration, Param, Performance


def create_iteration(config: str) -> Iteration:
    iteration = Iteration(config=config)
    iteration.save()
    return iteration


def get_iteration(iter_id: str) -> Iteration or None:
    try:
        iteration = Iteration.objects.get(pk=iter_id)
        return iteration
    except ObjectDoesNotExist:
        return None


def create_param(name: str, value: str, iteration: Iteration) -> Param:
    param = Param(param=name, config=value, iteration=iteration)
    param.save()
    return param


def get_performance(iteration: Iteration) -> Performance:
    try:
        performance = Performance.objects.get(iteration=iteration)
        return performance
    except ObjectDoesNotExist:
        return None

