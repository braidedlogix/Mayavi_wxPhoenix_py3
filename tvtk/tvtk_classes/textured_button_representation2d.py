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

from tvtk.tvtk_classes.button_representation import ButtonRepresentation


class TexturedButtonRepresentation2D(ButtonRepresentation):
    """
    TexturedButtonRepresentation2D - defines a representation for a
    ButtonWidget
    
    Superclass: ButtonRepresentation
    
    This class implements one type of ButtonRepresentation. It changes
    the appearance of a user-provided polydata by assigning textures
    according to the current button state. It also provides highlighting
    (when hovering and selecting the button) by fiddling with the actor's
    property. Since this is a 2d version, the button is rendered in the
    overlay plane. Typically it is positioned in display coordinates, but
    it can be anchored to a world position so it will appear to move as
    the camera moves.
    
    To use this representation, always begin by specifying the number of
    button states.  Then provide a polydata (the polydata should have
    associated texture coordinates), and a list of textures cooresponding
    to the button states. Optionally, the hovering_property and
    selection_property can be adjusted to obtain the appropriate
    appearance.
    
    @warning
    There are two variants of the place_widget() method. The first
    place_widget(bds[_6]) allows the widget to be placed in the display
    coordinates fixed to the overlay plane. The second
    place_widget(anchor[_3],size[_2]) places the widget in world space;
    hence it will appear to move as the camera moves around the scene.
    
    @sa
    ButtonWidget ButtonRepresentation
    TexturedButtonRepresentation Prop3DButtonRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTexturedButtonRepresentation2D, obj, update, **traits)
    
    def get_button_texture(self, *args):
        """
        V.get_button_texture(int) -> ImageData
        C++: ImageData *GetButtonTexture(int i)
        Add the ith texture corresponding to the ith button state. The
        parameter i should be 0<=i<_number_of_states.
        """
        ret = self._wrap_call(self._vtk_obj.GetButtonTexture, *args)
        return wrap_vtk(ret)

    def set_button_texture(self, *args):
        """
        V.set_button_texture(int, ImageData)
        C++: void SetButtonTexture(int i, ImageData *image)
        Add the ith texture corresponding to the ith button state. The
        parameter i should be 0<=i<_number_of_states.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetButtonTexture, *my_args)
        return ret

    def _get_hovering_property(self):
        return wrap_vtk(self._vtk_obj.GetHoveringProperty())
    def _set_hovering_property(self, arg):
        old_val = self._get_hovering_property()
        self._wrap_call(self._vtk_obj.SetHoveringProperty,
                        deref_vtk(arg))
        self.trait_property_changed('hovering_property', old_val, arg)
    hovering_property = traits.Property(_get_hovering_property, _set_hovering_property, help=\
        """
        Specify the property to use when the hovering over the button.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Specify the property to use when the button is to appear "normal"
        i.e., the mouse pointer is not hovering or selecting the button.
        """
    )

    def _get_selecting_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectingProperty())
    def _set_selecting_property(self, arg):
        old_val = self._get_selecting_property()
        self._wrap_call(self._vtk_obj.SetSelectingProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selecting_property', old_val, arg)
    selecting_property = traits.Property(_get_selecting_property, _set_selecting_property, help=\
        """
        Specify the property to use when selecting the button.
        """
    )

    def _get_balloon(self):
        return wrap_vtk(self._vtk_obj.GetBalloon())
    balloon = traits.Property(_get_balloon, help=\
        """
        Grab the underlying BalloonRepresentation used to position and
        display the button texture.
        """
    )

    _updateable_traits_ = \
    (('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('state', 'GetState'), ('handle_size',
    'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'need_to_render',
    'pickable', 'picking_managed', 'use_bounds', 'visibility',
    'estimated_render_time', 'handle_size', 'place_factor',
    'render_time_multiplier', 'state'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TexturedButtonRepresentation2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TexturedButtonRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['need_to_render', 'picking_managed', 'use_bounds',
            'visibility'], [], ['estimated_render_time', 'handle_size',
            'place_factor', 'render_time_multiplier', 'state']),
            title='Edit TexturedButtonRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TexturedButtonRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

