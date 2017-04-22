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

from tvtk.tvtk_classes.point_set_algorithm import PointSetAlgorithm


class CenterOfMass(PointSetAlgorithm):
    """
    CenterOfMass - Find the center of mass of a set of points.
    
    Superclass: PointSetAlgorithm
    
    CenterOfMass finds the "center of mass" of a PointSet
    (vtk_poly_data or UnstructuredGrid). Optionally, the user can
    specify to use the scalars as weights in the computation. If this
    option, use_scalars_as_weights, is off, each point contributes equally
    in the calculation.
    
    You must ensure Update() has been called before get_center will
    produce a valid value.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCenterOfMass, obj, update, **traits)
    
    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    use_scalars_as_weights = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Set a flag to determine if the points are weighted.
        """
    )

    def _use_scalars_as_weights_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseScalarsAsWeights,
                        self.use_scalars_as_weights)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        
        """
    )

    def compute_center_of_mass(self, *args):
        """
        V.compute_center_of_mass(Points, DataArray, [float, float,
            float])
        C++: static void ComputeCenterOfMass(Points *input,
            DataArray *scalars, double center[3])
        This function is called by request_data. It exists so that other
        classes may use this computation without constructing a
        CenterOfMass object.  The scalars can be set to NULL if all
        points are to be weighted equally.  If scalars are used, it is
        the caller's responsibility to ensure that the number of scalars
        matches the number of points, and that the sum of the scalars is
        a positive value.
        """
        my_args = deref_array(args, [('vtkPoints', 'vtkDataArray', ['float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.ComputeCenterOfMass, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('use_scalars_as_weights', 'GetUseScalarsAsWeights'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'progress_text',
    'use_scalars_as_weights'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CenterOfMass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CenterOfMass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['center', 'use_scalars_as_weights']),
            title='Edit CenterOfMass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CenterOfMass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

