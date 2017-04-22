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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class CellDataToPointData(DataSetAlgorithm):
    """
    CellDataToPointData - map cell data to point data
    
    Superclass: DataSetAlgorithm
    
    CellDataToPointData is a filter that transforms cell data (i.e.,
    data specified per cell) into point data (i.e., data specified at
    cell points). The method of transformation is based on averaging the
    data values of all cells using a particular point. Optionally, the
    input cell data can be passed through to the output as well.
    
    @warning
    This filter is an abstract filter, that is, the output is an abstract
    type (i.e., DataSet). Use the convenience methods (e.g.,
    get_poly_data_output(), get_structured_points_output(), etc.) to get the
    type of output you want.
    
    @sa
    PointData CellData PointDataToCellData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellDataToPointData, obj, update, **traits)
    
    pass_cell_data = tvtk_base.false_bool_trait(help=\
        """
        Control whether the input cell data is to be passed to the
        output. If on, then the input cell data is passed through to the
        output; otherwise, only generated point data is placed into the
        output.
        """
    )

    def _pass_cell_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassCellData,
                        self.pass_cell_data_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('pass_cell_data', 'GetPassCellData'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_cell_data', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellDataToPointData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CellDataToPointData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_cell_data'], [], []),
            title='Edit CellDataToPointData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellDataToPointData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

