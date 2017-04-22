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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class RecursiveDividingCubes(PolyDataAlgorithm):
    """
    RecursiveDividingCubes - create points laying on isosurface (using
    recursive approach)
    
    Superclass: PolyDataAlgorithm
    
    RecursiveDividingCubes is a filter that generates points laying on
    a surface of constant scalar value (i.e., an isosurface). Dense point
    clouds (i.e., at screen resolution) will appear as a surface. Less
    dense clouds can be used as a source to generate streamlines or to
    generate "transparent" surfaces.
    
    This implementation differs from DividingCubes in that it uses a
    recursive procedure. In many cases this can result in generating more
    points than the procedural implementation of DividingCubes. This
    is because the recursive procedure divides voxels by multiples of
    powers of two. This can over-constrain subdivision. One of the
    advantages of the recursive technique is that the recursion is
    terminated earlier, which in some cases can be more efficient.
    
    @sa
    DividingCubes ContourFilter MarchingCubes
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRecursiveDividingCubes, obj, update, **traits)
    
    distance = traits.Trait(0.1, traits.Range(1e-06, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify sub-voxel size at which to generate point.
        """
    )

    def _distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistance,
                        self.distance)

    increment = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Every "Increment" point is added to the list of points. This
        parameter, if set to a large value, can be used to limit the
        number of points while retaining good accuracy.
        """
    )

    def _increment_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncrement,
                        self.increment)

    value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set isosurface value.
        """
    )

    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('distance',
    'GetDistance'), ('increment', 'GetIncrement'), ('value', 'GetValue'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'distance', 'increment', 'progress_text',
    'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RecursiveDividingCubes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RecursiveDividingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['distance', 'increment', 'value']),
            title='Edit RecursiveDividingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RecursiveDividingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

