from django.db import models


class Iteration(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    startedAt = models.DateTimeField
    finishedAt = models.DateTimeField


class Param(models.Model):
    param = models.CharField
    config = models.CharField
    iteration = models.ForeignKey(Iteration, on_delete=models.CASCADE)


class Model(models.Model):
    iteration = models.ForeignKey(Iteration, on_delete=models.CASCADE)
    path = models.CharField
    trainStart = models.DateTimeField
    trainEnd = models.DateTimeField


class ParamValue(models.Model):
    param = models.ForeignKey(Param, on_delete=models.CASCADE)
    value = models.CharField
    model = models.ForeignKey(Model, on_delete=models.CASCADE)


class Performance(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    pip = models.CharField
    accuracy = models.CharField
    trainingTime = models.CharField


