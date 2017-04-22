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


class Shader(Object):
    """
    Shader - encapsulate a glsl shader
    
    Superclass: Object
    
    Shader represents a shader, vertex, fragment, geometry etc
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkShader, obj, update, **traits)
    
    def _get_source(self):
        return self._vtk_obj.GetSource()
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        arg)
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        Get the source for the shader.
        """
    )

    def _get_error(self):
        return self._vtk_obj.GetError()
    error = traits.Property(_get_error, help=\
        """
        Get the error message (empty if none) for the shader.
        """
    )

    def _get_handle(self):
        return self._vtk_obj.GetHandle()
    handle = traits.Property(_get_handle, help=\
        """
        Get the handle of the shader.
        """
    )

    def cleanup(self):
        """
        V.cleanup()
        C++: void Cleanup()
        Delete the shader.
        
        ote This should only be done once the shader_program is done with
        the Shader.
        """
        ret = self._vtk_obj.Cleanup()
        return ret
        

    def compile(self):
        """
        V.compile() -> bool
        C++: bool Compile()
        Compile the shader.
        
        ote A valid context must to current in order to compile the
        shader.
        """
        ret = self._vtk_obj.Compile()
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
            return super(Shader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Shader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Shader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Shader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

