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

from tvtk.tvtk_classes.algorithm import Algorithm


class TransformToGrid(Algorithm):
    """
    TransformToGrid - create a grid for a GridTransform
    
    Superclass: Algorithm
    
    TransformToGrid takes any transform as input and produces a grid
    for use by a GridTransform.  This can be used, for example, to
    invert a grid transform, concatenate two grid transforms, or to
    convert a thin plate spline transform into a grid transform.
    @sa
    GridTransform ThinPlateSplineTransform AbstractTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransformToGrid, obj, update, **traits)
    
    grid_scalar_type = traits.Trait('float',
    tvtk_base.TraitRevPrefixMap({'float': 10, 'char': 2, 'double': 11, 'short': 4, 'unsigned_char': 3, 'unsigned_short': 5}), help=\
        """
        Get/Set the scalar type of the grid.  The default is float.
        """
    )

    def _grid_scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridScalarType,
                        self.grid_scalar_type_)

    grid_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, 0, 0, 0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _grid_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridExtent,
                        self.grid_extent)

    grid_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _grid_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridOrigin,
                        self.grid_origin)

    grid_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _grid_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridSpacing,
                        self.grid_spacing)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        Set/Get the transform which will be converted into a grid.
        """
    )

    def _get_displacement_scale(self):
        return self._vtk_obj.GetDisplacementScale()
    displacement_scale = traits.Property(_get_displacement_scale, help=\
        """
        Get the scale and shift to convert integer grid elements into
        real values:  dx = scale*di + shift.  If the grid is of double
        type, then scale = 1 and shift = 0.
        """
    )

    def _get_displacement_shift(self):
        return self._vtk_obj.GetDisplacementShift()
    displacement_shift = traits.Property(_get_displacement_shift, help=\
        """
        Get the scale and shift to convert integer grid elements into
        real values:  dx = scale*di + shift.  If the grid is of double
        type, then scale = 1 and shift = 0.
        """
    )

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    output = traits.Property(_get_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self):
        """
        V.get_output() -> ImageData
        C++: ImageData *GetOutput()
        Get the output data object for a port on this algorithm.
        """
        return wrap_vtk(self._vtk_obj.GetOutput())

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('grid_scalar_type', 'GetGridScalarType'), ('grid_extent',
    'GetGridExtent'), ('grid_origin', 'GetGridOrigin'), ('grid_spacing',
    'GetGridSpacing'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'grid_scalar_type', 'grid_extent', 'grid_origin',
    'grid_spacing', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TransformToGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TransformToGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['grid_scalar_type'], ['grid_extent', 'grid_origin',
            'grid_spacing']),
            title='Edit TransformToGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TransformToGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

