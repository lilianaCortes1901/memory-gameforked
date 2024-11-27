

current_midi_files = []
current_user_input = []

letters_and_files_dict = {'MID_FILES/c_note_one_sec.mid' : 'a', 'MID_FILES/d_note_one_sec.mid' : 's', 'MID_FILES/e_note_one_sec.mid':'d',
                          'MID_FILES/f_note_one_sec.mid':'f', 'MID_FILES/g_note_one_sec.mid': 'g', 'MID_FILES/a_note_one_sec.mid': 'h',
                          'MID_FILES/b_note_one_sec.mid' : 'j', 'MID_FILES/c_oct_note_one_sec.mid':'k'}



#called from frontend to update global variable
def get_midi_files(midi_files):
    print(f"Selected MIDI Files recieved: {midi_files}")
    global current_midi_files
    current_midi_files = midi_files
    

#called from frontend to update global variable
def get_user_input(user_input):
    print(f"User input received: {user_input}")
    global current_user_input 
    current_user_input = user_input
    

def check_user_input():
    print("Checking user input!")
    global letters_and_files_dict
    global current_midi_files
    global current_user_input
    
    if len(current_midi_files) != len(current_user_input):
        return False

    value_to_key_dict = {v: k for k, v in letters_and_files_dict.items()} #get value to key mapping by reversing dict

    for i in range(len(current_midi_files)):
        
        if current_user_input[i] in value_to_key_dict: #get key corresponding to user input
            corresponding_key = value_to_key_dict[current_user_input[i]]
        else:
            return False 

        if current_midi_files[i] != corresponding_key:
            return False

    return True


def send_current_midi_files_back():
    global current_midi_files
    return_midi_files = current_midi_files
    return return_midi_files
    