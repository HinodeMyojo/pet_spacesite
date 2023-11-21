from django.shortcuts import render

from .models import PlansTitleSpeed

def index(request):
    template_name = 'plans/plans.html'

    plan_list = PlansTitleSpeed.objects.values(
        'id', 'title', 'price', 'option', 'equipment',
        'period', 'speed'
        ).filter(is_on_main=True)

    context = {
        'plan_list': plan_list
}

    return render(request, template_name, context)
