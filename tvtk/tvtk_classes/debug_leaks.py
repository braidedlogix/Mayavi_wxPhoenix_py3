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


class DebugLeaks(Object):
    """
    DebugLeaks - identify memory leaks at program termination
    DebugLeaks is used to report memory leaks at the exit of the
    program.
    
    Superclass: Object
    
    It uses ObjectBase::InitializeObjectBase() (called via
    ObjectFactory macros) to intercept the construction of all VTK
    objects. It uses the un_register_internal method of ObjectBase to
    intercept the destruction of all objects.
    
    If not using the ObjectFactory macros to implement New(), be sure
    to call ObjectBase::InitializeObjectBase() explicitly on the
    constructed instance. The rule of thumb is that wherever "new [some
    ObjectBase subclass]" is called,
    ObjectBase::InitializeObjectBase() must be called as well.
    
    There are exceptions to this:
    
    - Command subclasses traditionally do not fully participate in
      DebugLeaks registration, likely because they typically do not
      use TypeMacro to configure get_class_name. initialize_object_base
      should not be called on Command subclasses, and all such classes
    will be automatically registered with DebugLeaks as "vtk_command or
      subclass".
    
    - InformationKey subclasses are not reference counted. They are
      allocated statically and registered automatically with a singleton
      "manager" instance. The manager ensures that all keys are cleaned
      up before exiting, and registration/deregistration with
      DebugLeaks is bypassed.
    
    A table of object name to number of instances is kept. At the exit of
    the program if there are still VTK objects around it will print them
    out. To enable this class add the flag -DVTK_DEBUG_LEAKS to the
    compile line, and rebuild Object and ObjectFactory.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDebugLeaks, obj, update, **traits)
    
    exit_error = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set flag for exiting with an error when leaks are present.
        Default is on when VTK_DEBUG_LEAKS is on and off otherwise.
        """
    )

    def _exit_error_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExitError,
                        self.exit_error)

    def construct_class(self, *args):
        """
        V.construct_class(string)
        C++: static void ConstructClass(const char *classname)
        Call this when creating a class of a given name.
        """
        ret = self._wrap_call(self._vtk_obj.ConstructClass, *args)
        return ret

    def destruct_class(self, *args):
        """
        V.destruct_class(string)
        C++: static void DestructClass(const char *classname)
        Call this when deleting a class of a given name.
        """
        ret = self._wrap_call(self._vtk_obj.DestructClass, *args)
        return ret

    def print_current_leaks(self):
        """
        V.print_current_leaks() -> int
        C++: static int PrintCurrentLeaks()
        Print all the values in the table.  Returns non-zero if there
        were leaks.
        """
        ret = self._vtk_obj.PrintCurrentLeaks()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('exit_error', 'GetExitError'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'exit_error'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DebugLeaks, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DebugLeaks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['exit_error']),
            title='Edit DebugLeaks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DebugLeaks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

