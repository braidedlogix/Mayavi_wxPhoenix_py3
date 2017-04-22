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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class RotationFilter(UnstructuredGridAlgorithm):
    """
    RotationFilter - Duplicates a data set by rotation about an axis
    
    Superclass: UnstructuredGridAlgorithm
    
    The RotationFilter duplicates a data set by rotation about one of
    the 3 axis of the dataset's reference. Since it converts data sets
    into unstructured grids, it is not efficient for structured data
    sets.
    
    @par Thanks: Theophane Foggia of The Swiss National Supercomputing
    Centre (CSCS) for creating and contributing this filter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRotationFilter, obj, update, **traits)
    
    copy_input = tvtk_base.false_bool_trait(help=\
        """
        If on (the default), copy the input geometry to the output. If
        off, the output will only contain the rotation.
        """
    )

    def _copy_input_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCopyInput,
                        self.copy_input_)

    axis = traits.Trait('z',
    tvtk_base.TraitRevPrefixMap({'z': 2, 'x': 0, 'y': 1}), help=\
        """
        Set the axis of rotation to use. It is set by default to Z.
        """
    )

    def _axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxis,
                        self.axis_)

    angle = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the rotation angle to use.
        """
    )

    def _angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngle,
                        self.angle)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    number_of_copies = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of copies to create. The source will be rotated N
        times and a new polydata copy of the original created at each
        angular position All copies will be appended to form a single
        output
        """
    )

    def _number_of_copies_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfCopies,
                        self.number_of_copies)

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
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('copy_input', 'GetCopyInput'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('axis',
    'GetAxis'), ('angle', 'GetAngle'), ('center', 'GetCenter'),
    ('number_of_copies', 'GetNumberOfCopies'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'copy_input', 'debug', 'global_warning_display',
    'release_data_flag', 'axis', 'angle', 'center', 'number_of_copies',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RotationFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RotationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['copy_input'], ['axis'], ['angle', 'center',
            'number_of_copies']),
            title='Edit RotationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RotationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

