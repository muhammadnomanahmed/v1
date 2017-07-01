# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from django.contrib import admin

from .models import Choice, Question
from .models import Question

from django.contrib import admin
from django.contrib import admin

from .models import Choice, Question
# Register your models here.
from django.contrib import admin

from .models import Question
from django.contrib import admin

from .models import Question

from django.contrib import admin

from .models import Choice, Question

from django.contrib import admin

from .models import Question

#class QuestionAdmin(admin.ModelAdmin):
 #   fieldsets = [
  #      (None,               {'fields': ['question_text']}),
   #     ('Date information', {'fields': ['pub_date']}),
   # ]

#admin.site.register(Question, QuestionAdmin)


#admin.site.register(Choice)
#class QuestionAdmin(admin.ModelAdmin):
 #   fields = ['pub_date', 'question_text']

#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Question)



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    st_filter = ['pub_date'] 
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
admin.site.register(Question, QuestionAdmin)
