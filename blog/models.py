from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Plan(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=20) 
    program_name = models.CharField(max_length=200, null=True)
    program_sub_name = models.CharField(max_length=200, null=True)
    program_leader = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=4, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    effective_till = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.code+" Направление подготовки:"+self.program_name+" ("+self.year+", "+self.program_leader+")"

class Subject(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=20) 
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    effective_till = models.DateTimeField(blank=True, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.code+" "+self.name

class Competence(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=20) 
    name = models.CharField(max_length=200)
    description = models.TextField()
    plan = models.ManyToManyField(Plan)
    subject = models.ManyToManyField(Subject)
    

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return self.code+" "+self.name

class Subcompetence(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=20) 
    name = models.CharField(max_length=200)
    description = models.TextField()
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return self.code+" "+self.name
