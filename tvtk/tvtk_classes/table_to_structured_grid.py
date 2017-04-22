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


class TableToStructuredGrid(StructuredGridAlgorithm):
    """
    TableToStructuredGrid - converts Table to a StructuredGrid.
    
    Superclass: StructuredGridAlgorithm
    
    TableToStructuredGrid is a filter that converts an input Table
    to a StructuredGrid. It provides API to select columns to use as
    points in the output structured grid. The specified dimensions of the
    output (specified using set_whole_extent()) must match the number of
    rows in the input table.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableToStructuredGrid, obj, update, **traits)
    
    whole_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, 0, 0, 0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    x_column = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the column to use as the X coordinate for the
        points.
        """
    )

    def _x_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXColumn,
                        self.x_column)

    x_component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the component for the column specified using set_x_column()
        to use as the xcoordinate in case the column is a multi-component
        array. Default is 0.
        """
    )

    def _x_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXComponent,
                        self.x_component)

    y_column = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the column to use as the Y coordinate for the
        points. Default is 0.
        """
    )

    def _y_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYColumn,
                        self.y_column)

    y_component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the component for the column specified using set_y_column()
        to use as the Ycoordinate in case the column is a multi-component
        array.
        """
    )

    def _y_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYComponent,
                        self.y_component)

    z_column = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the column to use as the Z coordinate for the
        points. Default is 0.
        """
    )

    def _z_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZColumn,
                        self.z_column)

    z_component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the component for the column specified using set_z_column()
        to use as the Zcoordinate in case the column is a multi-component
        array.
        """
    )

    def _z_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZComponent,
                        self.z_component)

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
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('whole_extent', 'GetWholeExtent'), ('x_column', 'GetXColumn'),
    ('x_component', 'GetXComponent'), ('y_column', 'GetYColumn'),
    ('y_component', 'GetYComponent'), ('z_column', 'GetZColumn'),
    ('z_component', 'GetZComponent'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'whole_extent', 'x_column',
    'x_component', 'y_column', 'y_component', 'z_column', 'z_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableToStructuredGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TableToStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['whole_extent', 'x_column', 'x_component', 'y_column',
            'y_component', 'z_column', 'z_component']),
            title='Edit TableToStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableToStructuredGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

