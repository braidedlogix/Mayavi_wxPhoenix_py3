# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui.item import Item, spring
from traitsui.group import HGroup
from traitsui.view import View

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk


def InstanceEditor(*args, **kw):
    from traitsui.editors.api import InstanceEditor as Editor
    return Editor(view_name="handler.view")

try:
    long
except NameError:
    # Silly workaround for Python3.
    long = int

from tvtk.tvtk_classes.output_window import OutputWindow


class Win32OutputWindow(OutputWindow):
    """
    Win32OutputWindow - Win32 Specific output window class
    
    Superclass: OutputWindow
    
    This class is used for error and debug message output on the windows
    platform.   It creates a read only EDIT control to display the
    output.   This class should not be used directly.   It should only be
    used through the interface of OutputWindow.  This class only
    handles one output window per process.  If the window is destroyed,
    the Object::GlobalWarningDisplayOff() function is called.  The
    window is created the next time text is written to the window.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWin32OutputWindow, obj, update, **traits)
    
    send_to_std_err = tvtk_base.false_bool_trait(help=\
        """
        Set or get whether the Win32OutputWindow should also send its
        output to stderr / cerr.
        """
    )

    def _send_to_std_err_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSendToStdErr,
                        self.send_to_std_err_)

    _updateable_traits_ = \
    (('send_to_std_err', 'GetSendToStdErr'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'send_to_std_err'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Win32OutputWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Win32OutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['send_to_std_err'], [], []),
            title='Edit Win32OutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Win32OutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

