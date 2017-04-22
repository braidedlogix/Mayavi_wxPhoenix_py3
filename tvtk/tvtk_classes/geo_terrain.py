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

from tvtk.tvtk_classes.object import Object


class GeoTerrain(Object):
    """
    GeoTerrain - A 3d terrain model for the globe.
    
    Superclass: Object
    
    GeoTerrain contains a multi-resolution tree of geometry
    representing the globe. It uses a GeoSource subclass to generate
    the terrain, such as GeoGlobeSource. This source must be set
    before using the terrain in a GeoView. The terrain also contains
    an add_actors() method which will update the set of actors
    representing the globe given the current camera position.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoTerrain, obj, update, **traits)
    
    max_level = traits.Trait(20, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        The maximum level of the terrain tree.
        """
    )

    def _max_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxLevel,
                        self.max_level)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        The source used to obtain geometry patches.
        """
    )

    def add_actors(self, *args):
        """
        V.add_actors(Renderer, Assembly, Collection)
        C++: void AddActors(Renderer *ren, Assembly *assembly,
            Collection *imageReps)
        Update the actors in an assembly used to render the globe. ren is
        the current renderer, and image_reps holds the collection of
        GeoAlignedImageRepresentations that will be blended together
        to form the image on the globe.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddActors, *my_args)
        return ret

    def save_database(self, *args):
        """
        V.save_database(string, int)
        C++: void SaveDatabase(const char *path, int depth)
        Save the set of patches up to a given maximum depth.
        """
        ret = self._wrap_call(self._vtk_obj.SaveDatabase, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('max_level', 'GetMaxLevel'), ('origin',
    'GetOrigin'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'max_level', 'origin'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoTerrain, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoTerrain properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['max_level', 'origin']),
            title='Edit GeoTerrain properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoTerrain properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

