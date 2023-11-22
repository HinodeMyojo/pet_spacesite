from django.shortcuts import render, get_object_or_404

from .models import PlansTitleSpeed


def index(request):
    """
    Renders the index view for the plans.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    # Define the template name
    template_name = 'plans/plans.html'

    # Retrieve the plan list from the database
    plan_list = PlansTitleSpeed.objects.values('id', 'title', 'price', 'option', 'equipment', 'period', 'speed')

    # Define the context for the template
    context = {
        'plan_list': plan_list
    }

    # Render the template with the context
    return render(request, template_name, context)

from django.shortcuts import render, get_object_or_404
from .models import PlansTitleSpeed

def detail(request, pk):
    """
    Renders the detail view for a specific plan.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the plan.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    template_name = 'plans/detail.html'
    
    # Retrieve the plan detail from the database
    plan_detail = get_object_or_404(
        PlansTitleSpeed.objects.values('id', 'title', 'price', 'option', 'equipment', 'period', 'speed').filter(is_on_main=True),
        pk=pk
    )
    
    context = {
        'plan_detail': plan_detail
    }
    
    return render(request, template_name, context)
