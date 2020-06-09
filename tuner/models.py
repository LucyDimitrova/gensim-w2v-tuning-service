from django.db import models


class Iteration(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    startedAt = models.DateTimeField(null=True)
    finishedAt = models.DateTimeField(null=True)
    config = models.TextField(unique=True)

    def save(self, *args, **kwargs):
        self.validate_unique()
        return super().save(*args, **kwargs)


class Param(models.Model):
    param = models.CharField(max_length=100)
    config = models.CharField(max_length=100)
    iteration = models.ForeignKey(Iteration, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["param", "iteration"]

    def save(self, *args, **kwargs):
        self.validate_unique()
        return super().save(*args, **kwargs)


class Model(models.Model):
    iteration = models.ForeignKey(Iteration, on_delete=models.CASCADE)
    path = models.TextField(null=True)
    trainStart = models.DateTimeField(null=True)
    trainEnd = models.DateTimeField(null=True)


class ParamValue(models.Model):
    param = models.ForeignKey(Param, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)


class Performance(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    pip = models.CharField(max_length=100)
    accuracy = models.CharField(max_length=100)
    trainingTime = models.CharField(max_length=100)


