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


class AreaContourSpectrumFilter(DataObjectAlgorithm):
    """
    AreaContourSpectrumFilter - compute an approximation of the area
    contour signature (evolution of the area of the input surface along
    an arc of the Reeb graph).
    
    Superclass: DataObjectAlgorithm
    
    The filter takes a PolyData as an input (port 0), along with a
    ReebGraph (port 1). The Reeb graph arc to consider can be
    specified with set_arc_id() (default: 0). The number of (evenly
    distributed) samples of the signature can be defined with
    set_number_of_samples() (default value: 100). The filter will first try
    to pull as a scalar field the DataArray with Id '_field_id' of the
    PolyData, see set_field_id (default: 0). The filter will abort if
    this field does not exist.
    
    The filter outputs a Table with the area contour signature
    approximation, each sample being evenly distributed in the function
    span of the arc.
    
    This filter is a typical example for designing your own contour
    signature filter (with customized metrics). It also shows typical
    ReebGraph traversals.
    
    Reference: C. Bajaj, V. Pascucci, D. Schikore, "The contour
    spectrum", IEEE Visualization, 167-174, 1997.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAreaContourSpectrumFilter, obj, update, **traits)
    
    arc_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the arc Id for which the contour signature has to be
        computed. Default value: 0
        """
    )

    def _arc_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArcId,
                        self.arc_id)

    field_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the scalar field Id Default value: 0
        """
    )

    def _field_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldId,
                        self.field_id)

    number_of_samples = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        Set the number of samples in the output signature Default value:
        100
        """
    )

    def _number_of_samples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSamples,
                        self.number_of_samples)

    def _get_output(self):
        return wrap_vtk(self._vtk_obj.GetOutput())
    
    def _set_output(self, obj):
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)
    output = traits.Property(_get_output, _set_output,
                             help="Output of this source, i.e. the result of `get_output()`.")
    
    def get_output(self):
        """
        V.get_output() -> Table
        C++: Table *GetOutput()"""
        return wrap_vtk(self._vtk_obj.GetOutput())

    def set_output(self, obj):
        """
        V.set_output(DataObject)
        C++: virtual void SetOutput(DataObject *d)
        Get the output data object for a port on this algorithm.
        """
        old_val = self._get_output()
        self._wrap_call(self._vtk_obj.SetOutput, deref_vtk(obj))
        self.trait_property_changed('output', old_val, obj)

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
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('arc_id',
    'GetArcId'), ('field_id', 'GetFieldId'), ('number_of_samples',
    'GetNumberOfSamples'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'arc_id', 'field_id', 'number_of_samples',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AreaContourSpectrumFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AreaContourSpectrumFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['arc_id', 'field_id', 'number_of_samples']),
            title='Edit AreaContourSpectrumFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AreaContourSpectrumFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

