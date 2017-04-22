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


class TextureUnitManager(Object):
    """
    TextureUnitManager - allocate/free texture units.
    
    Superclass: Object
    
    TextureUnitManager is a central place used by shaders to reserve a
    texture unit ( Allocate() ) or release it ( Free() ).
    
    Don't create a TextureUnitManager, query it from the
    OpenGLRenderWindow
    
    @sa
    OpenGLRenderWindow
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextureUnitManager, obj, update, **traits)
    
    def _get_context(self):
        return wrap_vtk(self._vtk_obj.GetContext())
    def _set_context(self, arg):
        old_val = self._get_context()
        self._wrap_call(self._vtk_obj.SetContext,
                        deref_vtk(arg))
        self.trait_property_changed('context', old_val, arg)
    context = traits.Property(_get_context, _set_context, help=\
        """
        Get/Set the context. This does not increase the reference count
        of the context to avoid reference loops. set_context() may raise
        an error is the open_gl context does not support the required
        open_gl extensions.
        """
    )

    def _get_number_of_texture_units(self):
        return self._vtk_obj.GetNumberOfTextureUnits()
    number_of_texture_units = traits.Property(_get_number_of_texture_units, help=\
        """
        Number of texture units supported by the open_gl context.
        """
    )

    def allocate(self, *args):
        """
        V.allocate() -> int
        C++: virtual int Allocate()
        V.allocate(int) -> int
        C++: virtual int Allocate(int unit)
        Reserve a texture unit. It returns its number. It returns -1 if
        the allocation failed (because there are no more texture units
        left).
        \post valid_result: result==-1 || result>=0 &&
            result<this->_get_number_of_texture_units())
        \post allocated: result==-1 || this->_is_allocated(result)
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def free(self, *args):
        """
        V.free(int)
        C++: virtual void Free(int textureUnitId)
        Release a texture unit.
        \pre valid_texture_unit_id: texture_unit_id>=_0 &&
            texture_unit_id<this->_get_number_of_texture_units()
        \pre allocated_texture_unit_id: this->_is_allocated(texture_unit_id)
        """
        ret = self._wrap_call(self._vtk_obj.Free, *args)
        return ret

    def is_allocated(self, *args):
        """
        V.is_allocated(int) -> bool
        C++: bool IsAllocated(int textureUnitId)
        Tell if texture unit `texture_unit_id' is already allocated.
        \pre valid_texture_unit_id_range : texture_unit_id>=_0 &&
            texture_unit_id<this->_get_number_of_texture_units()
        """
        ret = self._wrap_call(self._vtk_obj.IsAllocated, *args)
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
            return super(TextureUnitManager, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextureUnitManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit TextureUnitManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextureUnitManager properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

