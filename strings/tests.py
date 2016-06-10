from django.test import TestCase
from strings.notes import *
import decimal

class NotesTests(TestCase):
   
    def test_sound_key(self):
        self.assertEqual(sound_to_key('A', 0), 1)
        self.assertEqual(sound_to_key('E', 1), 8)
        self.assertEqual(sound_to_key('A', 4), 49)
        self.assertEqual(sound_to_key('C', 8), 88)
        self.assertEqual(sound_to_key('E', 5), 56)
        self.assertEqual(sound_to_key('C', 8), 88)
    
    def test_pitch(self):
        self.assertEqual(get_pitch('A', 4), 440)
        self.assertEqual(round(get_pitch('C', 0),2), 16.35)
        self.assertEqual(round(get_pitch('C', 8), 2), 4186.01)
        
        
    def test_parser(self):
        a0 = parse_note('A0')
        self.assertEqual(a0.name, 'A')
        self.assertEqual(a0.octave, 0)
        e1 = parse_note('F#1')
        self.assertEqual(e1.name, 'F#')
        self.assertEqual(e1.octave, 1)
    
class StringTensionTest(TestCase):
    def test_string_tension(self):
        pass
#        tension = "%.2f" % string_tension(63, 0.057, 329)
#        print(string_tension(63, 0.057, 329))
#        self.assertEqual(float(tension), 10.02)
        
        
    
        
        
       
            

            
        
