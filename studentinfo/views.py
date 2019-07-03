from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Info, Marks
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic import ListView, DetailView
from studentinfo.forms import InfoForm, MarksForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.db.models import Q, F
from django.db.models import Sum, Avg

# Create your views here.


class Info_ListView(LoginRequiredMixin, ListView):

    model = Info
    template_name = 'index.html'
    context_object_name = 'infolist'

    # def list(self):
    #     a=[]
    #     for name in :
    #         a.append(name.name_text)

    # def search_titles(request):
    #     if request.method == 'POST':
    #         search_text == request.POST['search_text']
    #     else:
    #         search_text = ''

    #     list = Info_ListView.objects.filter(name_text__contains=search_text)

    #     return render_to_response('ajax_search.html', {'list' : list})


class Info_DetailView(DetailView):
    model = Info
    template_name = 'detail.html'
    context_object_name = 'studentdetail'

    def get_context_data(self, **kwargs):
        context = super(Info_DetailView, self).get_context_data(**kwargs)
        try:
            context['first_term'] = Marks.objects.filter(
                student=self.kwargs['pk'], terminal='first_term').latest('id')
        except:
            context['first_term'] = False

        try:
            context['second_term'] = Marks.objects.filter(
                student=self.kwargs['pk'], terminal='second_term').latest('id')
        except:
            context['second_term'] = False

        try:
            context['third_term'] = Marks.objects.filter(
                student=self.kwargs['pk'], terminal='third_term').latest('id')

        except:
            context['third_term'] = False
        return context


class Info_DeleteView(DeleteView):
    model = Info
    success_url = reverse_lazy('index')
    template_name = 'deleteform.html'


class Info_FormView(LoginRequiredMixin, FormView):
    template_name = 'add.html'
    form_class = InfoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        form.save()

        return super(Info_FormView, self).form_valid(form)


class Info_UpdateView(UpdateView):
    model = Info
    form_class = InfoForm
    template_name = 'updatestudent.html'
    context_object_name = 'updatestudent'

    def get_success_url(self):
        return reverse_lazy('student-detail', args=(self.object.id,))


class Marks_MarksView(FormView):
    template_name = 'marks.html'
    form_class = MarksForm

    def get_success_url(self):
        return reverse_lazy('student-detail', args=(self.kwargs['student_id'],))

    def form_valid(self, form):
        marks = form.save(commit=False)
        marks.student = Info.objects.get(id=self.kwargs['student_id'])
        marks.total = marks.english + marks.science + marks.maths + marks.nepali + marks.computer
        marks.avg = marks.total/5
        marks.percent = (marks.total/500)*100
        marks.save()
        return super(Marks_MarksView, self).form_valid(form)

class Marks_ListView(ListView):
    model = Marks
    template_name = 'markslist.html'
    context_object_name = 'markslist'


class Marks_DisplayView(DetailView):
    model = Marks
    template_name = 'displaymarks.html'
    context_object_name = 'displaymarks'

    def get_queryset(self):
        result = Marks.objects.filter(student=self.kwargs['pk'])
        return result


class Marks_UpdateView(UpdateView):
    model = Marks
    form_class = MarksForm
    template_name = 'updatemarks.html'
    context_object_name = 'updatemarks'

    def get_success_url(self):
        return reverse_lazy('student-detail', args=(self.object.student_id,))


class Home(TemplateView):
    template_name = 'contact.html'

# class Search_View(TemplateView):
#     template_name = 'autocomplete.html'

#     def get_context_data(self, **kwargs):
#         context = super(Search_View, self).get_context_data(**kwargs)
#         query=Info.objects.all()
#         items=[]
#         for i in query:
#             items.append(i.name_text.encode('ascii', 'xmlcharrefreplace'))
#         context['querylist']=items
#         return context.replace()


def autocompleteModel(request):
    search_qs = Info.objects.filter(
        name_text__startswith=request.REQUEST['search'])
    results = []
    for r in search_qs:
        results.append(r.name)
    resp = request.REQUEST['callback'] + '(' + json.dumps(result) + ');'
    return HttpResponse(resp, content_type='application/json')
