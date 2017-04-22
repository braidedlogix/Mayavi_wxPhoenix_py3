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


class Version(Object):
    """
    Version - Versioning class for vtk
    
    Superclass: Object
    
    Holds methods for defining/determining the current vtk version
    (major, minor, build).
    
    @warning
    This file will change frequently to update the vtk_source_version which
    timestamps a particular source release.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVersion, obj, update, **traits)
    
    def _get_vtk_build_version(self):
        return self._vtk_obj.GetVTKBuildVersion()
    vtk_build_version = traits.Property(_get_vtk_build_version, help=\
        """
        
        """
    )

    def _get_vtk_major_version(self):
        return self._vtk_obj.GetVTKMajorVersion()
    vtk_major_version = traits.Property(_get_vtk_major_version, help=\
        """
        
        """
    )

    def _get_vtk_minor_version(self):
        return self._vtk_obj.GetVTKMinorVersion()
    vtk_minor_version = traits.Property(_get_vtk_minor_version, help=\
        """
        
        """
    )

    def _get_vtk_source_version(self):
        return self._vtk_obj.GetVTKSourceVersion()
    vtk_source_version = traits.Property(_get_vtk_source_version, help=\
        """
        
        """
    )

    def _get_vtk_version(self):
        return self._vtk_obj.GetVTKVersion()
    vtk_version = traits.Property(_get_vtk_version, help=\
        """
        Return the version of vtk this object is a part of. A variety of
        methods are included. get_vtk_source_version returns a string with
        an identifier which timestamps a particular source tree.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Version, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Version properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Version properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Version properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

