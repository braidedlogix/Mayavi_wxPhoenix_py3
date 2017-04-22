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

from tvtk.tvtk_classes.structured_grid_algorithm import StructuredGridAlgorithm


class BlankStructuredGrid(StructuredGridAlgorithm):
    """
    BlankStructuredGrid - translate point attribute data into a
    blanking field
    
    Superclass: StructuredGridAlgorithm
    
    BlankStructuredGrid is a filter that sets the blanking field in a
    StructuredGrid dataset. The blanking field is set by examining a
    specified point attribute data array (e.g., scalars) and converting
    values in the data array to either a "1" (visible) or "0" (blanked)
    value in the blanking array. The values to be blanked are specified
    by giving a min/max range. All data values in the data array
    indicated and laying within the range specified (inclusive on both
    ends) are translated to a "off" blanking value.
    
    @sa
    StructuredGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBlankStructuredGrid, obj, update, **traits)
    
    array_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Specify the data array id to use to generate the blanking field.
        Alternatively, you can specify the array name. (If both are set,
        the array name takes precedence.)
        """
    )

    def _array_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayId,
                        self.array_id)

    array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the data array name to use to generate the blanking
        field. Alternatively, you can specify the array id. (If both are
        set, the array name takes precedence.)
        """
    )

    def _array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayName,
                        self.array_name)

    component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the component in the data array to use to generate the
        blanking field.
        """
    )

    def _component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponent,
                        self.component)

    max_blanking_value = traits.Float(9.999999680285692e+37, enter_set=True, auto_set=False, help=\
        """
        Specify the upper data value in the data array specified which
        will be converted into a "blank" (or off) value in the blanking
        array.
        """
    )

    def _max_blanking_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxBlankingValue,
                        self.max_blanking_value)

    min_blanking_value = traits.Float(9.999999680285692e+37, enter_set=True, auto_set=False, help=\
        """
        Specify the lower data value in the data array specified which
        will be converted into a "blank" (or off) value in the blanking
        array.
        """
    )

    def _min_blanking_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinBlankingValue,
                        self.min_blanking_value)

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
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('array_id',
    'GetArrayId'), ('array_name', 'GetArrayName'), ('component',
    'GetComponent'), ('max_blanking_value', 'GetMaxBlankingValue'),
    ('min_blanking_value', 'GetMinBlankingValue'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'array_id', 'array_name', 'component',
    'max_blanking_value', 'min_blanking_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BlankStructuredGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BlankStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['array_id', 'array_name', 'component',
            'max_blanking_value', 'min_blanking_value']),
            title='Edit BlankStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BlankStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

