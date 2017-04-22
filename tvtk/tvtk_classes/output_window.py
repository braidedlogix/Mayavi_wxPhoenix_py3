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


class OutputWindow(Object):
    """
    OutputWindow - base class for writing debug output to a console
    
    Superclass: Object
    
    This class is used to encapsulate all text output, so that it will
    work with operating systems that have a stdout and stderr, and ones
    that do not.  (i.e windows does not).  Sub-classes can be provided
    which can redirect the output to a window.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOutputWindow, obj, update, **traits)
    
    def _get_instance(self):
        return wrap_vtk(self._vtk_obj.GetInstance())
    def _set_instance(self, arg):
        old_val = self._get_instance()
        self._wrap_call(self._vtk_obj.SetInstance,
                        deref_vtk(arg))
        self.trait_property_changed('instance', old_val, arg)
    instance = traits.Property(_get_instance, _set_instance, help=\
        """
        Return the singleton instance with no reference counting.
        """
    )

    def display_debug_text(self, *args):
        """
        V.display_debug_text(string)
        C++: virtual void DisplayDebugText(const char *)"""
        ret = self._wrap_call(self._vtk_obj.DisplayDebugText, *args)
        return ret

    def display_error_text(self, *args):
        """
        V.display_error_text(string)
        C++: virtual void DisplayErrorText(const char *)
        Display the text. Four virtual methods exist, depending on the
        type of message to display. This allows redirection or
        reformatting of the messages. The default implementation uses
        display_text for all.
        """
        ret = self._wrap_call(self._vtk_obj.DisplayErrorText, *args)
        return ret

    def display_generic_warning_text(self, *args):
        """
        V.display_generic_warning_text(string)
        C++: virtual void DisplayGenericWarningText(const char *)
        Display the text. Four virtual methods exist, depending on the
        type of message to display. This allows redirection or
        reformatting of the messages. The default implementation uses
        display_text for all.
        """
        ret = self._wrap_call(self._vtk_obj.DisplayGenericWarningText, *args)
        return ret

    def display_text(self, *args):
        """
        V.display_text(string)
        C++: virtual void DisplayText(const char *)
        Display the text. Four virtual methods exist, depending on the
        type of message to display. This allows redirection or
        reformatting of the messages. The default implementation uses
        display_text for all.
        """
        ret = self._wrap_call(self._vtk_obj.DisplayText, *args)
        return ret

    def display_warning_text(self, *args):
        """
        V.display_warning_text(string)
        C++: virtual void DisplayWarningText(const char *)
        Display the text. Four virtual methods exist, depending on the
        type of message to display. This allows redirection or
        reformatting of the messages. The default implementation uses
        display_text for all.
        """
        ret = self._wrap_call(self._vtk_obj.DisplayWarningText, *args)
        return ret

    def prompt_user_off(self):
        """
        V.prompt_user_off()
        C++: void PromptUserOff()
        If prompt_user is set to true then each time a line of text is
        displayed, the user is asked if they want to keep getting
        messages.
        """
        ret = self._vtk_obj.PromptUserOff()
        return ret
        

    def prompt_user_on(self):
        """
        V.prompt_user_on()
        C++: void PromptUserOn()
        If prompt_user is set to true then each time a line of text is
        displayed, the user is asked if they want to keep getting
        messages.
        """
        ret = self._vtk_obj.PromptUserOn()
        return ret
        

    def set_prompt_user(self, *args):
        """
        V.set_prompt_user(int)
        C++: void SetPromptUser(int a)
        If prompt_user is set to true then each time a line of text is
        displayed, the user is asked if they want to keep getting
        messages.
        """
        ret = self._wrap_call(self._vtk_obj.SetPromptUser, *args)
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
            return super(OutputWindow, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OutputWindow properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

