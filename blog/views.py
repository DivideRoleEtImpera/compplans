from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Plan
from .models import Subject
from .models import Competence
from .models import Subcompetence
from django.db.models import Count
from .forms import PlanForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
	plans = Plan.objects.all()
	subjects = Subject.objects.all()
	return render(request, 'blog/post_list.html', {'plans':plans, 'subjects':subjects})
	
def plan_list(request):
	plans = Plan.objects.all().annotate(number_of_subjects=Count('subject'))
	subjects = Subject.objects.all()
	return render(request, 'blog/plans_list.html', {'plans':plans, 'subjects':subjects})
	
def plan(request,id):
	plan = Plan.objects.get(pk=id)
	subjects = Subject.objects.all()
	return render(request, 'blog/plan.html', {'plan':plan, 'subjects':subjects})


def plan_new(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.author = request.user
            plan.published_date = timezone.now()
            plan.save()
            return redirect('plan', id=plan.pk)
    else:
        form = PlanForm()
    return render(request, 'blog/plan_edit.html', {'form': form})

def plan_edit(request, id):
    plan = Plan.objects.get(pk=id)
    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.author = request.user
            plan.published_date = timezone.now()
            plan.save()
            return redirect('plan', id=plan.pk)
    else:
        form = PlanForm(instance=plan)
    return render(request, 'blog/plan_edit.html', {'form': form})