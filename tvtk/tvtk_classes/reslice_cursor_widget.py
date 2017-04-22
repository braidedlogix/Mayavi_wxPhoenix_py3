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

from tvtk.tvtk_classes.abstract_widget import AbstractWidget


class ResliceCursorWidget(AbstractWidget):
    """
    ResliceCursorWidget - represent a reslice cursor
    
    Superclass: AbstractWidget
    
    This class represents a reslice cursor that can be used to perform
    interactive thick slab MPR's through data. It consists of two cross
    sectional hairs, with an optional thickness. The hairs may have a
    hole in the center. These may be translated or rotated independent of
    each other in the view. The result is used to reslice the data along
    these cross sections. This allows the user to perform multi-planar
    thin or thick reformat of the data on an image view, rather than a 3d
    view. The class internally uses ImageSlabReslice or
    ImageReslice depending on the modes in ResliceCursor to do its
    reslicing. The slab thickness is set interactively from the widget.
    The slab resolution (ie the number of blend points) is set as the
    minimum spacing along any dimension from the dataset.
    @sa
    ImageSlabReslice ResliceCursorLineRepresentation
    ResliceCursor
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceCursorWidget, obj, update, **traits)
    
    manage_window_level = tvtk_base.true_bool_trait(help=\
        """
        Also perform window level ?
        """
    )

    def _manage_window_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetManageWindowLevel,
                        self.manage_window_level_)

    def _get_representation(self):
        return wrap_vtk(self._vtk_obj.GetRepresentation())
    def _set_representation(self, arg):
        old_val = self._get_representation()
        self._wrap_call(self._vtk_obj.SetRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('representation', old_val, arg)
    representation = traits.Property(_get_representation, _set_representation, help=\
        """
        Return an instance of WidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of Prop (typically a subclass of
        WidgetRepresenation) so it can be added to the renderer
        independent of the widget.
        """
    )

    def _get_reslice_cursor_representation(self):
        return wrap_vtk(self._vtk_obj.GetResliceCursorRepresentation())
    reslice_cursor_representation = traits.Property(_get_reslice_cursor_representation, help=\
        """
        Return the representation as a ResliceCursorRepresentation.
        """
    )

    def reset_reslice_cursor(self):
        """
        V.reset_reslice_cursor()
        C++: virtual void ResetResliceCursor()
        Reset the cursor back to its initial state
        """
        ret = self._vtk_obj.ResetResliceCursor()
        return ret
        

    _updateable_traits_ = \
    (('manage_window_level', 'GetManageWindowLevel'), ('manages_cursor',
    'GetManagesCursor'), ('process_events', 'GetProcessEvents'),
    ('enabled', 'GetEnabled'), ('key_press_activation',
    'GetKeyPressActivation'), ('picking_managed', 'GetPickingManaged'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('priority', 'GetPriority'),
    ('key_press_activation_value', 'GetKeyPressActivationValue'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'manage_window_level', 'manages_cursor',
    'picking_managed', 'process_events', 'key_press_activation_value',
    'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceCursorWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceCursorWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manage_window_level',
            'manages_cursor', 'picking_managed', 'process_events'], [],
            ['key_press_activation_value', 'priority']),
            title='Edit ResliceCursorWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceCursorWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

