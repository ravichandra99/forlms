from django.shortcuts import render,reverse
from lms.models import Course,Module,Lesson,CourseStatus,Category,Question,Answer
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic.edit import FormMixin
from lms.forms import QuestionForm

# Create your views here.

def index(request):
	category = Category.objects.all()
	return render(request,'index.html',{'category':category})

def about(request):
	return render(request,'about-us.html')

class CourseDetail(DetailView):
	model = Course
	template_name = 'course.html'

def blog(request):
	return render(request,'blog.html')

def contact(request):
	return render(request,'contact.html')

def event(request):
	return render(request,'event.html')

def allcourses(request):
	return render(request,'all-courses.html')

def mycourses(request):
	mycourses = CourseStatus.objects.filter(user = request.user)
	return render(request,'mycourses.html',{'mycourses':mycourses})

def cart(request):
	return render(request,'cart.html')

def checkout(request,slug):
    return render(request,'checkout.html')


class detail(FormMixin, DetailView):
	model = Course
	template_name = 'purchased-course.html'
	form_class = QuestionForm

	def get_success_url(self):
		return reverse('lms:detail', kwargs={'slug': self.object.slug})

	def get_context_data(self, **kwargs):
		context = super(detail, self).get_context_data(**kwargs)
		is_enrolled = self.request.user.is_authenticated and CourseStatus.objects.filter(user = self.request.user).filter(course = kwargs['object']).exists()
		if is_enrolled:
			user_course_it = CourseStatus.objects.filter(user = self.request.user).filter(course = kwargs['object'])
			user_course = CourseStatus.objects.get(id = [i.id for i in user_course_it][0])
			context['viewed'] = [i.video_id for i in user_course.completed_lessons.all()]
			context['form'] = QuestionForm()
			context['questions'] = Question.objects.filter(course = kwargs['object'])
			
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		course = Course.objects.get(slug = kwargs['slug'])
		form = self.get_form()
		question = request.POST.get('question')
		if form.is_valid():
			form.instance.user = self.request.user
			form.instance.course = course
			form.instance.question = question
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		form.save()
		return super(detail, self).form_valid(form)

def onended(request):
	if request.is_ajax():
		iframe_id = request.GET.get('iframe_id')
		status = CourseStatus.objects.get(user = request.user)
		current_lesson = Lesson.objects.get(video_id = iframe_id)
		status.completed_lessons.add(current_lesson)
		status.save()

		data = {'next':next_lesson.id,'get_slug':next_lesson.get_slug(),'percent':status.percent()}
	return JsonResponse(data)

def enrol(request):
	if request.is_ajax():
		username = request.GET.get('username')[0]
		data = request.GET.get('status')
		#print(data)
		r = data.split(':')
		slug = r[0]
		payment_id = r[1]
		enrol,created = CourseStatus.objects.get_or_create(user_id = request.user.id,course_id = Course.objects.get(slug = slug).id)
		data = {'slug':slug,'created':created}
		return JsonResponse(data)

def navbar(request):
   return {'category':Category.objects.all()}


