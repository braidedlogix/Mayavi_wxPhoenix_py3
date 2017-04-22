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


class AbstractContextItem(Object):
    """
    AbstractContextItem - base class for items that are part of a
    ContextScene.
    
    Superclass: Object
    
    This class is the common base for all context scene items. You should
    generally derive from ContextItem, rather than this class, as it
    provides most of the commonly used API.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractContextItem, obj, update, **traits)
    
    interactive = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Set if the item is interactive (should respond to mouse events).
        """
    )

    def _interactive_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInteractive,
                        self.interactive)

    def _get_parent(self):
        return wrap_vtk(self._vtk_obj.GetParent())
    def _set_parent(self, arg):
        old_val = self._get_parent()
        self._wrap_call(self._vtk_obj.SetParent,
                        deref_vtk(arg))
        self.trait_property_changed('parent', old_val, arg)
    parent = traits.Property(_get_parent, _set_parent, help=\
        """
        Get the parent item. The parent will be set for all items except
        top level items in a tree.
        """
    )

    def _get_scene(self):
        return wrap_vtk(self._vtk_obj.GetScene())
    def _set_scene(self, arg):
        old_val = self._get_scene()
        self._wrap_call(self._vtk_obj.SetScene,
                        deref_vtk(arg))
        self.trait_property_changed('scene', old_val, arg)
    scene = traits.Property(_get_scene, _set_scene, help=\
        """
        Get the ContextScene for the item, always set for an item in a
        scene.
        """
    )

    visible = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Set the visibility of the item (should it be drawn). Visible by
        default.
        """
    )

    def _visible_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVisible,
                        self.visible)

    def get_item(self, *args):
        """
        V.get_item(int) -> AbstractContextItem
        C++: AbstractContextItem *GetItem(unsigned int index)
        Get the item at the specified index.
        \return the item at the specified index (null if index is
            invalid).
        """
        ret = self._wrap_call(self._vtk_obj.GetItem, *args)
        return wrap_vtk(ret)

    def get_item_index(self, *args):
        """
        V.get_item_index(AbstractContextItem) -> int
        C++: unsigned int GetItemIndex(AbstractContextItem *item)
        Get the index of the specified item.
        \return the index of the item (-1 if item is not a valid child).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetItemIndex, *my_args)
        return ret

    def _get_number_of_items(self):
        return self._vtk_obj.GetNumberOfItems()
    number_of_items = traits.Property(_get_number_of_items, help=\
        """
        Get the number of child items.
        """
    )

    def get_picked_item(self, *args):
        """
        V.get_picked_item(ContextMouseEvent) -> AbstractContextItem
        C++: virtual AbstractContextItem *GetPickedItem(
            const ContextMouseEvent &mouse)
        Return the item under the mouse. If no item is under the mouse,
        the method returns a null pointer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPickedItem, *my_args)
        return wrap_vtk(ret)

    def add_item(self, *args):
        """
        V.add_item(AbstractContextItem) -> int
        C++: unsigned int AddItem(AbstractContextItem *item)
        Add child items to this item. Increments reference count of item.
        \return the index of the child item.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddItem, *my_args)
        return ret

    def clear_items(self):
        """
        V.clear_items()
        C++: void ClearItems()
        Remove all child items from this item.
        """
        ret = self._vtk_obj.ClearItems()
        return ret
        

    def hit(self, *args):
        """
        V.hit(ContextMouseEvent) -> bool
        C++: virtual bool Hit(const ContextMouseEvent &mouse)
        Return true if the supplied x, y coordinate is inside the item.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Hit, *my_args)
        return ret

    def key_press_event(self, *args):
        """
        V.key_press_event(ContextKeyEvent) -> bool
        C++: virtual bool KeyPressEvent(const ContextKeyEvent &key)
        Key press event.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.KeyPressEvent, *my_args)
        return ret

    def key_release_event(self, *args):
        """
        V.key_release_event(ContextKeyEvent) -> bool
        C++: virtual bool KeyReleaseEvent(const ContextKeyEvent &key)
        Key release event.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.KeyReleaseEvent, *my_args)
        return ret

    def lower(self, *args):
        """
        V.lower(int) -> int
        C++: unsigned int Lower(unsigned int index)
        Lowers the child to the bottom of the item's stack.
        \return The new index of the item
        \sa stack_under(), Raise(), stack_above()
        """
        ret = self._wrap_call(self._vtk_obj.Lower, *args)
        return ret

    def map_from_parent(self, *args):
        """
        V.map_from_parent(Vector2f) -> Vector2f
        C++: virtual Vector2f MapFromParent(const Vector2f &point)
        Maps the point from the parent coordinate system.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MapFromParent, *my_args)
        return wrap_vtk(ret)

    def map_from_scene(self, *args):
        """
        V.map_from_scene(Vector2f) -> Vector2f
        C++: virtual Vector2f MapFromScene(const Vector2f &point)
        Maps the point from the scene coordinate system.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MapFromScene, *my_args)
        return wrap_vtk(ret)

    def map_to_parent(self, *args):
        """
        V.map_to_parent(Vector2f) -> Vector2f
        C++: virtual Vector2f MapToParent(const Vector2f &point)
        Maps the point to the parent coordinate system.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MapToParent, *my_args)
        return wrap_vtk(ret)

    def map_to_scene(self, *args):
        """
        V.map_to_scene(Vector2f) -> Vector2f
        C++: virtual Vector2f MapToScene(const Vector2f &point)
        Maps the point to the scene coordinate system.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MapToScene, *my_args)
        return wrap_vtk(ret)

    def mouse_button_press_event(self, *args):
        """
        V.mouse_button_press_event(ContextMouseEvent) -> bool
        C++: virtual bool MouseButtonPressEvent(
            const ContextMouseEvent &mouse)
        Mouse button down event Return true if the item holds the event,
        false if the event can be propagated to other items.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MouseButtonPressEvent, *my_args)
        return ret

    def mouse_button_release_event(self, *args):
        """
        V.mouse_button_release_event(ContextMouseEvent) -> bool
        C++: virtual bool MouseButtonReleaseEvent(
            const ContextMouseEvent &mouse)
        Mouse button release event. Return true if the item holds the
        event, false if the event can be propagated to other items.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MouseButtonReleaseEvent, *my_args)
        return ret

    def mouse_double_click_event(self, *args):
        """
        V.mouse_double_click_event(ContextMouseEvent) -> bool
        C++: virtual bool MouseDoubleClickEvent(
            const ContextMouseEvent &mouse)
        Mouse button double click event. Return true if the item holds
        the event, false if the event can be propagated to other items.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MouseDoubleClickEvent, *my_args)
        return ret

    def mouse_enter_event(self, *args):
        """
        V.mouse_enter_event(ContextMouseEvent) -> bool
        C++: virtual bool MouseEnterEvent(
            const ContextMouseEvent &mouse)
        Mouse enter event. Return true if the item holds the event, false
        if the event can be propagated to other items.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MouseEnterEvent, *my_args)
        return ret

    def mouse_leave_event(self, *args):
        """
        V.mouse_leave_event(ContextMouseEvent) -> bool
        C++: virtual bool MouseLeaveEvent(
            const ContextMouseEvent &mouse)
        Mouse leave event. Return true if the item holds the event, false
        if the event can be propagated to other items.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MouseLeaveEvent, *my_args)
        return ret

    def mouse_move_event(self, *args):
        """
        V.mouse_move_event(ContextMouseEvent) -> bool
        C++: virtual bool MouseMoveEvent(
            const ContextMouseEvent &mouse)
        Mouse move event. Return true if the item holds the event, false
        if the event can be propagated to other items.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MouseMoveEvent, *my_args)
        return ret

    def mouse_wheel_event(self, *args):
        """
        V.mouse_wheel_event(ContextMouseEvent, int) -> bool
        C++: virtual bool MouseWheelEvent(
            const ContextMouseEvent &mouse, int delta)
        Mouse wheel event, positive delta indicates forward movement of
        the wheel. Return true if the item holds the event, false if the
        event can be propagated to other items.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.MouseWheelEvent, *my_args)
        return ret

    def paint(self, *args):
        """
        V.paint(Context2D) -> bool
        C++: virtual bool Paint(Context2D *painter)
        Paint event for the item, called whenever the item needs to be
        drawn.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Paint, *my_args)
        return ret

    def paint_children(self, *args):
        """
        V.paint_children(Context2D) -> bool
        C++: virtual bool PaintChildren(Context2D *painter)
        Paint the children of the item, should be called whenever the
        children need to be rendered.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PaintChildren, *my_args)
        return ret

    def raise_(self, *args):
        """
        V.raise(int) -> int
        C++: unsigned int Raise(unsigned int index)
        Raises the child to the top of the item's stack.
        \return The new index of the item
        \sa stack_above(), Lower(), lower_under()
        """
        ret = self._wrap_call(self._vtk_obj.Raise, *args)
        return ret

    def release_graphics_resources(self):
        """
        V.release_graphics_resources()
        C++: virtual void ReleaseGraphicsResources()
        Release graphics resources hold by the item. The default
        implementation is empty.
        """
        ret = self._vtk_obj.ReleaseGraphicsResources()
        return ret
        

    def remove_item(self, *args):
        """
        V.remove_item(AbstractContextItem) -> bool
        C++: bool RemoveItem(AbstractContextItem *item)
        V.remove_item(int) -> bool
        C++: bool RemoveItem(unsigned int index)
        Remove child item from this item. Decrements reference count of
        item.
        \param item the item to be removed.
        \return true on success, false otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveItem, *my_args)
        return ret

    def stack_above(self, *args):
        """
        V.stack_above(int, int) -> int
        C++: virtual unsigned int StackAbove(unsigned int index,
            unsigned int under)
        Raises the child above the under sibling. If under is invalid,
        the item is raised to the top of the item's stack.
        \return The new index of the item
        \sa Raise(), Lower(), stack_under()
        """
        ret = self._wrap_call(self._vtk_obj.StackAbove, *args)
        return ret

    def stack_under(self, *args):
        """
        V.stack_under(int, int) -> int
        C++: virtual unsigned int StackUnder(unsigned int child,
            unsigned int above)
        Lowers the child under the above sibling. If above is invalid,
        the item is lowered to the bottom of the item's stack
        \return The new index of the item
        \sa Lower(), Raise(), stack_above()
        """
        ret = self._wrap_call(self._vtk_obj.StackUnder, *args)
        return ret

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Perform any updates to the item that may be necessary before
        rendering. The scene should take care of calling this on all
        items before their Paint function is invoked.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interactive', 'GetInteractive'),
    ('visible', 'GetVisible'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'interactive', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractContextItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['interactive', 'visible']),
            title='Edit AbstractContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

