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


class ExtractCells(UnstructuredGridAlgorithm):
    """
    ExtractCells - subset a DataSet to create a UnstructuredGrid
    
    Superclass: UnstructuredGridAlgorithm
    
    Given a DataSet and a list of cell Ids, create a
    UnstructuredGrid
       composed of these cells.  If the cell list is empty when
    ExtractCells
       executes, it will set up the ugrid, point and cell arrays, with no
    points,
       cells or data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractCells, obj, update, **traits)
    
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

    def add_cell_list(self, *args):
        """
        V.add_cell_list(IdList)
        C++: void AddCellList(IdList *l)
        Add the supplied list of cell IDs to those that will be included
        in the output UnstructuredGrid.
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.AddCellList, *my_args)
        return ret

    def add_cell_range(self, *args):
        """
        V.add_cell_range(int, int)
        C++: void AddCellRange(IdType from, IdType to)
        Add this range of cell IDs to those that will be included in the
        output UnstructuredGrid.
        """
        ret = self._wrap_call(self._vtk_obj.AddCellRange, *args)
        return ret

    def set_cell_list(self, *args):
        """
        V.set_cell_list(IdList)
        C++: void SetCellList(IdList *l)
        Set the list of cell IDs that the output UnstructuredGrid will
        be composed of.  Replaces any other cell ID list supplied so far.
         (Set to NULL to free memory used by cell list.)
        """
        my_args = deref_array(args, [['vtkIdList']])
        ret = self._wrap_call(self._vtk_obj.SetCellList, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractCells, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ExtractCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractCells properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

