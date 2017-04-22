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


class PNGWriter(ImageWriter):
    """
    PNGWriter - Writes PNG files.
    
    Superclass: ImageWriter
    
    PNGWriter writes PNG files. It supports 1 to 4 component data of
    unsigned char or unsigned short
    
    @sa
    PNGReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPNGWriter, obj, update, **traits)
    
    write_to_memory = tvtk_base.false_bool_trait(help=\
        """
        Write the image to memory (a UnsignedCharArray)
        """
    )

    def _write_to_memory_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToMemory,
                        self.write_to_memory_)

    compression_level = traits.Trait(5, traits.Range(0, 9, enter_set=True, auto_set=False), help=\
        """
        Set/Get the zlib compression level. The range is 0-9, with 0
        meaning no compression corresponding to the largest file size,
        and 9 meaning best compression, corresponding to the smallest
        file size. The default is 5.
        """
    )

    def _compression_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompressionLevel,
                        self.compression_level)

    def _get_result(self):
        return wrap_vtk(self._vtk_obj.GetResult())
    def _set_result(self, arg):
        old_val = self._get_result()
        my_arg = deref_array([arg], [['vtkUnsignedCharArray']])
        self._wrap_call(self._vtk_obj.SetResult,
                        my_arg[0])
        self.trait_property_changed('result', old_val, arg)
    result = traits.Property(_get_result, _set_result, help=\
        """
        When writing to memory this is the result, it will be NULL until
        the data is written the first time
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input object from the image pipeline.
        """
    )

    def add_text(self, *args):
        """
        V.add_text(string, string)
        C++: void AddText(const char *key, const char *value)
        Adds a text chunk to the PNG. More than one text chunk with the
        same key is permissible. There are a number of predefined
        keywords that should be used when appropriate. See
        http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html for more
        information.
        """
        ret = self._wrap_call(self._vtk_obj.AddText, *args)
        return ret

    _updateable_traits_ = \
    (('write_to_memory', 'GetWriteToMemory'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('compression_level',
    'GetCompressionLevel'), ('file_dimensionality',
    'GetFileDimensionality'), ('file_name', 'GetFileName'),
    ('file_pattern', 'GetFilePattern'), ('file_prefix', 'GetFilePrefix'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_memory', 'compression_level',
    'file_dimensionality', 'file_name', 'file_pattern', 'file_prefix',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PNGWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PNGWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['write_to_memory'], [], ['compression_level',
            'file_dimensionality', 'file_name', 'file_pattern', 'file_prefix']),
            title='Edit PNGWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PNGWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

