def _get_brightness_int_from_filename(filename): 
    _path = "/sys/class/backlight/intel_backlight/" + filename
    with open(_path, 'r') as file:
        return int(file.read().replace('\n', '')) 

def get_brightness_percentage(): 
    _max = _get_brightness_int_from_filename("max_brightness") 
    _curr = _get_brightness_int_from_filename("brightness") 
    _percentage = round(_curr / _max * 10) * 10 
    return "BRIGHTNESS {0}%".format(_percentage) 
