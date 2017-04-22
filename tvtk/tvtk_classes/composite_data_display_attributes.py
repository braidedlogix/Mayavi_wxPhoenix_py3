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


class CompositeDataDisplayAttributes(Object):
    """
    CompositeDataDisplayAttributes - rendering attributes for a
    multi-block dataset.
    
    Superclass: Object
    
    The CompositeDataDisplayAttributes class stores display attributes
    for individual blocks in a multi-block dataset.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCompositeDataDisplayAttributes, obj, update, **traits)
    
    def get_block_color(self, *args):
        """
        V.get_block_color(int, [float, float, float])
        C++: void GetBlockColor(unsigned int flat_index, double color[3])
        V.get_block_color(int) -> Color3d
        C++: Color3d GetBlockColor(unsigned int flat_index)
        Set/get the color for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockColor, *args)
        return wrap_vtk(ret)

    def set_block_color(self, *args):
        """
        V.set_block_color(int, (float, float, float))
        C++: void SetBlockColor(unsigned int flat_index,
            const double color[3])
        Set/get the color for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.SetBlockColor, *args)
        return ret

    def get_block_opacity(self, *args):
        """
        V.get_block_opacity(int) -> float
        C++: double GetBlockOpacity(unsigned int flat_index)
        Set/get the opacity for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockOpacity, *args)
        return ret

    def set_block_opacity(self, *args):
        """
        V.set_block_opacity(int, float)
        C++: void SetBlockOpacity(unsigned int flat_index, double opacity)
        Set/get the opacity for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.SetBlockOpacity, *args)
        return ret

    def get_block_visibility(self, *args):
        """
        V.get_block_visibility(int) -> bool
        C++: bool GetBlockVisibility(unsigned int flat_index)
        Set/get the visibility for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockVisibility, *args)
        return ret

    def set_block_visibility(self, *args):
        """
        V.set_block_visibility(int, bool)
        C++: void SetBlockVisibility(unsigned int flat_index,
            bool visible)
        Set/get the visibility for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.SetBlockVisibility, *args)
        return ret

    def compute_visible_bounds(self, *args):
        """
        V.compute_visible_bounds(CompositeDataDisplayAttributes,
            DataObject, [float, float, float, float, float, float])
        C++: static void ComputeVisibleBounds(
            CompositeDataDisplayAttributes *cda, DataObject *dobj,
            double bounds[6])"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ComputeVisibleBounds, *my_args)
        return ret

    def has_block_color(self, *args):
        """
        V.has_block_color(int) -> bool
        C++: bool HasBlockColor(unsigned int flat_index)
        Returns true if the block with the given flat_index has a color.
        """
        ret = self._wrap_call(self._vtk_obj.HasBlockColor, *args)
        return ret

    def has_block_colors(self):
        """
        V.has_block_colors() -> bool
        C++: bool HasBlockColors()
        Returns true if any block has any block color is set.
        """
        ret = self._vtk_obj.HasBlockColors()
        return ret
        

    def has_block_opacities(self):
        """
        V.has_block_opacities() -> bool
        C++: bool HasBlockOpacities()
        Returns true if any block has an opacity set.
        """
        ret = self._vtk_obj.HasBlockOpacities()
        return ret
        

    def has_block_opacity(self, *args):
        """
        V.has_block_opacity(int) -> bool
        C++: bool HasBlockOpacity(unsigned int flat_index)
        Returns true if the block with flat_index has an opacity set.
        """
        ret = self._wrap_call(self._vtk_obj.HasBlockOpacity, *args)
        return ret

    def has_block_visibilities(self):
        """
        V.has_block_visibilities() -> bool
        C++: bool HasBlockVisibilities()
        Returns true if any block has any block visibility is set.
        """
        ret = self._vtk_obj.HasBlockVisibilities()
        return ret
        

    def has_block_visibility(self, *args):
        """
        V.has_block_visibility(int) -> bool
        C++: bool HasBlockVisibility(unsigned int flat_index)
        Returns true if the block with the given flat_index has a
        visiblity set.
        """
        ret = self._wrap_call(self._vtk_obj.HasBlockVisibility, *args)
        return ret

    def remove_block_color(self, *args):
        """
        V.remove_block_color(int)
        C++: void RemoveBlockColor(unsigned int flat_index)
        Removes the block color for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveBlockColor, *args)
        return ret

    def remove_block_colors(self):
        """
        V.remove_block_colors()
        C++: void RemoveBlockColors()
        Removes all block colors.
        """
        ret = self._vtk_obj.RemoveBlockColors()
        return ret
        

    def remove_block_opacities(self):
        """
        V.remove_block_opacities()
        C++: void RemoveBlockOpacities()
        Removes all block opacities.
        """
        ret = self._vtk_obj.RemoveBlockOpacities()
        return ret
        

    def remove_block_opacity(self, *args):
        """
        V.remove_block_opacity(int)
        C++: void RemoveBlockOpacity(unsigned int flat_index)
        Removes the set opacity for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveBlockOpacity, *args)
        return ret

    def remove_block_visibilites(self):
        """
        V.remove_block_visibilites()
        C++: void RemoveBlockVisibilites()
        Removes all block visibility flags. The effectively sets the
        visibility for all blocks to true.
        """
        ret = self._vtk_obj.RemoveBlockVisibilites()
        return ret
        

    def remove_block_visibility(self, *args):
        """
        V.remove_block_visibility(int)
        C++: void RemoveBlockVisibility(unsigned int flat_index)
        Removes the block visibility flag for the block with flat_index.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveBlockVisibility, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CompositeDataDisplayAttributes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CompositeDataDisplayAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit CompositeDataDisplayAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CompositeDataDisplayAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

