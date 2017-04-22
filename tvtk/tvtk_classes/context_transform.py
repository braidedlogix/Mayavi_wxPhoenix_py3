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

from tvtk.tvtk_classes.abstract_context_item import AbstractContextItem


class ContextTransform(AbstractContextItem):
    """
    ContextTransform - all children of this item are transformed by
    the Transform2D of this item.
    
    Superclass: AbstractContextItem
    
    This class can be used to transform all child items of this class.
    The default transform is the identity.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextTransform, obj, update, **traits)
    
    pan_y_on_mouse_wheel = tvtk_base.false_bool_trait(help=\
        """
        Whether to pan in the Y direction on mouse wheels. Default is
        false.
        """
    )

    def _pan_y_on_mouse_wheel_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPanYOnMouseWheel,
                        self.pan_y_on_mouse_wheel_)

    zoom_on_mouse_wheel = tvtk_base.true_bool_trait(help=\
        """
        Whether to zoom on mouse wheels. Default is true.
        """
    )

    def _zoom_on_mouse_wheel_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZoomOnMouseWheel,
                        self.zoom_on_mouse_wheel_)

    pan_modifier = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The modifier from ContextMouseEvent to use for panning.
        Default is ContextMouseEvent::NO_MODIFIER.
        """
    )

    def _pan_modifier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPanModifier,
                        self.pan_modifier)

    pan_mouse_button = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        The mouse button from ContextMouseEvent to use for panning.
        Default is ContextMouseEvent::LEFT_BUTTON.
        """
    )

    def _pan_mouse_button_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPanMouseButton,
                        self.pan_mouse_button)

    secondary_pan_modifier = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        A secondary modifier from ContextMouseEvent to use for
        panning. Default is ContextMouseEvent::NO_MODIFIER.
        """
    )

    def _secondary_pan_modifier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSecondaryPanModifier,
                        self.secondary_pan_modifier)

    secondary_pan_mouse_button = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        A secondary mouse button from ContextMouseEvent to use for
        panning. Default is ContextMouseEvent::NO_BUTTON (disabled).
        """
    )

    def _secondary_pan_mouse_button_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSecondaryPanMouseButton,
                        self.secondary_pan_mouse_button)

    secondary_zoom_modifier = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        A secondary modifier from ContextMouseEvent to use for
        panning. Default is ContextMouseEvent::SHIFT_MODIFIER.
        """
    )

    def _secondary_zoom_modifier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSecondaryZoomModifier,
                        self.secondary_zoom_modifier)

    secondary_zoom_mouse_button = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        A secondary mouse button from ContextMouseEvent to use for
        panning. Default is ContextMouseEvent::LEFT_BUTTON.
        """
    )

    def _secondary_zoom_mouse_button_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSecondaryZoomMouseButton,
                        self.secondary_zoom_mouse_button)

    zoom_modifier = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The modifier from ContextMouseEvent to use for panning.
        Default is ContextMouseEvent::NO_MODIFIER.
        """
    )

    def _zoom_modifier_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZoomModifier,
                        self.zoom_modifier)

    zoom_mouse_button = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        The mouse button from ContextMouseEvent to use for panning.
        Default is ContextMouseEvent::RIGHT_BUTTON.
        """
    )

    def _zoom_mouse_button_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZoomMouseButton,
                        self.zoom_mouse_button)

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    transform = traits.Property(_get_transform, help=\
        """
        Access the Transform2D that controls object transformation.
        """
    )

    def identity(self):
        """
        V.identity()
        C++: virtual void Identity()
        Reset the transform to the identity transformation.
        """
        ret = self._vtk_obj.Identity()
        return ret
        

    def rotate(self, *args):
        """
        V.rotate(float)
        C++: virtual void Rotate(float angle)
        Rotate the item by the specified angle.
        """
        ret = self._wrap_call(self._vtk_obj.Rotate, *args)
        return ret

    def scale(self, *args):
        """
        V.scale(float, float)
        C++: virtual void Scale(float dx, float dy)
        Scale the item by the specified amounts dx and dy in the x and y
        directions.
        """
        ret = self._wrap_call(self._vtk_obj.Scale, *args)
        return ret

    def translate(self, *args):
        """
        V.translate(float, float)
        C++: virtual void Translate(float dx, float dy)
        Translate the item by the specified amounts dx and dy in the x
        and y directions.
        """
        ret = self._wrap_call(self._vtk_obj.Translate, *args)
        return ret

    _updateable_traits_ = \
    (('pan_y_on_mouse_wheel', 'GetPanYOnMouseWheel'),
    ('zoom_on_mouse_wheel', 'GetZoomOnMouseWheel'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pan_modifier', 'GetPanModifier'), ('pan_mouse_button',
    'GetPanMouseButton'), ('secondary_pan_modifier',
    'GetSecondaryPanModifier'), ('secondary_pan_mouse_button',
    'GetSecondaryPanMouseButton'), ('secondary_zoom_modifier',
    'GetSecondaryZoomModifier'), ('secondary_zoom_mouse_button',
    'GetSecondaryZoomMouseButton'), ('zoom_modifier', 'GetZoomModifier'),
    ('zoom_mouse_button', 'GetZoomMouseButton'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pan_y_on_mouse_wheel',
    'zoom_on_mouse_wheel', 'interactive', 'pan_modifier',
    'pan_mouse_button', 'secondary_pan_modifier',
    'secondary_pan_mouse_button', 'secondary_zoom_modifier',
    'secondary_zoom_mouse_button', 'visible', 'zoom_modifier',
    'zoom_mouse_button'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pan_y_on_mouse_wheel', 'zoom_on_mouse_wheel'], [],
            ['interactive', 'pan_modifier', 'pan_mouse_button',
            'secondary_pan_modifier', 'secondary_pan_mouse_button',
            'secondary_zoom_modifier', 'secondary_zoom_mouse_button', 'visible',
            'zoom_modifier', 'zoom_mouse_button']),
            title='Edit ContextTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

