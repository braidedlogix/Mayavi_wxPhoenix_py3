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

from tvtk.tvtk_classes.border_widget import BorderWidget


class ScalarBarWidget(BorderWidget):
    """
    ScalarBarWidget - 2d widget for manipulating a scalar bar
    
    Superclass: BorderWidget
    
    This class provides support for interactively manipulating the
    position, size, and orientation of a scalar bar. It listens to Left
    mouse events and mouse movement. It also listens to Right mouse
    events and notifies any observers of Right mouse events on this
    object when they occur. It will change the cursor shape based on its
    location. If the cursor is over an edge of the scalar bar it will
    change the cursor shape to a resize edge shape. If the position of a
    scalar bar is moved to be close to the center of one of the four
    edges of the viewport, then the scalar bar will change its
    orientation to align with that edge. This orientation is sticky in
    that it will stay that orientation until the position is moved close
    to another edge.
    
    @sa
    InteractorObserver
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarBarWidget, obj, update, **traits)
    
    repositionable = tvtk_base.true_bool_trait(help=\
        """
        Can the widget be moved. On by default. If off, the widget cannot
        be moved around.
        
        * TODO: This functionality should probably be moved to the
          superclass.
        """
    )

    def _repositionable_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRepositionable,
                        self.repositionable_)

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

    def _get_scalar_bar_actor(self):
        return wrap_vtk(self._vtk_obj.GetScalarBarActor())
    def _set_scalar_bar_actor(self, arg):
        old_val = self._get_scalar_bar_actor()
        self._wrap_call(self._vtk_obj.SetScalarBarActor,
                        deref_vtk(arg))
        self.trait_property_changed('scalar_bar_actor', old_val, arg)
    scalar_bar_actor = traits.Property(_get_scalar_bar_actor, _set_scalar_bar_actor, help=\
        """
        Get the scalar_bar used by this Widget. One is created
        automatically.
        """
    )

    def _get_scalar_bar_representation(self):
        return wrap_vtk(self._vtk_obj.GetScalarBarRepresentation())
    scalar_bar_representation = traits.Property(_get_scalar_bar_representation, help=\
        """
        Return the representation as a ScalarBarRepresentation.
        """
    )

    _updateable_traits_ = \
    (('repositionable', 'GetRepositionable'), ('resizable',
    'GetResizable'), ('selectable', 'GetSelectable'), ('manages_cursor',
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
    'key_press_activation', 'manages_cursor', 'picking_managed',
    'process_events', 'repositionable', 'resizable', 'selectable',
    'key_press_activation_value', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarBarWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarBarWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'manages_cursor',
            'picking_managed', 'process_events', 'repositionable', 'resizable',
            'selectable'], [], ['key_press_activation_value', 'priority']),
            title='Edit ScalarBarWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarBarWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

