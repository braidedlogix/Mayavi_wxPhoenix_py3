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


class PickingManager(Object):
    """
    PickingManager - Class defines API to manage the picking process.
    
    Superclass: Object
    
    The Picking Manager (PM) coordinates picking across widgets
    simultaneously. It maintains a collection of registered pickers; when
    the manager is picked (e.g. PickingManager::Pick()), a pick is run
    on each picker but only the best picker (e.g. closest to camera
    point) is selected. It finally returns the widget/representation or
    picker that was selected.
    @warning
    Every time a Widget and/or a WidgetRepresentation is
    instantiated, it automatically registers its picker(s) and start
    being managed by delegating all its pick calls to the picking
    manager. It is possible to customize with the management in two ways:
    * at the widget level, the "_manages_picking" variable can be changed
      from the widget/representation class to tell whether to use the
      manager or not.
    * Directly disable the picking manager itself  with the boolean
      variable
    \sa Enabled using PickingManager::EnabledOn(), enabled_off(),
    set_enabled(bool).@par Important: The picking manager is not active by
    default as it slightly reduces the performances when interacting with
    the scene.@par Important: When registering pickers, a null object is
    considered valid because we can managed picker without any associated
    object. It is really important to note that a null object is
    different from one to an other !! This has been done to allow adding
    multiple times the same picker to the manager by not passing the
    referenced object to not force the supression of all pickers
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPickingManager, obj, update, **traits)
    
    enabled = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable management. When disabled, it redirects every pick
        on the picker. By default the picking manager is disabled when
        initialized.
        """
    )

    def _enabled_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnabled,
                        self.enabled_)

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        Set the window interactor associated with the manager.
        """
    )

    optimize_on_interactor_events = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Enable/Disable optimization depending on the
        render_window_interactor events. The mechanism keeps in cache the
        last selected picker as well as the last render time to recompute
        the selection only if a new render event occurred after the last
        selection; otherwise, it simply returns the last picker selected.
        By default picking_managers does use the optimization. Warning:
        Turning off the caching significantly decreases performance.
        """
    )

    def _optimize_on_interactor_events_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOptimizeOnInteractorEvents,
                        self.optimize_on_interactor_events)

    def get_assembly_path(self, *args):
        """
        V.get_assembly_path(float, float, float, AbstractPropPicker,
            Renderer, Object) -> AssemblyPath
        C++: AssemblyPath *GetAssemblyPath(double X, double Y,
            double Z, AbstractPropPicker *picker,
            Renderer *renderer, Object *obj)
        If the picking manager is enabled, it runs the picking selection
        process and return the assembly path associated to the picker
        passed as argument if it is the one mediated. Otherwise it simply
        proceeds to a pick using the given renderer and returns the
        corresponding assembly path.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetAssemblyPath, *my_args)
        return wrap_vtk(ret)

    def get_number_of_objects_linked(self, *args):
        """
        V.get_number_of_objects_linked(AbstractPicker) -> int
        C++: int GetNumberOfObjectsLinked(AbstractPicker *picker)
        Return the number of objects linked with a given picker. Note: a
        null object is counted as an associated object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetNumberOfObjectsLinked, *my_args)
        return ret

    def _get_number_of_pickers(self):
        return self._vtk_obj.GetNumberOfPickers()
    number_of_pickers = traits.Property(_get_number_of_pickers, help=\
        """
        Return the number of pickers registered. If the same picker is
        added multiple times with different objects, it is counted once.
        """
    )

    def add_picker(self, *args):
        """
        V.add_picker(AbstractPicker, Object)
        C++: void AddPicker(AbstractPicker *picker,
            Object *object=0)
        Register a picker into the picking manager. It can be internally
        associated (optional) with an object. This allows the removal of
        all the pickers of the given object. Note that a picker can be
        registered multiple times with different objects.
        \sa remove_picker(), remove_object().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddPicker, *my_args)
        return ret

    def pick(self, *args):
        """
        V.pick(AbstractPicker, Object) -> bool
        C++: bool Pick(AbstractPicker *picker, Object *object)
        V.pick(Object) -> bool
        C++: bool Pick(Object *object)
        V.pick(AbstractPicker) -> bool
        C++: bool Pick(AbstractPicker *picker)
        Run the picking selection process and return true if the object
        is associated with the given picker if it is the best one, false
        otherwise. If optimize_on_interactor_events is true, the pick can
        reuse cached information.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Pick, *my_args)
        return ret

    def remove_object(self, *args):
        """
        V.remove_object(Object)
        C++: void RemoveObject(Object *object)
        Remove all occurences of the object from the registered list. If
        a picker associated with the object is not also associated with
        any other object, it is removed from the list as well.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveObject, *my_args)
        return ret

    def remove_picker(self, *args):
        """
        V.remove_picker(AbstractPicker, Object)
        C++: void RemovePicker(AbstractPicker *picker,
            Object *object=0)
        Unregister the picker from the picking manager. If object is non
        null, only the pair ( picker, object) is removed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemovePicker, *my_args)
        return ret

    _updateable_traits_ = \
    (('enabled', 'GetEnabled'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('optimize_on_interactor_events', 'GetOptimizeOnInteractorEvents'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'optimize_on_interactor_events'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PickingManager, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PickingManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled'], [], ['optimize_on_interactor_events']),
            title='Edit PickingManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PickingManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

