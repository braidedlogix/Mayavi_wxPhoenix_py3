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


class SelectVisiblePoints(PolyDataAlgorithm):
    """
    SelectVisiblePoints - extract points that are visible (based on
    z-buffer calculation)
    
    Superclass: PolyDataAlgorithm
    
    SelectVisiblePoints is a filter that selects points based on
    whether they are visible or not. Visibility is determined by
    accessing the z-buffer of a rendering window. (The position of each
    input point is converted into display coordinates, and then the
    z-value at that point is obtained. If within the user-specified
    tolerance, the point is considered visible.)
    
    Points that are visible (or if the ivar select_invisible is on,
    invisible points) are passed to the output. Associated data
    attributes are passed to the output as well.
    
    This filter also allows you to specify a rectangular window in
    display (pixel) coordinates in which the visible points must lie.
    This can be used as a sort of local "brushing" operation to select
    just data within a window.
    
    @warning
    You must carefully synchronize the execution of this filter. The
    filter refers to a renderer, which is modified every time a render
    occurs. Therefore, the filter is always out of date, and always
    executes. You may have to perform two rendering passes, or if you are
    using this filter in conjunction with LabeledDataMapper, things
    work out because 2d rendering occurs after the 3d rendering.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSelectVisiblePoints, obj, update, **traits)
    
    select_invisible = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag which enables inverse selection; i.e., invisible
        points are selected.
        """
    )

    def _select_invisible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectInvisible,
                        self.select_invisible_)

    selection_window = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the flag which enables selection in a rectangular display
        region.
        """
    )

    def _selection_window_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionWindow,
                        self.selection_window_)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Specify the renderer in which the visibility computation is to be
        performed.
        """
    )

    selection = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=int, value=(0, 1600, 0, 1600), cols=3, help=\
        """
        
        """
    )

    def _selection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelection,
                        self.selection)

    tolerance = traits.Trait(0.01, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set/Get a tolerance to use to determine whether a point is
        visible. A tolerance is usually required because the conversion
        from world space to display space during rendering introduces
        numerical round-off.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

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

    def initialize(self, *args):
        """
        V.initialize(bool) -> (float, ...)
        C++: float *Initialize(bool getZbuff)
        Requires the renderer to be set. Populates the composite
        perspective transform and returns a pointer to the Z-buffer (that
        must be deleted) if get_zbuff is set.
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    def is_point_occluded(self, *args):
        """
        V.is_point_occluded((float, float, float), (float, ...)) -> bool
        C++: bool IsPointOccluded(const double x[3], const float *zPtr)
        Tests if a point x is being occluded or not against the Z-Buffer
        array passed in by z_ptr. Call Initialize before calling this
        method.
        """
        ret = self._wrap_call(self._vtk_obj.IsPointOccluded, *args)
        return ret

    _updateable_traits_ = \
    (('select_invisible', 'GetSelectInvisible'), ('selection_window',
    'GetSelectionWindow'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('selection',
    'GetSelection'), ('tolerance', 'GetTolerance'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'select_invisible', 'selection_window',
    'progress_text', 'selection', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SelectVisiblePoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SelectVisiblePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['select_invisible', 'selection_window'], [], ['selection',
            'tolerance']),
            title='Edit SelectVisiblePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SelectVisiblePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

