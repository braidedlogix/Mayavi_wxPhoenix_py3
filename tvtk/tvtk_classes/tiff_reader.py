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

from tvtk.tvtk_classes.image_reader2 import ImageReader2


class TIFFReader(ImageReader2):
    """
    TIFFReader - read TIFF files
    
    Superclass: ImageReader2
    
    TIFFReader is a source object that reads TIFF files. It should be
    able to read almost any TIFF file
    
    @sa
    TIFFWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTIFFReader, obj, update, **traits)
    
    origin_specified_flag = tvtk_base.false_bool_trait(help=\
        """
        Set/get methods to see if manual origin has been set.
        """
    )

    def _origin_specified_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginSpecifiedFlag,
                        self.origin_specified_flag_)

    spacing_specified_flag = tvtk_base.false_bool_trait(help=\
        """
        Set/get if the spacing flag has been specified.
        """
    )

    def _spacing_specified_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacingSpecifiedFlag,
                        self.spacing_specified_flag_)

    orientation_type = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Set orientation type ORIENTATION_TOPLEFT         1       (row 0
        top, col 0 lhs) ORIENTATION_TOPRIGHT        2       (row 0 top,
        col 0 rhs) ORIENTATION_BOTRIGHT        3       (row 0 bottom, col
        0 rhs) ORIENTATION_BOTLEFT         4       (row 0 bottom, col 0
        lhs) ORIENTATION_LEFTTOP         5       (row 0 lhs, col 0 top)
        ORIENTATION_RIGHTTOP        6       (row 0 rhs, col 0 top)
        ORIENTATION_RIGHTBOT        7       (row 0 rhs, col 0 bottom)
        ORIENTATION_LEFTBOT         8       (row 0 lhs, col 0 bottom)
        User need to explicitly include vtk_tiff.h header to have access
        to those #define
        """
    )

    def _orientation_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientationType,
                        self.orientation_type)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_orientation_type_specified_flag(self):
        return self._vtk_obj.GetOrientationTypeSpecifiedFlag()
    orientation_type_specified_flag = traits.Property(_get_orientation_type_specified_flag, help=\
        """
        Get method to check if orientation type is specified.
        """
    )

    _updateable_traits_ = \
    (('origin_specified_flag', 'GetOriginSpecifiedFlag'),
    ('spacing_specified_flag', 'GetSpacingSpecifiedFlag'),
    ('file_lower_left', 'GetFileLowerLeft'), ('swap_bytes',
    'GetSwapBytes'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('data_byte_order', 'GetDataByteOrder'), ('orientation_type',
    'GetOrientationType'), ('data_extent', 'GetDataExtent'),
    ('data_origin', 'GetDataOrigin'), ('data_spacing', 'GetDataSpacing'),
    ('file_dimensionality', 'GetFileDimensionality'), ('file_name',
    'GetFileName'), ('file_name_slice_offset', 'GetFileNameSliceOffset'),
    ('file_name_slice_spacing', 'GetFileNameSliceSpacing'),
    ('file_pattern', 'GetFilePattern'), ('file_prefix', 'GetFilePrefix'),
    ('header_size', 'GetHeaderSize'), ('memory_buffer_length',
    'GetMemoryBufferLength'), ('number_of_scalar_components',
    'GetNumberOfScalarComponents'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'file_lower_left',
    'global_warning_display', 'origin_specified_flag',
    'release_data_flag', 'spacing_specified_flag', 'swap_bytes',
    'data_byte_order', 'data_extent', 'data_origin', 'data_spacing',
    'file_dimensionality', 'file_name', 'file_name_slice_offset',
    'file_name_slice_spacing', 'file_pattern', 'file_prefix',
    'header_size', 'memory_buffer_length', 'number_of_scalar_components',
    'orientation_type', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TIFFReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TIFFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['file_lower_left', 'origin_specified_flag',
            'spacing_specified_flag', 'swap_bytes'], ['data_byte_order'],
            ['data_extent', 'data_origin', 'data_spacing', 'file_dimensionality',
            'file_name', 'file_name_slice_offset', 'file_name_slice_spacing',
            'file_pattern', 'file_prefix', 'header_size', 'memory_buffer_length',
            'number_of_scalar_components', 'orientation_type']),
            title='Edit TIFFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TIFFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

