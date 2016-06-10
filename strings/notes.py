import math

class Constants:
    NOTES = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', )
    NOTE_ADD = {
        'C':1,
        'C#':2,
        'D':3,
        'D#':4,
        'E':5,
        'F':6,
        'F#':7,
        'G':8,
        'G#':9,
        'A':10,
        'A#':11,
        'B':12
            
    }
    

class Note:
    def __init__(self, name, octave, pitch):
        self.name = name
        self.pitch = pitch
        self.octave = octave


def octave_to_keystart(octave):
      
    start = (octave) * 12
        
    return start
        

def sound_to_key(note, octave):
    return  (octave_to_keystart(octave) + Constants.NOTE_ADD[note])-9
    

def get_pitch(note, octave, reference_pitch=440):
    key = sound_to_key(note, octave)
    root = math.pow(2, 1 / 12)
    pitch = pow(root, key-49) * reference_pitch
    return pitch
        
    
def get_notes(start_octave=0, start_note='A', end_octave=8, end_note='G#'):
    notes = []        
    for o in range(start_octave, end_octave):
        for n in Constants.NOTES:
            note = Note(name=n, octave=o, pitch=get_pitch(n, o))
            notes.append(note)
                
    return notes
    

def get_note_choice(start_octave=0, start_note='A', end_octave=8, end_note='G#', flat=False):
    choices = []
    for o in range(start_octave, end_octave):
        for n in Constants.NOTES:
            name = n + str(o)
            if flat:
                choices.append(name)
            else:
                choices.append((name, name))
    return choices
                

def parse_note(note_text):
    note = None
    octave = None
    if len(note_text) == 3: #has sharp
        note = note_text[0] + note_text[1]
        octave = note_text[2]
    elif len(note_text) == 2:
        note = note_text[0]
        octave = note_text[1]
    else:
        #TODO throw type error
        return None
    return Note(name=note, octave=int(octave), pitch=get_pitch(note, int(octave)))
            
"""
http://www.daddario.com/DAstringtensionguide.Page
http://hyperphysics.phy-astr.gsu.edu/hbase/waves/string.html
http://www.mcdonaldstrings.com/String_tensions.pdf
T = (UW x (2 x L x F)2) / 386.4
T = 4 x F2 x L x M / 980621
"""

def gauge_to_weight(gauge):
    pass

def get_string_tension(scale_length, gauge, frequency):
    #m = M = .057 x 6.3 = .359gm
    m = gauge * (scale_length / 10)
    f2 = (frequency * frequency)
    return 4 * f2 * scale_length * m / 980621