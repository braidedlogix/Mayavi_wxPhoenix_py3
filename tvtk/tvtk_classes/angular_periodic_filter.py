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

from tvtk.tvtk_classes.periodic_filter import PeriodicFilter


class AngularPeriodicFilter(PeriodicFilter):
    """
    AngularPeriodicFilter - A filter to produce mapped angular
    periodic multiblock dataset from a single block, by rotation.
    
    Superclass: PeriodicFilter
    
    Generate angular periodic dataset by rotating points, vectors and
    tensors data arrays from an original data array. The generated
    dataset is of the same type than the input (float or double). To
    compute the rotation this filter needs i) a number of periods, wich
    can be the maximum, i.e. a full period, ii) an angle, wich can be
    fetched from a field data array in radian or directly in degrees;
    iii) the axis (X, Y or Z) and the center of rotation. Point
    coordinates are transformed, as well as all vectors (3-components)
    and tensors (9 components) in points and cell data arrays. The
    generated multiblock will have the same tree architecture than the
    input, except transformed leaves are replaced by a
    MultipieceDataSet. Supported input leaf dataset type are:
    PolyData, StructuredGrid and UnstructuredGrid. Other data
    objects are rotated using the transform filter (at a high cost!).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAngularPeriodicFilter, obj, update, **traits)
    
    compute_rotations_on_the_fly = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether the rotated array values should be computed
        on-the-fly (default), which is compute-intensive, or the arrays
        should be explicitly generated and stored, at the cost of using
        more memory.
        """
    )

    def _compute_rotations_on_the_fly_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeRotationsOnTheFly,
                        self.compute_rotations_on_the_fly_)

    rotation_axis = traits.Trait('x',
    tvtk_base.TraitRevPrefixMap({'x': 0, 'y': 1, 'z': 2}), help=\
        """
        Set/Get Rotation Axis, 0 for X, 1 for Y, 2 for Z
        """
    )

    def _rotation_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationAxis,
                        self.rotation_axis_)

    rotation_mode = traits.Trait('direct_angle',
    tvtk_base.TraitRevPrefixMap({'direct_angle': 0, 'array_value': 1}), help=\
        """
        Set/Get The rotation mode. VTK_ROTATION_MODE_DIRECT_ANGLE to
        specifiy a angle value (default), VTK_ROTATION_MODE_ARRAY_VALUE
        to use value from an array in the input dataset.
        """
    )

    def _rotation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationMode,
                        self.rotation_mode_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    rotation_angle = traits.Float(180.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get Rotation angle, in degrees. Used only with
        VTK_ROTATION_MODE_DIRECT_ANGLE. Default is 180.
        """
    )

    def _rotation_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationAngle,
                        self.rotation_angle)

    rotation_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get Name of array to get the angle from. Used only with
        VTK_ROTATION_MODE_ARRAY_VALUE.
        """
    )

    def _rotation_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRotationArrayName,
                        self.rotation_array_name)

    _updateable_traits_ = \
    (('compute_rotations_on_the_fly', 'GetComputeRotationsOnTheFly'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('rotation_axis', 'GetRotationAxis'), ('rotation_mode',
    'GetRotationMode'), ('iteration_mode', 'GetIterationMode'), ('center',
    'GetCenter'), ('rotation_angle', 'GetRotationAngle'),
    ('rotation_array_name', 'GetRotationArrayName'), ('number_of_periods',
    'GetNumberOfPeriods'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_rotations_on_the_fly', 'debug',
    'global_warning_display', 'release_data_flag', 'iteration_mode',
    'rotation_axis', 'rotation_mode', 'center', 'number_of_periods',
    'progress_text', 'rotation_angle', 'rotation_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AngularPeriodicFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AngularPeriodicFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_rotations_on_the_fly'], ['iteration_mode',
            'rotation_axis', 'rotation_mode'], ['center', 'number_of_periods',
            'rotation_angle', 'rotation_array_name']),
            title='Edit AngularPeriodicFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AngularPeriodicFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

