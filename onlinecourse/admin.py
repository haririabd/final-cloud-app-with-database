from random import choices
from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Enrollment, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
# A class that is used to create a new admin page for the Course model.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('id', 'name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')
    list_filter = ['course']


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')

# The QuestionAdmin class is a subclass of ModelAdmin, and it has an inline attribute that is a list
# containing the ChoiceInline class.


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('id', 'question', 'lesson')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'question')

# <HINT> Register Question and Choice models here


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Submission)
