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


class ContextScene(Object):
    """
    ContextScene - Provides a 2d scene for ContextItem objects.
    
    Superclass: Object
    
    Provides a 2d scene that ContextItem objects can be added to.
    Manages the items, ensures that they are rendered at the right times
    and passes on mouse events.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextScene, obj, update, **traits)
    
    scale_tiles = tvtk_base.true_bool_trait(help=\
        """
        Whether to scale the scene transform when tiling, for example
        when using WindowToImageFilter to take a large screenshot. The
        default is true.
        """
    )

    def _scale_tiles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleTiles,
                        self.scale_tiles_)

    def _get_annotation_link(self):
        return wrap_vtk(self._vtk_obj.GetAnnotationLink())
    def _set_annotation_link(self, arg):
        old_val = self._get_annotation_link()
        self._wrap_call(self._vtk_obj.SetAnnotationLink,
                        deref_vtk(arg))
        self.trait_property_changed('annotation_link', old_val, arg)
    annotation_link = traits.Property(_get_annotation_link, _set_annotation_link, help=\
        """
        Get the AnnotationLink for the chart.
        """
    )

    dirty = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Inform the scene that something changed that requires a repaint
        of the scene. This should only be used by the ContextItem
        derived objects in a scene in their event handlers.
        """
    )

    def _dirty_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirty,
                        self.dirty)

    geometry = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometry,
                        self.geometry)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        This should not be necessary as the context view should take care
        of rendering.
        """
    )

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Get the transform for the scene.
        """
    )

    use_buffer_id = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Set whether the scene should use the color buffer. Default is
        true.
        """
    )

    def _use_buffer_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseBufferId,
                        self.use_buffer_id)

    def _get_buffer_id(self):
        return wrap_vtk(self._vtk_obj.GetBufferId())
    buffer_id = traits.Property(_get_buffer_id, help=\
        """
        Return buffer id. Not part of the end-user API. Can be used by
        context items to initialize their own colorbuffer id (when a
        context item is a container).
        """
    )

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

    def _get_logical_tile_scale(self):
        return wrap_vtk(self._vtk_obj.GetLogicalTileScale())
    logical_tile_scale = traits.Property(_get_logical_tile_scale, help=\
        """
        The tile scale of the target RenderWindow. Hardcoded pixel
        offsets, etc should properly account for these <x, y> scale
        factors. This will simply return Vector2i(1, 1) if scale_tiles
        is false or if this->Renderer is NULL.
        """
    )

    def _get_number_of_items(self):
        return self._vtk_obj.GetNumberOfItems()
    number_of_items = traits.Property(_get_number_of_items, help=\
        """
        Get the number of child items.
        """
    )

    def _get_scene_height(self):
        return self._vtk_obj.GetSceneHeight()
    scene_height = traits.Property(_get_scene_height, help=\
        """
        Get the height of the scene.
        """
    )

    def _get_scene_width(self):
        return self._vtk_obj.GetSceneWidth()
    scene_width = traits.Property(_get_scene_width, help=\
        """
        Get the width of the scene.
        """
    )

    def _get_view_height(self):
        return self._vtk_obj.GetViewHeight()
    view_height = traits.Property(_get_view_height, help=\
        """
        Get the height of the view
        """
    )

    def _get_view_width(self):
        return self._vtk_obj.GetViewWidth()
    view_width = traits.Property(_get_view_width, help=\
        """
        Get the width of the view
        """
    )

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
        

    def has_transform(self):
        """
        V.has_transform() -> bool
        C++: bool HasTransform()
        Check whether the scene has a transform.
        """
        ret = self._vtk_obj.HasTransform()
        return ret
        

    def paint(self, *args):
        """
        V.paint(Context2D) -> bool
        C++: virtual bool Paint(Context2D *painter)
        Paint event for the chart, called whenever the chart needs to be
        drawn
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Paint, *my_args)
        return ret

    def release_graphics_resources(self):
        """
        V.release_graphics_resources()
        C++: void ReleaseGraphicsResources()
        Release graphics resources hold by the scene.
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

    _updateable_traits_ = \
    (('scale_tiles', 'GetScaleTiles'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('dirty',
    'GetDirty'), ('geometry', 'GetGeometry'), ('use_buffer_id',
    'GetUseBufferId'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'scale_tiles', 'dirty',
    'geometry', 'use_buffer_id'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextScene, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['scale_tiles'], [], ['dirty', 'geometry', 'use_buffer_id']),
            title='Edit ContextScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextScene properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

