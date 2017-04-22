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


class VoxelModeller(ImageAlgorithm):
    """
    VoxelModeller - convert an arbitrary dataset to a voxel
    representation
    
    Superclass: ImageAlgorithm
    
    VoxelModeller is a filter that converts an arbitrary data set to a
    structured point (i.e., voxel) representation. It is very similar to
    ImplicitModeller, except that it doesn't record distance; instead
    it records occupancy. By default it supports a compact output of 0/1
    VTK_BIT. Other vtk scalar types can be specified. The Foreground and
    Background values of the output can also be specified. NOTE: Not all
    vtk filters/readers/writers support the VTK_BIT scalar type. You may
    want to use VTK_CHAR as an alternative.
    @sa
    ImplicitModeller
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVoxelModeller, obj, update, **traits)
    
    scalar_type = traits.Trait('bit',
    tvtk_base.TraitRevPrefixMap({'bit': 1, 'char': 2, 'double': 11, 'float': 10, 'int': 6, 'long': 8, 'short': 4, 'unsigned_char': 3, 'unsigned_int': 7, 'unsigned_long': 9, 'unsigned_short': 5}), help=\
        """
        Control the scalar type of the output image. The default is
        VTK_BIT. NOTE: Not all filters/readers/writers support the
        VTK_BIT scalar type. You may want to use VTK_CHAR as an
        alternative.
        """
    )

    def _scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarType,
                        self.scalar_type_)

    background_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the Foreground/Background values of the output. The
        Foreground value is set when a voxel is occupied. The Background
        value is set when a voxel is not occupied. The default
        foreground_value is 1. The default background_value is 0.
        """
    )

    def _background_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundValue,
                        self.background_value)

    foreground_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the Foreground/Background values of the output. The
        Foreground value is set when a voxel is occupied. The Background
        value is set when a voxel is not occupied. The default
        foreground_value is 1. The default background_value is 0.
        """
    )

    def _foreground_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForegroundValue,
                        self.foreground_value)

    maximum_distance = traits.Trait(1.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Specify distance away from surface of input geometry to sample.
        Smaller values make large increases in performance. Default is
        1.0.
        """
    )

    def _maximum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistance,
                        self.maximum_distance)

    model_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        Specify the position in space to perform the voxelization.
        Default is (0, 0, 0, 0, 0, 0)
        """
    )

    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    sample_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(50, 50, 50), cols=3, help=\
        """
        Set the i-j-k dimensions on which to sample the distance
        function. Default is (50, 50, 50)
        """
    )

    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

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

    def compute_model_bounds(self, *args):
        """
        V.compute_model_bounds([float, float, float], [float, float, float])
             -> float
        C++: double ComputeModelBounds(double origin[3], double ar[3])
        Compute the model_bounds based on the input geometry.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeModelBounds, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('scalar_type',
    'GetScalarType'), ('background_value', 'GetBackgroundValue'),
    ('foreground_value', 'GetForegroundValue'), ('maximum_distance',
    'GetMaximumDistance'), ('model_bounds', 'GetModelBounds'),
    ('sample_dimensions', 'GetSampleDimensions'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_type', 'background_value',
    'foreground_value', 'maximum_distance', 'model_bounds',
    'progress_text', 'sample_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VoxelModeller, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VoxelModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['scalar_type'], ['background_value', 'foreground_value',
            'maximum_distance', 'model_bounds', 'sample_dimensions']),
            title='Edit VoxelModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VoxelModeller properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

