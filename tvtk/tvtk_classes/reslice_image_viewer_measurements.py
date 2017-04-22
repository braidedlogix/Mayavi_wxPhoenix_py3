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


class ResliceImageViewerMeasurements(Object):
    """
    ResliceImageViewerMeasurements - Manage measurements on a resliced
    image
    
    Superclass: Object
    
    This class manages measurements on the resliced image. It toggles the
    the visibility of the measurements based on whether the resliced
    image is the same orientation as when the measurement was initially
    placed.
    @sa
    ResliceCursor ResliceCursorWidget
    ResliceCursorRepresentation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceImageViewerMeasurements, obj, update, **traits)
    
    process_events = tvtk_base.true_bool_trait(help=\
        """
        Methods to change whether the widget responds to interaction. Set
        this to Off to disable interaction. On by default. Subclasses
        must overide set_process_events() to make sure that they pass on
        the flag to all component widgets.
        """
    )

    def _process_events_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProcessEvents,
                        self.process_events_)

    def _get_reslice_image_viewer(self):
        return wrap_vtk(self._vtk_obj.GetResliceImageViewer())
    def _set_reslice_image_viewer(self, arg):
        old_val = self._get_reslice_image_viewer()
        self._wrap_call(self._vtk_obj.SetResliceImageViewer,
                        deref_vtk(arg))
        self.trait_property_changed('reslice_image_viewer', old_val, arg)
    reslice_image_viewer = traits.Property(_get_reslice_image_viewer, _set_reslice_image_viewer, help=\
        """
        Set the reslice image viewer. This is automatically done in the
        class ResliceImageViewer
        """
    )

    tolerance = traits.Float(6.0, enter_set=True, auto_set=False, help=\
        """
        Tolerance for Point-in-Plane check
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_process_events_max_value(self):
        return self._vtk_obj.GetProcessEventsMaxValue()
    process_events_max_value = traits.Property(_get_process_events_max_value, help=\
        """
        Methods to change whether the widget responds to interaction. Set
        this to Off to disable interaction. On by default. Subclasses
        must overide set_process_events() to make sure that they pass on
        the flag to all component widgets.
        """
    )

    def _get_process_events_min_value(self):
        return self._vtk_obj.GetProcessEventsMinValue()
    process_events_min_value = traits.Property(_get_process_events_min_value, help=\
        """
        Methods to change whether the widget responds to interaction. Set
        this to Off to disable interaction. On by default. Subclasses
        must overide set_process_events() to make sure that they pass on
        the flag to all component widgets.
        """
    )

    def add_item(self, *args):
        """
        V.add_item(AbstractWidget)
        C++: virtual void AddItem(AbstractWidget *)
        Add / remove a measurement widget
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddItem, *my_args)
        return ret

    def remove_all_items(self):
        """
        V.remove_all_items()
        C++: virtual void RemoveAllItems()
        Add / remove a measurement widget
        """
        ret = self._vtk_obj.RemoveAllItems()
        return ret
        

    def remove_item(self, *args):
        """
        V.remove_item(AbstractWidget)
        C++: virtual void RemoveItem(AbstractWidget *)
        Add / remove a measurement widget
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveItem, *my_args)
        return ret

    def render(self):
        """
        V.render()
        C++: virtual void Render()
        Render the measurements.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Update the measurements. This is automatically called when the
        reslice cursor's axes are change.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('process_events', 'GetProcessEvents'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('tolerance',
    'GetTolerance'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'process_events', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceImageViewerMeasurements, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceImageViewerMeasurements properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['process_events'], [], ['tolerance']),
            title='Edit ResliceImageViewerMeasurements properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceImageViewerMeasurements properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

