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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class ReflectionFilter(DataObjectAlgorithm):
    """
    ReflectionFilter - reflects a data set across a plane
    
    Superclass: DataObjectAlgorithm
    
    The ReflectionFilter reflects a data set across one of the planes
    formed by the data set's bounding box. Since it converts data sets
    into unstructured grids, it is not effeicient for structured data
    sets.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkReflectionFilter, obj, update, **traits)
    
    copy_input = tvtk_base.true_bool_trait(help=\
        """
        If on (the default), copy the input geometry to the output. If
        off, the output will only contain the reflection.
        """
    )

    def _copy_input_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyInput,
                        self.copy_input_)

    plane = traits.Trait('x_min',
    tvtk_base.TraitRevPrefixMap({'x_min': 0, 'x': 6, 'x_max': 3, 'y': 7, 'y_max': 4, 'y_min': 1, 'z': 8, 'z_max': 5, 'z_min': 2}), help=\
        """
        Set the normal of the plane to use as mirror.
        """
    )

    def _plane_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPlane,
                        self.plane_)

    center = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        If the reflection plane is set to X, Y or Z, this variable is use
        to set the position of the plane.
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

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
    (('copy_input', 'GetCopyInput'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('plane',
    'GetPlane'), ('center', 'GetCenter'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'copy_input', 'debug', 'global_warning_display',
    'release_data_flag', 'plane', 'center', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ReflectionFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ReflectionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['copy_input'], ['plane'], ['center']),
            title='Edit ReflectionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ReflectionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

