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

from tvtk.tvtk_classes.image_writer import ImageWriter


class PImageWriter(ImageWriter):
    """
    PImageWriter - Writes images to files.
    
    Superclass: ImageWriter
    
    PImageWriter writes images to files with any data type. The data
    type of the file is the same scalar type as the input.  The
    dimensionality determines whether the data will be written in one or
    multiple files. This class is used as the superclass of most image
    writing classes such as BMPWriter etc. It supports streaming.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPImageWriter, obj, update, **traits)
    
    memory_limit = traits.Int(1048576, enter_set=True, auto_set=False, help=\
        """
        Set / Get the memory limit in kibibytes (1024 bytes). The writer
        will stream to attempt to keep the pipeline size within this
        limit
        """
    )

    def _memory_limit_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMemoryLimit,
                        self.memory_limit)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input object from the image pipeline.
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('memory_limit', 'GetMemoryLimit'), ('file_dimensionality',
    'GetFileDimensionality'), ('file_name', 'GetFileName'),
    ('file_pattern', 'GetFilePattern'), ('file_prefix', 'GetFilePrefix'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_dimensionality', 'file_name',
    'file_pattern', 'file_prefix', 'memory_limit', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PImageWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['file_dimensionality', 'file_name', 'file_pattern',
            'file_prefix', 'memory_limit']),
            title='Edit PImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

