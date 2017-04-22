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


class FileOutputWindow(OutputWindow):
    """
    FileOutputWindow - File Specific output window class
    
    Superclass: OutputWindow
    
    Writes debug/warning/error output to a log file instead of the
    console. To use this class, instantiate it and then call
    set_instance(this).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFileOutputWindow, obj, update, **traits)
    
    append = tvtk_base.false_bool_trait(help=\
        """
        Setting append will cause the log file to be opened in append
        mode.  Otherwise, if the log file exists, it will be overwritten
        each time the FileOutputWindow is created.
        """
    )

    def _append_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAppend,
                        self.append_)

    flush = tvtk_base.false_bool_trait(help=\
        """
        Turns on buffer flushing for the output to the log file.
        """
    )

    def _flush_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlush,
                        self.flush_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Sets the name for the log file.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('append', 'GetAppend'), ('flush', 'GetFlush'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('file_name', 'GetFileName'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['append', 'debug', 'flush', 'global_warning_display', 'file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FileOutputWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FileOutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['append', 'flush'], [], ['file_name']),
            title='Edit FileOutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FileOutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

