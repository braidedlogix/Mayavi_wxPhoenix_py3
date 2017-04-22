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


class JPEGWriter(ImageWriter):
    """
    JPEGWriter - Writes JPEG files.
    
    Superclass: ImageWriter
    
    JPEGWriter writes JPEG files. It supports 1 and 3 component data
    of unsigned char. It relies on the IJG's libjpeg.  Thanks to IJG for
    supplying a public jpeg IO library.
    
    @sa
    JPEGReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkJPEGWriter, obj, update, **traits)
    
    progressive = tvtk_base.true_bool_trait(help=\
        """
        Progressive JPEG generation.
        """
    )

    def _progressive_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgressive,
                        self.progressive_)

    write_to_memory = tvtk_base.false_bool_trait(help=\
        """
        Write the image to memory (a UnsignedCharArray)
        """
    )

    def _write_to_memory_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToMemory,
                        self.write_to_memory_)

    quality = traits.Trait(95, traits.Range(0, 100, enter_set=True, auto_set=False), help=\
        """
        Compression quality. 0 = Low quality, 100 = High quality
        """
    )

    def _quality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuality,
                        self.quality)

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

    _updateable_traits_ = \
    (('progressive', 'GetProgressive'), ('write_to_memory',
    'GetWriteToMemory'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('quality',
    'GetQuality'), ('file_dimensionality', 'GetFileDimensionality'),
    ('file_name', 'GetFileName'), ('file_pattern', 'GetFilePattern'),
    ('file_prefix', 'GetFilePrefix'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'progressive',
    'release_data_flag', 'write_to_memory', 'file_dimensionality',
    'file_name', 'file_pattern', 'file_prefix', 'progress_text',
    'quality'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(JPEGWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit JPEGWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['progressive', 'write_to_memory'], [], ['file_dimensionality',
            'file_name', 'file_pattern', 'file_prefix', 'quality']),
            title='Edit JPEGWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit JPEGWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

