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

from tvtk.tvtk_classes.poly_data_mapper2d import PolyDataMapper2D


class OpenGLPolyDataMapper2D(PolyDataMapper2D):
    """
    OpenGLPolyDataMapper2D - 2d poly_data support for open_gl
    
    Superclass: PolyDataMapper2D
    
    OpenGLPolyDataMapper2D provides 2d poly_data annotation support for
    vtk under open_gl.  Normally the user should use PolyDataMapper2D
    which in turn will use this class.
    
    @sa
    PolyDataMapper2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLPolyDataMapper2D, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set the input to the mapper.
        """
    )

    def _get_vbo(self):
        return wrap_vtk(self._vtk_obj.GetVBO())
    vbo = traits.Property(_get_vbo, help=\
        """
        Return the mapper's vertex buffer object.
        """
    )

    _updateable_traits_ = \
    (('scalar_visibility', 'GetScalarVisibility'),
    ('transform_coordinate_use_double',
    'GetTransformCoordinateUseDouble'), ('use_lookup_table_scalar_range',
    'GetUseLookupTableScalarRange'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('color_mode',
    'GetColorMode'), ('scalar_mode', 'GetScalarMode'), ('scalar_range',
    'GetScalarRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_visibility',
    'transform_coordinate_use_double', 'use_lookup_table_scalar_range',
    'color_mode', 'scalar_mode', 'progress_text', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLPolyDataMapper2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLPolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['scalar_visibility', 'transform_coordinate_use_double',
            'use_lookup_table_scalar_range'], ['color_mode', 'scalar_mode'],
            ['scalar_range']),
            title='Edit OpenGLPolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLPolyDataMapper2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

