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


class ValuePass(DefaultPass):
    """
    ValuePass - Renders geometry using the values of a field array as
    fragment colors.
    
    Superclass: DefaultPass
    
    The output can be used for deferred color mapping. It supports using
    arrays of either point or cell data. The target array can be selected
    by setting an array name/id and a component number. Only opaque
    geometry is supported.
    
    There are two rendering modes available:
    
    * INVERTIBLE_LUT  Encodes array values as RGB data and renders the
      result to the default framebuffer.
    
    * FLOATING_POINT  Renders actual array values as floating point data
      to an internal rgba32f framebuffer.  This class binds and unbinds
      the framebuffer on each render pass.
    
    @sa
    RenderPass DefaultPass ValuePassHelper Mapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkValuePass, obj, update, **traits)
    
    rendering_mode = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _rendering_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderingMode,
                        self.rendering_mode)

    def get_float_image_data(self, *args):
        """
        V.get_float_image_data(int, int, int, void)
        C++: void GetFloatImageData(int const format, int const width,
            int const height, void *data)
        Interface to get the rendered image in FLOATING_POINT mode.  Low
        level API, a format for the internal gl_read_pixels call can be
        specified. 'data' is expected to be allocated and cleaned-up by
        the caller.
        """
        ret = self._wrap_call(self._vtk_obj.GetFloatImageData, *args)
        return ret

    def get_float_image_data_array(self, *args):
        """
        V.get_float_image_data_array(Renderer) -> FloatArray
        C++: FloatArray *GetFloatImageDataArray(Renderer *ren)
        Interface to get the rendered image in FLOATING_POINT mode. 
        Returns a single component array containing the rendered values. 
        The returned array is owned by ValuePass so it is intended to
        be deep copied.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetFloatImageDataArray, *my_args)
        return wrap_vtk(ret)

    def _get_float_image_extents(self):
        return self._vtk_obj.GetFloatImageExtents()
    float_image_extents = traits.Property(_get_float_image_extents, help=\
        """
        Interface to get the rendered image in FLOATING_POINT mode. 
        Image extents of the value array.
        """
    )

    def ARRAY_COMPONENT(self):
        """
        V.array__component() -> InformationIntegerKey
        C++: static InformationIntegerKey *ARRAY_COMPONENT()
        Passed down the rendering pipeline to control what data array to
        draw.
        """
        ret = wrap_vtk(self._vtk_obj.ARRAY_COMPONENT())
        return ret
        

    def ARRAY_ID(self):
        """
        V.array__id() -> InformationIntegerKey
        C++: static InformationIntegerKey *ARRAY_ID()
        Passed down the rendering pipeline to control what data array to
        draw.
        """
        ret = wrap_vtk(self._vtk_obj.ARRAY_ID())
        return ret
        

    def ARRAY_MODE(self):
        """
        V.array__mode() -> InformationIntegerKey
        C++: static InformationIntegerKey *ARRAY_MODE()
        Passed down the rendering pipeline to control what data array to
        draw.
        """
        ret = wrap_vtk(self._vtk_obj.ARRAY_MODE())
        return ret
        

    def ARRAY_NAME(self):
        """
        V.array__name() -> InformationStringKey
        C++: static InformationStringKey *ARRAY_NAME()
        Passed down the rendering pipeline to control what data array to
        draw.
        """
        ret = wrap_vtk(self._vtk_obj.ARRAY_NAME())
        return ret
        

    def is_floating_point_mode_supported(self, *args):
        """
        V.is_floating_point_mode_supported(RenderWindow) -> bool
        C++: bool IsFloatingPointModeSupported(RenderWindow *renWin)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsFloatingPointModeSupported, *my_args)
        return ret

    def RELOAD_DATA(self):
        """
        V.reload__data() -> InformationIntegerKey
        C++: static InformationIntegerKey *RELOAD_DATA()
        Passed down the rendering pipeline to control what data array to
        draw.
        """
        ret = wrap_vtk(self._vtk_obj.RELOAD_DATA())
        return ret
        

    def RENDER_VALUES(self):
        """
        V.render__values() -> InformationIntegerKey
        C++: static InformationIntegerKey *RENDER_VALUES()"""
        ret = wrap_vtk(self._vtk_obj.RENDER_VALUES())
        return ret
        

    def SCALAR_MODE(self):
        """
        V.scalar__mode() -> InformationIntegerKey
        C++: static InformationIntegerKey *SCALAR_MODE()
        Passed down the rendering pipeline to control what data array to
        draw.
        """
        ret = wrap_vtk(self._vtk_obj.SCALAR_MODE())
        return ret
        

    def SCALAR_RANGE(self):
        """
        V.scalar__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *SCALAR_RANGE()
        Passed down the rendering pipeline to control what data array to
        draw.
        """
        ret = wrap_vtk(self._vtk_obj.SCALAR_RANGE())
        return ret
        

    def set_input_array_to_process(self, *args):
        """
        V.set_input_array_to_process(int, string)
        C++: void SetInputArrayToProcess(int fieldAssociation,
            const char *name)
        V.set_input_array_to_process(int, int)
        C++: void SetInputArrayToProcess(int fieldAssociation,
            int fieldAttributeType)"""
        ret = self._wrap_call(self._vtk_obj.SetInputArrayToProcess, *args)
        return ret

    def set_input_component_to_process(self, *args):
        """
        V.set_input_component_to_process(int)
        C++: void SetInputComponentToProcess(int component)"""
        ret = self._wrap_call(self._vtk_obj.SetInputComponentToProcess, *args)
        return ret

    def set_scalar_range(self, *args):
        """
        V.set_scalar_range(float, float)
        C++: void SetScalarRange(double min, double max)"""
        ret = self._wrap_call(self._vtk_obj.SetScalarRange, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('rendering_mode', 'GetRenderingMode'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'rendering_mode'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ValuePass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ValuePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['rendering_mode']),
            title='Edit ValuePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ValuePass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

