from django.views import generic

from scrap_input.scrap_app.models import CompareScrapTable


class CompareScrapWeightView(generic.ListView):
    model = CompareScrapTable
    template_name = 'compare/compare_scrap_weight.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO
        return context


class UpdateUserScrapWeightView(generic.UpdateView):
    model = CompareScrapTable
    fields = ('user_id', 'actual_weight')
    template_name = 'compare/update_scrap_weight.html'
