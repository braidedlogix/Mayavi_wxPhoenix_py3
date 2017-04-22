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

from tvtk.tvtk_classes.prop3d import Prop3D


class ResliceCursorActor(Prop3D):
    """
    ResliceCursorActor - Represent a reslice cursor
    
    Superclass: Prop3D
    
    A reslice cursor consists of a pair of lines (cross hairs), thin or
    thick, that may be interactively manipulated for thin/thick reformats
    through the data.
    @sa
    ResliceCursor ResliceCursorPolyDataAlgorithm
    ResliceCursorWidget ResliceCursorRepresentation
    ResliceCursorLineRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceCursorActor, obj, update, **traits)
    
    def _get_user_matrix(self):
        return wrap_vtk(self._vtk_obj.GetUserMatrix())
    def _set_user_matrix(self, arg):
        old_val = self._get_user_matrix()
        self._wrap_call(self._vtk_obj.SetUserMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('user_matrix', old_val, arg)
    user_matrix = traits.Property(_get_user_matrix, _set_user_matrix, help=\
        """
        The user_matrix can be used in place of user_transform.
        """
    )

    def get_centerline_actor(self, *args):
        """
        V.get_centerline_actor(int) -> Actor
        C++: Actor *GetCenterlineActor(int axis)
        Get the centerline actor along a particular axis
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterlineActor, *args)
        return wrap_vtk(ret)

    def get_centerline_property(self, *args):
        """
        V.get_centerline_property(int) -> Property
        C++: Property *GetCenterlineProperty(int i)
        Get property of the internal actor.
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterlineProperty, *args)
        return wrap_vtk(ret)

    def _get_cursor_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetCursorAlgorithm())
    cursor_algorithm = traits.Property(_get_cursor_algorithm, help=\
        """
        Get the cursor algorithm. The cursor must be set on the algorithm
        """
    )

    def get_thick_slab_property(self, *args):
        """
        V.get_thick_slab_property(int) -> Property
        C++: Property *GetThickSlabProperty(int i)
        Get property of the internal actor.
        """
        ret = self._wrap_call(self._vtk_obj.GetThickSlabProperty, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('orientation', 'GetOrientation'),
    ('origin', 'GetOrigin'), ('position', 'GetPosition'), ('scale',
    'GetScale'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'estimated_render_time', 'orientation',
    'origin', 'position', 'render_time_multiplier', 'scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceCursorActor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceCursorActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_bounds', 'visibility'], [], ['estimated_render_time',
            'orientation', 'origin', 'position', 'render_time_multiplier',
            'scale']),
            title='Edit ResliceCursorActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceCursorActor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

