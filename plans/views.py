from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Plans

class PlansListView(ListView):
    model = Plans
    ordering = 'price'

class PlansDetailView(DetailView):
    model = Plans


# def index(request):
#     """
#     Renders the index view for the plans.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: The HTTP response object containing the rendered template.
#     """
#     # Define the template name
#     template_name = 'plans/plans.html'

#     plan_list = Plans.objects.values(
#         'id', 'title', 'price', 'option', 'equipment',
#         'period', 'speed'
#         ).filter(is_on_main=True)

#     # Define the context for the template
#     context = {
#         'plan_list': plan_list
#     }

#     # Render the template with the context
#     return render(request, template_name, context)

# def detail(request, pk):
#     """
#     Renders the detail view for a specific plan.

#     Args:
#         request (HttpRequest): The HTTP request object.
#         pk (int): The primary key of the plan.

#     Returns:
#         HttpResponse: The HTTP response object containing the rendered template.
#     """
#     template_name = 'plans/detail.html'

#     # Retrieve the plan detail from the database
#     plan_detail = get_object_or_404(
#         Plans.objects.values(
#             'id', 'title', 'price', 'option',
#             'equipment', 'period', 'speed'
#         ).filter(is_on_main=True),
#         pk=pk
#     )

#     context = {
#         'plan_detail': plan_detail
#     }

#     return render(request, template_name, context)
