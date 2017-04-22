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

from tvtk.tvtk_classes.point_placer import PointPlacer


class ImageActorPointPlacer(PointPlacer):
    """
    ImageActorPointPlacer - Converts 2d display positions to world
    positions such that they lie on an image_actor
    
    Superclass: PointPlacer
    
    This point_placer is used to constrain the placement of points on the
    supplied image actor. Additionally, you may set bounds to restrict
    the placement of the points. The placement of points will then be
    constrained to lie not only on the image_actor but also within the
    bounds specified. If no bounds are specified, they may lie anywhere
    on the supplied image_actor.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageActorPointPlacer, obj, update, **traits)
    
    bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(1e+299, -1e+299, 1e+299, -1e+299, 1e+299, -1e+299), cols=3, help=\
        """
        
        """
    )

    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    def _get_image_actor(self):
        return wrap_vtk(self._vtk_obj.GetImageActor())
    def _set_image_actor(self, arg):
        old_val = self._get_image_actor()
        self._wrap_call(self._vtk_obj.SetImageActor,
                        deref_vtk(arg))
        self.trait_property_changed('image_actor', old_val, arg)
    image_actor = traits.Property(_get_image_actor, _set_image_actor, help=\
        """
        Set / get the reference ImageActor used to place the points.
        An image actor must be set for this placer to work. An internal
        bounded plane point placer is created and set to match the bounds
        of the displayed image.
        """
    )

    world_tolerance = traits.Float(0.001, enter_set=True, auto_set=False, help=\
        """
        Set the world tolerance. This propagates it to the internal
        bounded_plane_point_placer.
        """
    )

    def _world_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldTolerance,
                        self.world_tolerance)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('bounds', 'GetBounds'),
    ('world_tolerance', 'GetWorldTolerance'), ('pixel_tolerance',
    'GetPixelTolerance'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'bounds', 'pixel_tolerance',
    'world_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageActorPointPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageActorPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['bounds', 'pixel_tolerance', 'world_tolerance']),
            title='Edit ImageActorPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageActorPointPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

