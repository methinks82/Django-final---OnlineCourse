from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5 

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

#admin.site.register(Choice, ChoiceInline)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
