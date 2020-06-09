from django.core.exceptions import ObjectDoesNotExist
import datetime

from tuner.models import Iteration, ParamValue, Performance, Model


def create_iteration(config: str) -> Iteration:
    iteration = Iteration(config=config)
    iteration.save()
    return iteration


def get_iteration(iter_id: str) -> Iteration:
    iteration = Iteration.objects.get(pk=iter_id)
    return iteration


def start_iteration(iteration: Iteration) -> None:
    iteration.startedAt = datetime.datetime.now()
    iteration.save()


def create_param_value(param: str, value: str, model: Model) -> ParamValue:
    param = ParamValue(param=param, value=value, model=model)
    param.save()
    return param


def get_values_by_model(model: Model):
    values = ParamValue.objects.filter(model=model)
    return values


def get_performance(iteration: Iteration) -> Performance:
    try:
        performance = Performance.objects.get(iteration=iteration)
        return performance
    except ObjectDoesNotExist:
        return None


def create_model(iteration: Iteration) -> Model:
    model = Model(iteration=iteration)
    model.save()
    return model


def get_models(iteration: Iteration):
    models = Model.objects.filter(iteration=iteration)
    return models
