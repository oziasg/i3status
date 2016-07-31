import json
import subprocess
import math

# get process output string 
def get_process(process): 
    return str(subprocess.check_output(process).decode("ascii")).strip() 

# get brightness percentage
def get_brightness(): 
    brightness = float(get_process("xbacklight")) 
    # round to nearest 10th 
    brightness = round(brightness / 10) * 10 
    return "BRIGHTNESS: {0}%".format(str(brightness))

# get the next line of output from the process and format it 
def next_line(i3status): 
    line = str(i3status.stdout.readline().decode("ascii")).strip()
    return line

# add data to be displayed on the i3 menu
def insert_custom_objects(json_line): 
    json_line.insert(7, {'full_text' : get_brightness(), 'name' : 'brightness'})
    return json_line

# prints the i3status JSON output tick
def print_json(i3status): 
    line = next_line(i3status)
    # remove the comma at the beginning 
    line = line[1:] 
   
    json_line = json.loads(line) 
    json_line = insert_custom_objects(json_line) 
    print("," + json.dumps(json_line), flush=True) 

def main(): 
    # pipe i3status output 
    i3status = subprocess.Popen("i3status", stdout=subprocess.PIPE)

    # first 3 lines can be skipped 
    for x in range(0,3): 
        print(next_line(i3status)) 
   
    # prints the i3status JSON output tick in an infinite loop
    while True: 
        print_json(i3status)    


main() 
