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


class HandleRepresentation(WidgetRepresentation):
    """
    HandleRepresentation - abstract class for representing widget
    handles
    
    Superclass: WidgetRepresentation
    
    This class defines an API for widget handle representations. These
    representations interact with HandleWidget. Various
    representations can be used depending on the nature of the handle.
    The basic functionality of the handle representation is to maintain a
    position. The position is represented via a Coordinate, meaning
    that the position can be easily obtained in a variety of coordinate
    systems.
    
    Optional features for this representation include an active mode (the
    widget appears only when the mouse pointer is close to it). The
    active distance is expressed in pixels and represents a circle in
    display space.
    
    The class may be subclassed so that alternative representations can
    be created.  The class defines an API and a default implementation
    that the HandleWidget interacts with to render itself in the
    scene.
    
    @warning
    The separation of the widget event handling and representation
    enables users and developers to create new appearances for the
    widget. It also facilitates parallel processing, where the client
    application handles events, and remote representations of the widget
    are slaves to the client (and do not handle events).
    
    @sa
    RectilinearWipeWidget WidgetRepresentation AbstractWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHandleRepresentation, obj, update, **traits)
    
    active_representation = tvtk_base.false_bool_trait(help=\
        """
        Flag controls whether the widget becomes visible when the mouse
        pointer moves close to it (i.e., the widget becomes active). By
        default, active_representation is off and the representation is
        always visible.
        """
    )

    def _active_representation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveRepresentation,
                        self.active_representation_)

    constrained = tvtk_base.false_bool_trait(help=\
        """
        Specify whether any motions (such as scale, translate, etc.) are
        constrained in some way (along an axis, etc.) Widgets can use
        this to control the resulting motion.
        """
    )

    def _constrained_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstrained,
                        self.constrained_)

    display_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Handles usually have their coordinates set in display coordinates
        (generally by an associated widget) and internally maintain the
        position in world coordinates. (Using world coordinates insures
        that handles are rendered in the right position when the camera
        view changes.) These methods are often subclassed because special
        constraint operations can be used to control the actual
        positioning.
        """
    )

    def _display_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayPosition,
                        self.display_position)

    interaction_state = traits.Trait(0, traits.Range(0, 4, enter_set=True, auto_set=False), help=\
        """
        The interaction state may be set from a widget (e.g.,
        handle_widget) or other object. This controls how the interaction
        with the widget proceeds. Normally this method is used as part of
        a handshaking processwith the widget: First
        compute_interaction_state() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
    )

    def _interaction_state_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractionState,
                        self.interaction_state)

    def _get_point_placer(self):
        return wrap_vtk(self._vtk_obj.GetPointPlacer())
    def _set_point_placer(self, arg):
        old_val = self._get_point_placer()
        self._wrap_call(self._vtk_obj.SetPointPlacer,
                        deref_vtk(arg))
        self.trait_property_changed('point_placer', old_val, arg)
    point_placer = traits.Property(_get_point_placer, _set_point_placer, help=\
        """
        Set/Get the point placer. Point placers can be used to dictate
        constraints on the placement of handles. As an example, see
        BoundedPlanePointPlacer (constrains the placement of handles
        to a set of bounded planes) FocalPlanePointPlacer (constrains
        placement on the focal plane) etc. The default point placer is
        PointPlacer (which does not apply any constraints, so the
        handles are free to move anywhere).
        """
    )

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Subclasses of WidgetRepresentation must implement these
        methods. This is considered the minimum API for a widget
        representation.
        
        set_renderer() - the renderer in which the representations draws
        itself. Typically the renderer is set by the associated widget.
        Use the widget's set_current_renderer() method in most cases;
        otherwise there is a risk of inconsistent behavior as events and
        drawing may be performed in different viewports.
        build_representation() - update the geometry of the widget based
        on its current state.  WARNING: The renderer is NOT reference
        counted by the representation, in order to avoid reference loops.
         Be sure that the representation lifetime does not extend beyond
        the renderer lifetime.
        """
    )

    tolerance = traits.Trait(15, traits.Range(1, 100, enter_set=True, auto_set=False), help=\
        """
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the widget to be
        active.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    world_position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Handles usually have their coordinates set in display coordinates
        (generally by an associated widget) and internally maintain the
        position in world coordinates. (Using world coordinates insures
        that handles are rendered in the right position when the camera
        view changes.) These methods are often subclassed because special
        constraint operations can be used to control the actual
        positioning.
        """
    )

    def _world_position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWorldPosition,
                        self.world_position)

    def check_constraint(self, *args):
        """
        V.check_constraint(Renderer, [float, float]) -> int
        C++: virtual int CheckConstraint(Renderer *renderer,
            double pos[2])
        Method has to be overridden in the subclasses which has
        constraints on placing the handle (Ex.
        ConstrainedPointHandleRepresentation). It should return 1 if
        the position is within the constraint, else it should return
        0. By default it returns 1.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CheckConstraint, *my_args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Prop)
        C++: virtual void DeepCopy(Prop *prop)
        Methods to make this class properly act like a
        WidgetRepresentation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    _updateable_traits_ = \
    (('active_representation', 'GetActiveRepresentation'), ('constrained',
    'GetConstrained'), ('need_to_render', 'GetNeedToRender'),
    ('picking_managed', 'GetPickingManaged'), ('dragable', 'GetDragable'),
    ('pickable', 'GetPickable'), ('use_bounds', 'GetUseBounds'),
    ('visibility', 'GetVisibility'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('display_position', 'GetDisplayPosition'), ('interaction_state',
    'GetInteractionState'), ('tolerance', 'GetTolerance'),
    ('world_position', 'GetWorldPosition'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['active_representation', 'constrained', 'debug', 'dragable',
    'global_warning_display', 'need_to_render', 'pickable',
    'picking_managed', 'use_bounds', 'visibility', 'display_position',
    'estimated_render_time', 'handle_size', 'interaction_state',
    'place_factor', 'render_time_multiplier', 'tolerance',
    'world_position'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HandleRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['active_representation', 'constrained', 'need_to_render',
            'picking_managed', 'use_bounds', 'visibility'], [],
            ['display_position', 'estimated_render_time', 'handle_size',
            'interaction_state', 'place_factor', 'render_time_multiplier',
            'tolerance', 'world_position']),
            title='Edit HandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HandleRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

