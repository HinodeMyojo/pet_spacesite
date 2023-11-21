from django.shortcuts import render, get_object_or_404

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


def detail(request, pk):
    template_name = 'plans/detail.html'

    plan_detail = get_object_or_404(PlansTitleSpeed.objects.values('id', 'title', 'price', 'option', 'equipment', 'period', 'speed').filter(is_on_main=True),pk=pk)

    context = {
        'plan_detail': plan_detail
    }

    return render(request, template_name, context)
