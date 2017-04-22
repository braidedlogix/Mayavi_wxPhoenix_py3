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


class ReverseSense(PolyDataAlgorithm):
    """
    ReverseSense - reverse the ordering of polygonal cells and/or
    vertex normals
    
    Superclass: PolyDataAlgorithm
    
    ReverseSense is a filter that reverses the order of polygonal
    cells and/or reverses the direction of point and cell normals. Two
    flags are used to control these operations. Cell reversal means
    reversing the order of indices in the cell connectivity list. Normal
    reversal means multiplying the normal vector by -1 (both point and
    cell normals, if present).
    
    @warning
    Normals can be operated on only if they are present in the data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkReverseSense, obj, update, **traits)
    
    reverse_cells = tvtk_base.true_bool_trait(help=\
        """
        Flag controls whether to reverse cell ordering.
        """
    )

    def _reverse_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseCells,
                        self.reverse_cells_)

    reverse_normals = tvtk_base.false_bool_trait(help=\
        """
        Flag controls whether to reverse normal orientation.
        """
    )

    def _reverse_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverseNormals,
                        self.reverse_normals_)

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
    (('reverse_cells', 'GetReverseCells'), ('reverse_normals',
    'GetReverseNormals'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'reverse_cells', 'reverse_normals',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ReverseSense, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ReverseSense properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['reverse_cells', 'reverse_normals'], [], []),
            title='Edit ReverseSense properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ReverseSense properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

