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


class DistanceToCamera(PolyDataAlgorithm):
    """
    DistanceToCamera - calculates distance from points to the camera.
    
    Superclass: PolyDataAlgorithm
    
    This filter adds a double array containing the distance from each
    point to the camera. If Scaling is on, it will use the values in the
    input array to process in order to scale the size of the points.
    screen_size sets the size in screen pixels that you would want a
    rendered rectangle at that point to be, if it was scaled by the
    output array.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDistanceToCamera, obj, update, **traits)
    
    scaling = tvtk_base.false_bool_trait(help=\
        """
        Whether to scale the distance by the input array to process.
        """
    )

    def _scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaling,
                        self.scaling_)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        The renderer which will ultimately render these points.
        """
    )

    screen_size = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        The desired screen size obtained by scaling glyphs by the
        distance array. It assumes the glyph at each point will be unit
        size.
        """
    )

    def _screen_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenSize,
                        self.screen_size)

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
    (('scaling', 'GetScaling'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('screen_size',
    'GetScreenSize'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scaling', 'progress_text', 'screen_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DistanceToCamera, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DistanceToCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['scaling'], [], ['screen_size']),
            title='Edit DistanceToCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DistanceToCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

