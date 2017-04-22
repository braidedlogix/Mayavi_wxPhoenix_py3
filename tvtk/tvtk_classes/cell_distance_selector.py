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

from tvtk.tvtk_classes.selection_algorithm import SelectionAlgorithm


class CellDistanceSelector(SelectionAlgorithm):
    """
    CellDistanceSelector - select neighbor cells up to a distance
    
    Superclass: SelectionAlgorithm
    
    This filter grows an input selection by iteratively selecting
    neighbor cells (a neighbor cell is a cell that shares a
    vertex/edge/face), up to a given topological distance to the selected
    neighborhood (number of times we add neighbor cells). This filter
    takes a Selection and a CompositeDataSet as inputs. It outputs
    a Selection identifying all the selected cells.
    
    @par Thanks: This file has been initially developed in the frame of
    CEA's Love visualization software development
    
    CEA/DIF - Commissariat a l'Energie Atomique, Centre DAM Ile-De-France
    
    BP12, F-91297 Arpajon, France.
    
    Modified and integrated into VTK, Kitware SAS 2012 Implementation by
    Thierry Carrard and Philippe Pebay
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellDistanceSelector, obj, update, **traits)
    
    add_intermediate = tvtk_base.true_bool_trait(help=\
        """
        If set, intermediate cells (between seed cells and the selection
        boundary) will be included in the final selection
        """
    )

    def _add_intermediate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAddIntermediate,
                        self.add_intermediate_)

    include_seed = tvtk_base.true_bool_trait(help=\
        """
        If set, seed cells passed with set_seed_cells will be included in
        the final selection
        """
    )

    def _include_seed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncludeSeed,
                        self.include_seed_)

    distance = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Tells how far (in term of topological distance) away from seed
        cells to expand the selection
        """
    )

    def _distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistance,
                        self.distance)

    def set_input_mesh(self, *args):
        """
        V.set_input_mesh(DataObject)
        C++: void SetInputMesh(DataObject *obj)
        A convenience method to set the input data object
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputMesh, *my_args)
        return ret

    def set_input_mesh_connection(self, *args):
        """
        V.set_input_mesh_connection(AlgorithmOutput)
        C++: void SetInputMeshConnection(AlgorithmOutput *in)
        A convenience method to set the data object input connection to
        the producer output
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputMeshConnection, *my_args)
        return ret

    def set_input_selection(self, *args):
        """
        V.set_input_selection(Selection)
        C++: void SetInputSelection(Selection *obj)
        A convenience method to set the input selection
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputSelection, *my_args)
        return ret

    def set_input_selection_connection(self, *args):
        """
        V.set_input_selection_connection(AlgorithmOutput)
        C++: void SetInputSelectionConnection(AlgorithmOutput *in)
        A convenience method to set the selection input connection to the
        producer output
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputSelectionConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('add_intermediate', 'GetAddIntermediate'), ('include_seed',
    'GetIncludeSeed'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('distance',
    'GetDistance'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'add_intermediate', 'debug',
    'global_warning_display', 'include_seed', 'release_data_flag',
    'distance', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellDistanceSelector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CellDistanceSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['add_intermediate', 'include_seed'], [], ['distance']),
            title='Edit CellDistanceSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellDistanceSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

