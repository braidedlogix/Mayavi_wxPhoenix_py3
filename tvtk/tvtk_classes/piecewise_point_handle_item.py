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

from tvtk.tvtk_classes.context_item import ContextItem


class PiecewisePointHandleItem(ContextItem):
    """
    PiecewisePointHandleItem - a ContextItem that draws handles
          around a point of a piecewise function
    
    Superclass: ContextItem
    
    This is a ContextItem that can be placed into a ContextScene.
    It draws handles around a given point of a piecewise function so that
    the curve can be adjusted using these handles.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPiecewisePointHandleItem, obj, update, **traits)
    
    current_point_index = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        The current point id in the piecewise function being handled.
        """
    )

    def _current_point_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentPointIndex,
                        self.current_point_index)

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

    def call_redraw(self, *args):
        """
        V.call_redraw(Object, int, void, void)
        C++: static void CallRedraw(Object *sender,
            unsigned long event, void *receiver, void *params)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CallRedraw, *my_args)
        return ret

    def is_over_handle(self, *args):
        """
        V.is_over_handle([float, ...]) -> int
        C++: int IsOverHandle(float *pos)
        Returns the index of the handle if pos is over any of the
        handles, otherwise return -1;
        """
        ret = self._wrap_call(self._vtk_obj.IsOverHandle, *args)
        return ret

    def set_piecewise_function(self, *args):
        """
        V.set_piecewise_function(PiecewiseFunction)
        C++: virtual void SetPiecewiseFunction(
            PiecewiseFunction *piecewiseFunc)
        Set the piece_wise_function the handles will manipulate
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPiecewiseFunction, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('current_point_index',
    'GetCurrentPointIndex'), ('opacity', 'GetOpacity'), ('interactive',
    'GetInteractive'), ('visible', 'GetVisible'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'current_point_index',
    'interactive', 'opacity', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PiecewisePointHandleItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PiecewisePointHandleItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['current_point_index', 'interactive', 'opacity',
            'visible']),
            title='Edit PiecewisePointHandleItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PiecewisePointHandleItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

