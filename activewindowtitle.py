import Xlib
import Xlib.display

def _get_active_window(root, display):
    _net_active_window = display.intern_atom('_NET_ACTIVE_WINDOW')
    return root.get_full_property(_net_active_window, Xlib.X.AnyPropertyType).value[0]

def _get_window_name(root, display):
    _net_wm_name = display.intern_atom('_NET_WM_NAME')
    try:
        window_obj = display.create_resource_object('window', root)
        window_name = window_obj.get_full_property(_net_wm_name, 0).value
    except Xlib.error.XError:
        window_name = None
    return window_name

def get_title(): 
    _display = Xlib.display.Display()
    _root = _display.screen().root
    _root.change_attributes(event_mask=Xlib.X.PropertyChangeMask)
    _active_window = _get_active_window(_root, _display) 
    _window_name = _get_window_name(_active_window, _display)
    return "" if _window_name == None else _window_name.decode("UTF-8") 
