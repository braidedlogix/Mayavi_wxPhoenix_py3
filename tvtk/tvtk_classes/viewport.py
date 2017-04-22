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


class Viewport(Object):
    """
    Viewport - abstract specification for Viewports
    
    Superclass: Object
    
    Viewport provides an abstract specification for Viewports. A
    Viewport is an object that controls the rendering process for
    objects. Rendering is the process of converting geometry, a
    specification for lights, and a camera view into an image.
    Viewport also performs coordinate transformation between world
    coordinates, view coordinates (the computer graphics rendering
    coordinate system), and display coordinates (the actual screen
    coordinates on the display device). Certain advanced rendering
    features such as two-sided lighting can also be controlled.
    
    @sa
    Window Renderer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkViewport, obj, update, **traits)
    
    gradient_background = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether this viewport should have a gradient background
        using the Background (bottom) and Background2 (top) colors.
        Default is off.
        """
    )

    def _gradient_background_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGradientBackground,
                        self.gradient_background_)

    aspect = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _aspect_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAspect,
                        self.aspect)

    background = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )

    def _background_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackground,
                        self.background, False)

    background2 = tvtk_base.vtk_color_trait((0.2, 0.2, 0.2), help=\
        """
        
        """
    )

    def _background2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackground2,
                        self.background2, False)

    current_pick_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _current_pick_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentPickId,
                        self.current_pick_id)

    display_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _display_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayPoint,
                        self.display_point)

    pixel_aspect = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(1.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _pixel_aspect_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPixelAspect,
                        self.pixel_aspect)

    view_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _view_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewPoint,
                        self.view_point)

    viewport = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _viewport_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewport,
                        self.viewport)

    world_point = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _world_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldPoint,
                        self.world_point)

    def _get_actors2d(self):
        return wrap_vtk(self._vtk_obj.GetActors2D())
    actors2d = traits.Property(_get_actors2d, help=\
        """
        Add/Remove different types of props to the renderer. These
        methods are all synonyms to add_view_prop and remove_view_prop. They
        are here for convenience and backwards compatibility.
        """
    )

    def _get_center(self):
        return self._vtk_obj.GetCenter()
    center = traits.Property(_get_center, help=\
        """
        Return the center of this viewport in display coordinates.
        """
    )

    def _get_is_picking(self):
        return self._vtk_obj.GetIsPicking()
    is_picking = traits.Property(_get_is_picking, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_origin(self):
        return self._vtk_obj.GetOrigin()
    origin = traits.Property(_get_origin, help=\
        """
        Get the size and origin of the viewport in display coordinates.
        Note: if the window has not yet been realized, get_size() and
        get_origin() return (0,0).
        """
    )

    def _get_pick_height(self):
        return self._vtk_obj.GetPickHeight()
    pick_height = traits.Property(_get_pick_height, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_pick_result_props(self):
        return wrap_vtk(self._vtk_obj.GetPickResultProps())
    pick_result_props = traits.Property(_get_pick_result_props, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_pick_width(self):
        return self._vtk_obj.GetPickWidth()
    pick_width = traits.Property(_get_pick_width, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_pick_x(self):
        return self._vtk_obj.GetPickX()
    pick_x = traits.Property(_get_pick_x, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_pick_x1(self):
        return self._vtk_obj.GetPickX1()
    pick_x1 = traits.Property(_get_pick_x1, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_pick_x2(self):
        return self._vtk_obj.GetPickX2()
    pick_x2 = traits.Property(_get_pick_x2, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_pick_y(self):
        return self._vtk_obj.GetPickY()
    pick_y = traits.Property(_get_pick_y, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_pick_y1(self):
        return self._vtk_obj.GetPickY1()
    pick_y1 = traits.Property(_get_pick_y1, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_pick_y2(self):
        return self._vtk_obj.GetPickY2()
    pick_y2 = traits.Property(_get_pick_y2, help=\
        """
        Methods used to return the pick (x,y) in local display
        coordinates (i.e., it's that same as selection_x and selection_y).
        """
    )

    def _get_picked_z(self):
        return self._vtk_obj.GetPickedZ()
    picked_z = traits.Property(_get_picked_z, help=\
        """
        Return the Z value for the last picked Prop.
        """
    )

    def _get_size(self):
        return self._vtk_obj.GetSize()
    size = traits.Property(_get_size, help=\
        """
        Get the size and origin of the viewport in display coordinates.
        Note: if the window has not yet been realized, get_size() and
        get_origin() return (0,0).
        """
    )

    def get_tiled_size(self, *args):
        """
        V.get_tiled_size([int, ...], [int, ...])
        C++: void GetTiledSize(int *width, int *height)
        Get the size and origin of the viewport in display coordinates.
        Note: if the window has not yet been realized, get_size() and
        get_origin() return (0,0).
        """
        ret = self._wrap_call(self._vtk_obj.GetTiledSize, *args)
        return ret

    def get_tiled_size_and_origin(self, *args):
        """
        V.get_tiled_size_and_origin([int, ...], [int, ...], [int, ...], [int,
            ...])
        C++: virtual void GetTiledSizeAndOrigin(int *width, int *height,
            int *lowerLeftX, int *lowerLeftY)
        Get the size and origin of the viewport in display coordinates.
        Note: if the window has not yet been realized, get_size() and
        get_origin() return (0,0).
        """
        ret = self._wrap_call(self._vtk_obj.GetTiledSizeAndOrigin, *args)
        return ret

    def _get_vtk_window(self):
        return wrap_vtk(self._vtk_obj.GetVTKWindow())
    vtk_window = traits.Property(_get_vtk_window, help=\
        """
        Return the Window that owns this Viewport.
        """
    )

    def _get_view_props(self):
        return wrap_vtk(self._vtk_obj.GetViewProps())
    view_props = traits.Property(_get_view_props, help=\
        """
        Return any props in this viewport.
        """
    )

    def add_actor2d(self, *args):
        """
        V.add_actor2d(Prop)
        C++: void AddActor2D(Prop *p)
        Add/Remove different types of props to the renderer. These
        methods are all synonyms to add_view_prop and remove_view_prop. They
        are here for convenience and backwards compatibility.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddActor2D, *my_args)
        return ret

    def add_view_prop(self, *args):
        """
        V.add_view_prop(Prop)
        C++: void AddViewProp(Prop *)
        Add a prop to the list of props. Does nothing if the prop is
        already present. Prop is the superclass of all actors, volumes,
        2d actors, composite props etc.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddViewProp, *my_args)
        return ret

    def compute_aspect(self):
        """
        V.compute_aspect()
        C++: virtual void ComputeAspect()
        Set the aspect ratio of the rendered image. This is computed
        automatically and should not be set by the user.
        """
        ret = self._vtk_obj.ComputeAspect()
        return ret
        

    def display_to_local_display(self, *args):
        """
        V.display_to_local_display(float, float)
        C++: virtual void DisplayToLocalDisplay(double &x, double &y)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.DisplayToLocalDisplay, *args)
        return ret

    def display_to_normalized_display(self, *args):
        """
        V.display_to_normalized_display(float, float)
        C++: virtual void DisplayToNormalizedDisplay(double &u, double &v)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.DisplayToNormalizedDisplay, *args)
        return ret

    def display_to_view(self):
        """
        V.display_to_view()
        C++: virtual void DisplayToView()
        Convert display coordinates to view coordinates.
        """
        ret = self._vtk_obj.DisplayToView()
        return ret
        

    def display_to_world(self):
        """
        V.display_to_world()
        C++: void DisplayToWorld()
        Convert display (or screen) coordinates to world coordinates.
        """
        ret = self._vtk_obj.DisplayToWorld()
        return ret
        

    def has_view_prop(self, *args):
        """
        V.has_view_prop(Prop) -> int
        C++: int HasViewProp(Prop *)
        Query if a prop is in the list of props.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasViewProp, *my_args)
        return ret

    def is_in_viewport(self, *args):
        """
        V.is_in_viewport(int, int) -> int
        C++: virtual int IsInViewport(int x, int y)
        Is a given display point in this Viewport's viewport.
        """
        ret = self._wrap_call(self._vtk_obj.IsInViewport, *args)
        return ret

    def local_display_to_display(self, *args):
        """
        V.local_display_to_display(float, float)
        C++: virtual void LocalDisplayToDisplay(double &x, double &y)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.LocalDisplayToDisplay, *args)
        return ret

    def normalized_display_to_display(self, *args):
        """
        V.normalized_display_to_display(float, float)
        C++: virtual void NormalizedDisplayToDisplay(double &u, double &v)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.NormalizedDisplayToDisplay, *args)
        return ret

    def normalized_display_to_viewport(self, *args):
        """
        V.normalized_display_to_viewport(float, float)
        C++: virtual void NormalizedDisplayToViewport(double &x,
            double &y)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.NormalizedDisplayToViewport, *args)
        return ret

    def normalized_viewport_to_view(self, *args):
        """
        V.normalized_viewport_to_view(float, float, float)
        C++: virtual void NormalizedViewportToView(double &x, double &y,
            double &z)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.NormalizedViewportToView, *args)
        return ret

    def normalized_viewport_to_viewport(self, *args):
        """
        V.normalized_viewport_to_viewport(float, float)
        C++: virtual void NormalizedViewportToViewport(double &u,
            double &v)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.NormalizedViewportToViewport, *args)
        return ret

    def pick_prop(self, *args):
        """
        V.pick_prop(float, float) -> AssemblyPath
        C++: virtual AssemblyPath *PickProp(double selectionX,
            double selectionY)
        V.pick_prop(float, float, float, float) -> AssemblyPath
        C++: virtual AssemblyPath *PickProp(double selectionX1,
            double selectionY1, double selectionX2, double selectionY2)
        Return the Prop that has the highest z value at the given x, y
        position in the viewport.  Basically, the top most prop that
        renders the pixel at selection_x, selection_y will be returned.  If
        no Props are there NULL is returned.  This method selects from
        the Viewports Prop list.
        """
        ret = self._wrap_call(self._vtk_obj.PickProp, *args)
        return wrap_vtk(ret)

    def pick_prop_from(self, *args):
        """
        V.pick_prop_from(float, float, PropCollection) -> AssemblyPath
        C++: AssemblyPath *PickPropFrom(double selectionX,
            double selectionY, PropCollection *)
        V.pick_prop_from(float, float, float, float, PropCollection)
            -> AssemblyPath
        C++: AssemblyPath *PickPropFrom(double selectionX1,
            double selectionY1, double selectionX2, double selectionY2,
            PropCollection *)
        Same as pick_prop with two arguments, but selects from the given
        collection of Props instead of the Renderers props.  Make sure
        the Props in the collection are in this renderer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PickPropFrom, *my_args)
        return wrap_vtk(ret)

    def remove_actor2d(self, *args):
        """
        V.remove_actor2d(Prop)
        C++: void RemoveActor2D(Prop *p)
        Add/Remove different types of props to the renderer. These
        methods are all synonyms to add_view_prop and remove_view_prop. They
        are here for convenience and backwards compatibility.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveActor2D, *my_args)
        return ret

    def remove_all_view_props(self):
        """
        V.remove_all_view_props()
        C++: void RemoveAllViewProps(void)
        Remove all props from the list of props.
        """
        ret = self._vtk_obj.RemoveAllViewProps()
        return ret
        

    def remove_view_prop(self, *args):
        """
        V.remove_view_prop(Prop)
        C++: void RemoveViewProp(Prop *)
        Remove a prop from the list of props. Does nothing if the prop is
        not already present.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveViewProp, *my_args)
        return ret

    def view_to_display(self):
        """
        V.view_to_display()
        C++: virtual void ViewToDisplay()
        Convert view coordinates to display coordinates.
        """
        ret = self._vtk_obj.ViewToDisplay()
        return ret
        

    def view_to_normalized_viewport(self, *args):
        """
        V.view_to_normalized_viewport(float, float, float)
        C++: virtual void ViewToNormalizedViewport(double &x, double &y,
            double &z)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.ViewToNormalizedViewport, *args)
        return ret

    def view_to_world(self, *args):
        """
        V.view_to_world()
        C++: virtual void ViewToWorld()
        V.view_to_world(float, float, float)
        C++: virtual void ViewToWorld(double &, double &, double &)
        Convert view point coordinates to world coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.ViewToWorld, *args)
        return ret

    def viewport_to_normalized_display(self, *args):
        """
        V.viewport_to_normalized_display(float, float)
        C++: virtual void ViewportToNormalizedDisplay(double &x,
            double &y)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.ViewportToNormalizedDisplay, *args)
        return ret

    def viewport_to_normalized_viewport(self, *args):
        """
        V.viewport_to_normalized_viewport(float, float)
        C++: virtual void ViewportToNormalizedViewport(double &u,
            double &v)
        These methods map from one coordinate system to another. They are
        primarily used by the Coordinate object and are often strung
        together. These methods return valid information only if the
        window has been realized (e.g., get_size() returns something other
        than (0,0)).
        """
        ret = self._wrap_call(self._vtk_obj.ViewportToNormalizedViewport, *args)
        return ret

    def world_to_display(self):
        """
        V.world_to_display()
        C++: void WorldToDisplay()
        Convert world point coordinates to display (or screen)
        coordinates.
        """
        ret = self._vtk_obj.WorldToDisplay()
        return ret
        

    def world_to_view(self, *args):
        """
        V.world_to_view()
        C++: virtual void WorldToView()
        V.world_to_view(float, float, float)
        C++: virtual void WorldToView(double &, double &, double &)
        Convert world point coordinates to view coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.WorldToView, *args)
        return ret

    _updateable_traits_ = \
    (('gradient_background', 'GetGradientBackground'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('aspect', 'GetAspect'), ('background', 'GetBackground'),
    ('background2', 'GetBackground2'), ('current_pick_id',
    'GetCurrentPickId'), ('display_point', 'GetDisplayPoint'),
    ('pixel_aspect', 'GetPixelAspect'), ('view_point', 'GetViewPoint'),
    ('viewport', 'GetViewport'), ('world_point', 'GetWorldPoint'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'gradient_background', 'aspect',
    'background', 'background2', 'current_pick_id', 'display_point',
    'pixel_aspect', 'view_point', 'viewport', 'world_point'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Viewport, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Viewport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['gradient_background'], [], ['aspect', 'background',
            'background2', 'current_pick_id', 'display_point', 'pixel_aspect',
            'view_point', 'viewport', 'world_point']),
            title='Edit Viewport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Viewport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

