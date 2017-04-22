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


class TableToPolyData(PolyDataAlgorithm):
    """
    TableToPolyData - filter used to convert a Table to a
    PolyData consisting of vertices.
    
    Superclass: PolyDataAlgorithm
    
    TableToPolyData is a filter used to convert a Table  to a
    PolyData consisting of vertices.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableToPolyData, obj, update, **traits)
    
    create2d_points = tvtk_base.false_bool_trait(help=\
        """
        Specify whether the points of the polydata are 3d or 2d. If this
        is set to true then the Z Column will be ignored and the z value
        of each point on the polydata will be set to 0. By default this
        will be off.
        """
    )

    def _create2d_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCreate2DPoints,
                        self.create2d_points_)

    preserve_coordinate_columns_as_data_arrays = tvtk_base.false_bool_trait(help=\
        """
        Allow user to keep columns specified as X,Y,Z as Data arrays. By
        default this will be off.
        """
    )

    def _preserve_coordinate_columns_as_data_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreserveCoordinateColumnsAsDataArrays,
                        self.preserve_coordinate_columns_as_data_arrays_)

    x_column = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the name of the column to use as the X coordinate for the
        points.
        """
    )

    def _x_column_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXColumn,
                        self.x_column)

    x_column_index = traits.Trait(-1, traits.Range(-1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the index of the column to use as the X coordinate for the
        points.
        """
    )

    def _x_column_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXColumnIndex,
                        self.x_column_index)

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

    y_column_index = traits.Trait(-1, traits.Range(-1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the index of the column to use as the Y coordinate for the
        points.
        """
    )

    def _y_column_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYColumnIndex,
                        self.y_column_index)

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

    z_column_index = traits.Trait(-1, traits.Range(-1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the index of the column to use as the Z coordinate for the
        points.
        """
    )

    def _z_column_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZColumnIndex,
                        self.z_column_index)

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
    (('create2d_points', 'GetCreate2DPoints'),
    ('preserve_coordinate_columns_as_data_arrays',
    'GetPreserveCoordinateColumnsAsDataArrays'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('x_column', 'GetXColumn'),
    ('x_column_index', 'GetXColumnIndex'), ('x_component',
    'GetXComponent'), ('y_column', 'GetYColumn'), ('y_column_index',
    'GetYColumnIndex'), ('y_component', 'GetYComponent'), ('z_column',
    'GetZColumn'), ('z_column_index', 'GetZColumnIndex'), ('z_component',
    'GetZComponent'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'create2d_points', 'debug',
    'global_warning_display',
    'preserve_coordinate_columns_as_data_arrays', 'release_data_flag',
    'progress_text', 'x_column', 'x_column_index', 'x_component',
    'y_column', 'y_column_index', 'y_component', 'z_column',
    'z_column_index', 'z_component'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableToPolyData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TableToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['create2d_points',
            'preserve_coordinate_columns_as_data_arrays'], [], ['x_column',
            'x_column_index', 'x_component', 'y_column', 'y_column_index',
            'y_component', 'z_column', 'z_column_index', 'z_component']),
            title='Edit TableToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableToPolyData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

