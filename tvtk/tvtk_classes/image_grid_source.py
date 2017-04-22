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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageGridSource(ImageAlgorithm):
    """
    ImageGridSource - Create an image of a grid.
    
    Superclass: ImageAlgorithm
    
    ImageGridSource produces an image of a grid.  The default output
    type is double.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageGridSource, obj, update, **traits)
    
    def get_data_scalar_type(self):
        """
        V.get_data_scalar_type() -> int
        C++: int GetDataScalarType()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        ret = self._vtk_obj.GetDataScalarType()
        return ret
        

    def set_data_scalar_type(self, *args):
        """
        V.set_data_scalar_type(int)
        C++: void SetDataScalarType(int a)
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataScalarType, *args)
        return ret

    def set_data_scalar_type_to_int(self):
        """
        V.set_data_scalar_type_to_int()
        C++: void SetDataScalarTypeToInt()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        self._vtk_obj.SetDataScalarTypeToInt()

    def set_data_scalar_type_to_short(self):
        """
        V.set_data_scalar_type_to_short()
        C++: void SetDataScalarTypeToShort()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        self._vtk_obj.SetDataScalarTypeToShort()

    def set_data_scalar_type_to_unsigned_char(self):
        """
        V.set_data_scalar_type_to_unsigned_char()
        C++: void SetDataScalarTypeToUnsignedChar()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedChar()

    def set_data_scalar_type_to_unsigned_short(self):
        """
        V.set_data_scalar_type_to_unsigned_short()
        C++: void SetDataScalarTypeToUnsignedShort()
        Set/Get the data type of pixels in the imported data. As a
        convenience, the output_scalar_type is set to the same value.
        """
        self._vtk_obj.SetDataScalarTypeToUnsignedShort()

    data_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, 255, 0, 255, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _data_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataExtent,
                        self.data_extent)

    data_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _data_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataOrigin,
                        self.data_origin)

    data_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _data_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataSpacing,
                        self.data_spacing)

    fill_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the grey level of the fill. Default 0.0.
        """
    )

    def _fill_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillValue,
                        self.fill_value)

    grid_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _grid_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridOrigin,
                        self.grid_origin)

    grid_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(10, 10, 0), cols=3, help=\
        """
        
        """
    )

    def _grid_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridSpacing,
                        self.grid_spacing)

    line_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the grey level of the lines. Default 1.0.
        """
    )

    def _line_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineValue,
                        self.line_value)

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

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('data_extent',
    'GetDataExtent'), ('data_origin', 'GetDataOrigin'), ('data_spacing',
    'GetDataSpacing'), ('fill_value', 'GetFillValue'), ('grid_origin',
    'GetGridOrigin'), ('grid_spacing', 'GetGridSpacing'), ('line_value',
    'GetLineValue'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'data_extent', 'data_origin', 'data_spacing',
    'fill_value', 'grid_origin', 'grid_spacing', 'line_value',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageGridSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['data_extent', 'data_origin', 'data_spacing',
            'fill_value', 'grid_origin', 'grid_spacing', 'line_value']),
            title='Edit ImageGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageGridSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

