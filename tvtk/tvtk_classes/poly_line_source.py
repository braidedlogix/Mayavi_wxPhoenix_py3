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


class PolyLineSource(PolyDataAlgorithm):
    """
    PolyLineSource - create a poly line from a list of input points
    
    Superclass: PolyDataAlgorithm
    
    PolyLineSource is a source object that creates a poly line from
    user-specified points. The output is a PolyLine.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyLineSource, obj, update, **traits)
    
    closed = tvtk_base.false_bool_trait(help=\
        """
        Set whether to close the poly line by connecting the last and
        first points.
        """
    )

    def _closed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClosed,
                        self.closed_)

    number_of_points = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the number of points in the poly line.
        """
    )

    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    def _set_points(self, arg):
        old_val = self._get_points()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetPoints,
                        my_arg[0])
        self.trait_property_changed('points', old_val, arg)
    points = traits.Property(_get_points, _set_points, help=\
        """
        Get the points.
        """
    )

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

    def resize(self, *args):
        """
        V.resize(int)
        C++: void Resize(IdType numPoints)
        Resize while preserving data.
        """
        ret = self._wrap_call(self._vtk_obj.Resize, *args)
        return ret

    def set_point(self, *args):
        """
        V.set_point(int, float, float, float)
        C++: void SetPoint(IdType id, double x, double y, double z)
        Set a point location.
        """
        ret = self._wrap_call(self._vtk_obj.SetPoint, *args)
        return ret

    _updateable_traits_ = \
    (('closed', 'GetClosed'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_points', 'GetNumberOfPoints'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'closed', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_points', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyLineSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyLineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['closed'], [], ['number_of_points']),
            title='Edit PolyLineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyLineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

