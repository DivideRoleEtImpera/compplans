from django.contrib import admin
from .models import Post
from .models import Plan
from .models import Subject
from .models import Competence
from .models import Subcompetence

admin.site.register(Post)
admin.site.register(Plan)
admin.site.register(Subject)
admin.site.register(Competence)
admin.site.register(Subcompetence)
