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

from tvtk.tvtk_classes.warp_transform import WarpTransform


class GridTransform(WarpTransform):
    """
    GridTransform - a nonlinear warp transformation
    
    Superclass: WarpTransform
    
    GridTransform describes a nonlinear warp transformation as a set
    of displacement vectors sampled along a uniform 3d grid.
    @warning
    The inverse grid transform is calculated using an iterative method,
    and is several times more expensive than the forward transform.
    @sa
    ThinPlateSplineTransform GeneralTransform TransformToGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGridTransform, obj, update, **traits)
    
    interpolation_mode = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'linear': 1, 'cubic': 2, 'nearest_neighbor': 0}), help=\
        """
        Set interpolation mode for sampling the grid.  Higher-order
        interpolation allows you to use a sparser grid. Default: Linear.
        """
    )

    def _interpolation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationMode,
                        self.interpolation_mode_)

    displacement_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set scale factor to be applied to the displacements. This is used
        primarily for grids which contain integer data types.  Default: 1
        """
    )

    def _displacement_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementScale,
                        self.displacement_scale)

    displacement_shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set a shift to be applied to the displacements.  The shift is
        applied after the scale, i.e. x = scale*y + shift. Default: 0
        """
    )

    def _displacement_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementShift,
                        self.displacement_shift)

    def _get_displacement_grid(self):
        return wrap_vtk(self._vtk_obj.GetDisplacementGrid())
    displacement_grid = traits.Property(_get_displacement_grid, help=\
        """
        Set/Get the grid transform (the grid transform must have three
        components for displacement in x, y, and z respectively). The
        GridTransform class will never modify the data. Note that
        set_displacement_grid_data() does not setup a pipeline connection
        whereas set_displacement_grid_connection does.
        """
    )

    def set_displacement_grid_connection(self, *args):
        """
        V.set_displacement_grid_connection(AlgorithmOutput)
        C++: virtual void SetDisplacementGridConnection(
            AlgorithmOutput *)
        Set/Get the grid transform (the grid transform must have three
        components for displacement in x, y, and z respectively). The
        GridTransform class will never modify the data. Note that
        set_displacement_grid_data() does not setup a pipeline connection
        whereas set_displacement_grid_connection does.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDisplacementGridConnection, *my_args)
        return ret

    def set_displacement_grid_data(self, *args):
        """
        V.set_displacement_grid_data(ImageData)
        C++: virtual void SetDisplacementGridData(ImageData *)
        Set/Get the grid transform (the grid transform must have three
        components for displacement in x, y, and z respectively). The
        GridTransform class will never modify the data. Note that
        set_displacement_grid_data() does not setup a pipeline connection
        whereas set_displacement_grid_connection does.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDisplacementGridData, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolation_mode',
    'GetInterpolationMode'), ('displacement_scale',
    'GetDisplacementScale'), ('displacement_shift',
    'GetDisplacementShift'), ('inverse_iterations',
    'GetInverseIterations'), ('inverse_tolerance', 'GetInverseTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interpolation_mode',
    'displacement_scale', 'displacement_shift', 'inverse_iterations',
    'inverse_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GridTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GridTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['interpolation_mode'], ['displacement_scale',
            'displacement_shift', 'inverse_iterations', 'inverse_tolerance']),
            title='Edit GridTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GridTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

