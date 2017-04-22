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


class EarthSource(PolyDataAlgorithm):
    """
    EarthSource - create the continents of the Earth as a sphere
    
    Superclass: PolyDataAlgorithm
    
    EarthSource creates a spherical rendering of the geographical
    shapes of the major continents of the earth. The on_ratio determines
    how much of the data is actually used. The radius defines the radius
    of the sphere at which the continents are placed. Obtains data from
    an imbedded array of coordinates.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEarthSource, obj, update, **traits)
    
    outline = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off drawing continents as filled polygons or as wireframe
        outlines. Warning: some graphics systems will have trouble with
        the very large, concave filled polygons. Recommend you use
        outlien_on (i.e., disable filled polygons) for now.
        """
    )

    def _outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutline,
                        self.outline_)

    on_ratio = traits.Trait(10, traits.Range(1, 16, enter_set=True, auto_set=False), help=\
        """
        Turn on every nth entity. This controls how much detail the model
        will have. The maximum ratio is sixteen. (The smaller on_ratio,
        the more detail there is.)
        """
    )

    def _on_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOnRatio,
                        self.on_ratio)

    radius = traits.Trait(1.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Set radius of earth.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

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
    (('outline', 'GetOutline'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('on_ratio',
    'GetOnRatio'), ('radius', 'GetRadius'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'outline',
    'release_data_flag', 'on_ratio', 'progress_text', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EarthSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EarthSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['outline'], [], ['on_ratio', 'radius']),
            title='Edit EarthSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EarthSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

