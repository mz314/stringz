from django.shortcuts import render
from django.views.generic import View
from strings.forms import StringForm
from strings.forms import StringSetForm, StringStringsetForm
from strings.models import String, StringSet
from strings.notes import Constants, get_note_choice

from rest_framework import viewsets, routers
from strings.serializers import StringSerializer, StringSetSerializer

class StringViewSet(viewsets.ModelViewSet):
    queryset = String.objects.all()
    serializer_class = StringSerializer
    

class StringSetViewSet(viewsets.ModelViewSet):
    queryset = StringSet.objects.all()
    serializer_class = StringSetSerializer
    


#class StringsView(View):
#    template_name = 'strings/string_list.html'
#
#    def render(self, request, form): 
#        strings = String.objects.all()
#        return render(request, self.template_name, {
#                      'strings': strings,
#                      'form': form
#                      })
#        
#    def post(self, request, * args, ** kwargs):
#        form = StringForm(request.POST)
#        if form.is_valid():
#            form.save()
#        return self.render(request, form)
#     
#    def get(self, request, * args, ** kwargs):
#        form = StringForm()
#        return self.render(request, form)
# 
#
#class StringSetsView(View):
#    template_name = 'strings/stringset_list.html'
#    
#    def get(self, request, * args, ** kwargs):
#        stringsets = StringSet.objects.all()
#        form = StringSetForm()
#        return render(request, self.template_name, {
#            'form': form,
#            'stringsets': stringsets,
#    })
#
#
#def stringset(request, set):
#    stringset = StringSet.objects.get(pk=set)
#    strings = String.objects.all()
#    if request.method == 'POST':
#        form = StringSetForm(request.POST, instance=stringset)
#        if form.is_valid():
#            form.save()
#            #TODO redirect here
#    else:
#        form = StringSetForm(instance=stringset)
#
#    return render(request, 'strings/stringset.html', {
#        'stringset': stringset,
#        'form': form,
#        'strings': strings,
#        'notes': get_note_choice(flat=True),
#    })    
#    
#
#    

