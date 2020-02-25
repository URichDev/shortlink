from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
from django.views.generic import FormView
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,DeleteView

from .forms import ShortLinkForm
from .services import short_link_generator
from .models import ShortLink

class MainView(View):
    def get(self, request):
        return HttpResponse("Home")

class LinkShortenerView(FormView):
    template_name = "link_shortener/main.html"
    form_class = ShortLinkForm
    success_url = '/users/profile/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.short_link = short_link_generator()
        instance.save()
        return redirect(self.get_success_url())


class ShortLinkList(ListView):
    model = ShortLink
    paginate_by = 10

class ShortLinkUpdate(UpdateView):
    model = ShortLink
    fields = ['short_link']
    template_name_suffix = '_update_form'
    success_url = '/my_links'

class ShortLinkDelete(DeleteView):
    model = ShortLink
    success_url = '/my_links'