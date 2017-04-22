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

from tvtk.tvtk_classes.default_pass import DefaultPass


class LightingMapPass(DefaultPass):
    """
    LightingMapPass - TO DO
    
    Superclass: DefaultPass
    
    Renders lighting information directly instead of final shaded colors.
    The information keys allow the selection of either normal rendering
    or luminance. For normals, the (nx, ny, nz) tuple are rendered
    directly into the (r,g,b) fragment. For luminance, the diffuse and
    specular intensities are rendered into the red and green channels,
    respectively. The blue channel is zero. For both luminances and
    normals, the alpha channel is set to 1.0 if present.
    
    @sa
    RenderPass DefaultPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLightingMapPass, obj, update, **traits)
    
    def RENDER_LUMINANCE(self):
        """
        V.render__luminance() -> InformationIntegerKey
        C++: static InformationIntegerKey *RENDER_LUMINANCE()
        If this key exists on the property_keys of a prop, the active
        scalar array on the prop will be rendered as its color. This key
        is mutually exclusive with the RENDER_LUMINANCE key.
        """
        ret = wrap_vtk(self._vtk_obj.RENDER_LUMINANCE())
        return ret
        

    def RENDER_NORMALS(self):
        """
        V.render__normals() -> InformationIntegerKey
        C++: static InformationIntegerKey *RENDER_NORMALS()
        if this key exists on the propery_keys of a prop, the active
        vector array on the prop will be rendered as its color. This key
        is mutually exclusive with the RENDER_LUMINANCE key.
        """
        ret = wrap_vtk(self._vtk_obj.RENDER_NORMALS())
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
            return super(LightingMapPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LightingMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit LightingMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LightingMapPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

