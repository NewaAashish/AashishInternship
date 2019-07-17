from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Info, Marks, Final, AcademicExtra
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.views.generic import ListView, DetailView, View
from studentinfo.forms import InfoForm, MarksForm, FinalForm, AcademicForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.db.models import Q, F
from django.db.models import Sum, Avg
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape
from .utils import render_to_pdf 
from reportlab.pdfgen import canvas  
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.template import RequestContext
import tempfile
import math
import xhtml2pdf.pisa as pisa
from django.utils import timezone


# Create your views here.
class Info_ListView(LoginRequiredMixin, ListView):
    model = Info
    template_name = 'index.html'
    context_object_name = 'infolist'

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
        try:
            context['academic_detail']= AcademicExtra.objects.filter(student__id=self.kwargs['pk']).latest('id')
        except:
            context['academic_detail']= False
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
        marks.total = marks.english + marks.science + marks.maths + marks.nepali + marks.computer + marks.social + marks.account + marks.eph
        marks.percent = float(math.ceil((marks.total/800)*100))
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

    def form_valid(self, form):
        marks = form.save(commit=False)
        marks.total = marks.english + marks.science + marks.maths + marks.nepali + marks.computer + marks.social + marks.account + marks.eph
        marks.percent = (marks.total/800)*100
        marks.save()
        return super(Marks_UpdateView, self).form_valid(form)

class Home(TemplateView):
    template_name = 'contact.html'

class Final_Result(TemplateView):
    model = Final
    form_class = FinalForm
    template_name = 'final_result.html'
    context_object_name = 'finalmarks'

    def get_context_data(self, **kwargs):
        context = super(Final_Result, self).get_context_data(**kwargs)
        context['displaymarks'] = Final.objects.filter(student__id=self.kwargs['pk']).latest('id')
        context['student'] = Info.objects.get(id=self.kwargs['pk'])
        return context

class Result(Info_DetailView):
    def dispatch(self, request, **kwargs):
        try:
            first_term = Marks.objects.filter(
                student=self.kwargs['pk'], terminal='first_term').latest('id')
        except:
            first_term = False
        try:
            second_term = Marks.objects.filter(
                student=self.kwargs['pk'], terminal='second_term').latest('id')
        except:
            second_term = False
        try:
            third_term = Marks.objects.filter(
                student=self.kwargs['pk'], terminal='third_term').latest('id')
        except:
            third_term = False
        

        # getmarks
        if first_term and second_term and third_term:
            english= (first_term.english/100*10)+(second_term.english/100*10)+(third_term.english/100*80)
            science= (first_term.science/100*10)+(second_term.science/100*10)+(third_term.science/100*80)
            maths= (first_term.maths/100*10)+(second_term.maths/100*10)+(third_term.maths/100*80)
            social= (first_term.social/100*10)+(second_term.social/100*10)+(third_term.social/100*80)
            eph= (first_term.eph/100*10)+(second_term.eph/100*10)+(third_term.eph/100*80)
            computer= (first_term.computer/100*10)+(second_term.computer/100*10)+(third_term.computer/100*80)
            nepali= (first_term.nepali/100*10)+(second_term.nepali/100*10)+(third_term.nepali/100*80)
            account= (first_term.account/100*10)+(second_term.account/100*10)+(third_term.account/100*80)
            total=english+science+maths+social+eph+computer+nepali+account
            percent=(total/800)*100
            if percent >= 80:
                remark = 'Very good'
            elif percent >= 70:
                remark = 'Good'
            elif percent >= 60:
                remark = 'Satisfactory'
            else:
                remark = 'Needs Improvement'


        remark='Satisfactory'
        Final.objects.create(
            student = Info.objects.get(id=self.kwargs['pk']),
            final_english = english,
            final_science = science,
            final_maths = maths,
            final_social = social,
            final_computer = computer,
            final_eph = eph,
            final_account = account,
            final_nepali = nepali,
            final_total = total,
            final_percent = float(math.ceil(percent)),
            final_remarks = remark,
        )
        
        return HttpResponseRedirect(reverse_lazy('student-detail', args=(self.kwargs['pk'],)))

class Academic_Extra(FormView):
    template_name = 'academic_extra.html'
    form_class = AcademicForm
    success_url = reverse_lazy('index')
    context_object_name = 'academic'

    def form_valid(self, form):
        detail = form.save(commit=False)
        detail.student = Info.objects.get(id=self.kwargs['student_id'])
        detail.save()
        return super(Academic_Extra, self).form_valid(form)

# For PDF #

class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):

    def get(self, request):
        final = Final.objects.all()
        # params = {
        #     'student': student,
        #     'final_english': final_english,
        #     'final_science': final_science,
        #     'final_maths': final_maths,
        #     'final_nepali': final_nepali,
        #     'final_computer': final_computer,
        #     'final_social': final_social,
        #     'final_eph': final_eph,
        #     'final_account': final_account,
        # }
        return render_to_pdf('pdf.html')