import json
import subprocess
import activewindowtitle 
import brightness 

def get_process(process): 
    '''get the process output string'''
    return str(subprocess.check_output(process).decode("ascii")).strip() 

def next_line(i3status): 
    '''get the next line of output from the process and format it'''
    return str(i3status.stdout.readline().decode("ascii")).strip()
    
def print_JSON_tick(i3status): 
    # gets the next line without the initial comma 
    _json_line = json.loads(next_line(i3status)[1:]) 
    _json_line.insert(7, {'full_text' : brightness.get_brightness_percentage(), 'name' : 'brightness'})
    _json_line.insert(0, {'full_text': activewindowtitle.get_title(), 'name' : 'active_window'}) 
    print("," + json.dumps(_json_line), flush=True) 

def get_piped_i3status(): 
    return subprocess.Popen("i3status", stdout=subprocess.PIPE)

def print_first_3_lines(i3status): 
    '''The first 3 lines can be skipped.''' 
    for x in range(0,3): 
        print(next_line(i3status)) 

def init_tick(i3status): 
    while True: 
        print_JSON_tick(i3status)    

if __name__ == "__main__": 
    _i3status = get_piped_i3status() 
    print_first_3_lines(_i3status) 
    init_tick(_i3status) 
