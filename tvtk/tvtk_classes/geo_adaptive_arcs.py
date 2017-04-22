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


class GeoAdaptiveArcs(PolyDataAlgorithm):
    """
    GeoAdaptiveArcs - no description provided.
    
    Superclass: PolyDataAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoAdaptiveArcs, obj, update, **traits)
    
    globe_radius = traits.Float(6356750.0, enter_set=True, auto_set=False, help=\
        """
        The base radius used to determine the earth's surface. Default is
        the earth's radius in meters. TODO: Change this to take in a
        GeoTerrain to get altitude.
        """
    )

    def _globe_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobeRadius,
                        self.globe_radius)

    maximum_pixel_separation = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        The maximum number of pixels between points on the arcs. If two
        adjacent points are farther than the threshold, the line segment
        will be subdivided such that each point is separated by at most
        the threshold.
        """
    )

    def _maximum_pixel_separation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumPixelSeparation,
                        self.maximum_pixel_separation)

    minimum_pixel_separation = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The minimum number of pixels between points on the arcs. Points
        closer than the threshold will be skipped until a point farther
        than the minimum threshold is reached.
        """
    )

    def _minimum_pixel_separation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumPixelSeparation,
                        self.minimum_pixel_separation)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        The renderer used to estimate the number of pixels between
        points.
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

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('globe_radius', 'GetGlobeRadius'), ('maximum_pixel_separation',
    'GetMaximumPixelSeparation'), ('minimum_pixel_separation',
    'GetMinimumPixelSeparation'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'globe_radius', 'maximum_pixel_separation',
    'minimum_pixel_separation', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoAdaptiveArcs, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoAdaptiveArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['globe_radius', 'maximum_pixel_separation',
            'minimum_pixel_separation']),
            title='Edit GeoAdaptiveArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoAdaptiveArcs properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

