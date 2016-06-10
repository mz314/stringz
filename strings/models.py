import decimal
from django.db import models
from pint import UnitRegistry
from strings.notes import parse_note, get_note_choice, get_string_tension


class Guitar(models.Model):
    name = models.CharField(max_length=128)
    scale_length_imperial = models.DecimalField(max_digits=8, decimal_places=2)
    #type = models.CharField(max_length=128) #acoustic/electric/classical/etc

class ScaleLength(models.Model):
    scale_imperial = models.DecimalField(max_digits=10, decimal_places=2)
    
    def scale_metric(self):
        return (self.scale_imperial*UnitRegistry().inch).to_base_units().magnitude*100
    
    def __str__(self):
        return str(self.scale_imperial)

class String(models.Model):
    WINDING_PLAIN = 'p'
    WINDING_WOUND = 'w'
    WINDING_WOUNDPLAIN = 'wp'
    WINDING_CHOICES = (
        (WINDING_PLAIN, 'Plain'),
        (WINDING_WOUND, 'Wound'),
        (WINDING_WOUNDPLAIN, 'Wound filed down')
    )
    
    MATERIAL_STEEL = "st"
    MATERIAL_NYLON = "nl"
    MATERIAL_CHOICES = (
        (MATERIAL_STEEL, 'Steel'),
        (MATERIAL_NYLON, 'Nylon')
    )
    
    """
    TODO: 
        coating
    """
    material = models.CharField(max_length=128, choices=MATERIAL_CHOICES)
    winding = models.CharField(max_length=128, choices=WINDING_CHOICES)
    gauge_imperial = models.DecimalField(max_digits=8, decimal_places=8)
    #unit_weight_imperial = models.DecimalField(max_digits=20, decimal_places=20)
    
    
    def gauge_metric(self):
        return (self.gauge_imperial*UnitRegistry().inch).to_base_units().magnitude*100
        
    
    def __str__(self):
        return str(self.gauge_imperial)
    

class StringStringSet(models.Model):
    string = models.ForeignKey("strings.String")
    stringset = models.ForeignKey("strings.StringSet")
    note = models.CharField(max_length=3, choices=get_note_choice())
    
    def get_pitch(self):
        note = parse_note(self.note)
        return str(note.pitch)
    
    def get_tension(self):
        note = parse_note(self.note)
        return str(get_string_tension(64.77, float(self.string.gauge_metric()), note.pitch))


class StringSet(models.Model):
    name = models.CharField(max_length=128)
    reference_pith = models.DecimalField(max_digits=20, decimal_places=2, default=440)
    scale_lengths = models.ManyToManyField("strings.ScaleLength", verbose_name="Recommended scale lengths")
    base_stringset = models.ForeignKey("strings.StringSet", null=True, blank=True)
    
    def get_stringset_strings(self):
        return StringStringSet.objects.filter(stringset=self)
    
    def __str__(self):
        return self.name
    
