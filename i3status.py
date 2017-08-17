import json
import subprocess

def get_process(process): 
    '''get the process output string'''
    return str(subprocess.check_output(process).decode("ascii")).strip() 

def get_brightness_int_from_filename(filename): 
    _path = "/sys/class/backlight/intel_backlight/" + filename
    with open(_path, 'r') as file:
        return int(file.read().replace('\n', '')) 

def get_brightness_percentage(): 
    _max = get_brightness_int_from_filename("max_brightness") 
    _curr = get_brightness_int_from_filename("brightness") 
    _percentage = round(_curr / _max * 10) * 10 
    return "BRIGHTNESS {0}%".format(_percentage) 

def next_line(i3status): 
    '''get the next line of output from the process and format it'''
    line = str(i3status.stdout.readline().decode("ascii")).strip()
    return line

def insert_custom_objects(json_line): 
    '''insert a custom object into the i3 tick''' 
    json_line.insert(7, {'full_text' : get_brightness_percentage(), 'name' : 'brightness'})
    return json_line

def print_JSON_tick(i3status): 
    # gets the next line without the initial comma 
    _json_line = json.loads(next_line(i3status)[1:]) 
    _json_line = insert_custom_objects(_json_line) 
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
