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

from tvtk.tvtk_classes.widget_representation import WidgetRepresentation


class SeedRepresentation(WidgetRepresentation):
    """
    SeedRepresentation - represent the SeedWidget
    
    Superclass: WidgetRepresentation
    
    The SeedRepresentation is a superclass for classes representing
    the SeedWidget. This representation consists of one or more
    handles (vtk_handle_representation) which are used to place and
    manipulate the points defining the collection of seeds.
    
    @sa
    SeedWidget HandleRepresentation SeedRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSeedRepresentation, obj, update, **traits)
    
    def get_handle_representation(self, *args):
        """
        V.get_handle_representation(int) -> HandleRepresentation
        C++: HandleRepresentation *GetHandleRepresentation(
            unsigned int num)
        V.get_handle_representation() -> HandleRepresentation
        C++: HandleRepresentation *GetHandleRepresentation()
        Get the handle representations used for a particular seed. A side
        effect of this method is that it will create a handle
        representation in the list of representations if one has not yet
        been created.
        """
        ret = self._wrap_call(self._vtk_obj.GetHandleRepresentation, *args)
        return wrap_vtk(ret)

    def set_handle_representation(self, *args):
        """
        V.set_handle_representation(HandleRepresentation)
        C++: void SetHandleRepresentation(HandleRepresentation *handle)
        This method is used to specify the type of handle representation
        to use for the internal HandleWidgets within SeedWidget. 
        To use this method, create a dummy HandleWidget (or subclass),
        and then invoke this method with this dummy. Then the
        SeedRepresentation uses this dummy to clone HandleWidgets
        of the same type. Make sure you set the handle representation
        before the widget is enabled.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetHandleRepresentation, *my_args)
        return ret

    def get_seed_display_position(self, *args):
        """
        V.get_seed_display_position(int, [float, float, float])
        C++: virtual void GetSeedDisplayPosition(unsigned int seedNum,
            double pos[3])
        Methods to Set/Get the coordinates of seed points defining this
        representation. Note that methods are available for both display
        and world coordinates. The seeds are accessed by a seed number.
        """
        ret = self._wrap_call(self._vtk_obj.GetSeedDisplayPosition, *args)
        return ret

    def set_seed_display_position(self, *args):
        """
        V.set_seed_display_position(int, [float, float, float])
        C++: virtual void SetSeedDisplayPosition(unsigned int seedNum,
            double pos[3])
        Methods to Set/Get the coordinates of seed points defining this
        representation. Note that methods are available for both display
        and world coordinates. The seeds are accessed by a seed number.
        """
        ret = self._wrap_call(self._vtk_obj.SetSeedDisplayPosition, *args)
        return ret

    tolerance = traits.Trait(5, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the seed points
        of the widget to be active.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_active_handle(self):
        return self._vtk_obj.GetActiveHandle()
    active_handle = traits.Property(_get_active_handle, help=\
        """
        These are methods specific to SeedRepresentation and which are
        invoked from SeedWidget.
        """
    )

    def _get_number_of_seeds(self):
        return self._vtk_obj.GetNumberOfSeeds()
    number_of_seeds = traits.Property(_get_number_of_seeds, help=\
        """
        Return the number of seeds (or handles) that have been created.
        """
    )

    def get_seed_world_position(self, *args):
        """
        V.get_seed_world_position(int, [float, float, float])
        C++: virtual void GetSeedWorldPosition(unsigned int seedNum,
            double pos[3])
        Methods to Set/Get the coordinates of seed points defining this
        representation. Note that methods are available for both display
        and world coordinates. The seeds are accessed by a seed number.
        """
        ret = self._wrap_call(self._vtk_obj.GetSeedWorldPosition, *args)
        return ret

    def create_handle(self, *args):
        """
        V.create_handle([float, float]) -> int
        C++: virtual int CreateHandle(double e[2])"""
        ret = self._wrap_call(self._vtk_obj.CreateHandle, *args)
        return ret

    def remove_active_handle(self):
        """
        V.remove_active_handle()
        C++: virtual void RemoveActiveHandle()"""
        ret = self._vtk_obj.RemoveActiveHandle()
        return ret
        

    def remove_handle(self, *args):
        """
        V.remove_handle(int)
        C++: virtual void RemoveHandle(int n)
        Remove the nth handle.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveHandle, *args)
        return ret

    def remove_last_handle(self):
        """
        V.remove_last_handle()
        C++: virtual void RemoveLastHandle()"""
        ret = self._vtk_obj.RemoveLastHandle()
        return ret
        

    _updateable_traits_ = \
    (('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('tolerance', 'GetTolerance'),
    ('handle_size', 'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'use_bounds', 'visibility',
    'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SeedRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SeedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'use_bounds',
            'visibility'], [], ['estimated_render_time', 'handle_size',
            'place_factor', 'render_time_multiplier', 'tolerance']),
            title='Edit SeedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SeedRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

