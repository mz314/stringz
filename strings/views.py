from django.shortcuts import render
from django.views.generic import View
from strings.forms import StringForm
from strings.forms import StringSetForm
from strings.models import String, StringSet
from strings.notes import Constants


class StringsView(View):
    template_name = 'strings/string_list.html'

    def render(self, request, form): 
        strings = String.objects.all()
        return render(request, self.template_name, {
                      'strings': strings,
                      'form': form
                      })
        
    def post(self, request, * args, ** kwargs):
        form = StringForm(request.POST)
        if form.is_valid():
            form.save()
        return self.render(request, form)
     
    def get(self, request, * args, ** kwargs):
        form = StringForm()
        return self.render(request, form)
 

class StringSetsView(View):
    template_name = 'strings/stringset_list.html'
    
    def get(self, request, * args, ** kwargs):
        stringsets = StringSet.objects.all()
        form = StringSetForm()
        return render(request, self.template_name, {
            'form': form,
            'stringsets': stringsets,
    })
    
def stringset(request, set):
    stringset = StringSet.objects.get(pk=set)
    return render(request, 'strings/stringset.html', {
        'stringset': stringset,
    })    
    
def stringset_edit(request, set):
    strings = String.objects.all()
    form = StringSetForm()
    return render(request, 'strings/stringset.html', {
        'strings': strings,
        'notes': Notes.get_note_choice(flat=True),
        'form': form,
    })
    

