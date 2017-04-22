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

from tvtk.tvtk_classes.image_stencil_source import ImageStencilSource


class PolyDataToImageStencil(ImageStencilSource):
    """
    PolyDataToImageStencil - use polydata to mask an image
    
    Superclass: ImageStencilSource
    
    The PolyDataToImageStencil class will convert polydata into an
    image stencil.  The polydata can either be a closed surface mesh or a
    series of polyline contours (one contour per slice).
    @warning
    If contours are provided, the contours must be aligned with the Z
    planes.  Other contour orientations are not supported.
    @sa
    ImageStencil ImageAccumulate ImageBlend ImageReslice
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataToImageStencil, obj, update, **traits)
    
    tolerance = traits.Trait(7.62939453125e-06, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The tolerance for including a voxel inside the stencil. This is
        in fractions of a voxel, and must be between 0 and 1. Tolerance
        is only applied in the x and y directions, not in z. Setting the
        tolerance to zero disables all tolerance checks and might result
        in faster performance.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the implicit function to convert into a stencil.
        """
    )

    def set_input_data(self, *args):
        """
        V.set_input_data(PolyData)
        C++: virtual void SetInputData(PolyData *)
        Specify the implicit function to convert into a stencil.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('tolerance',
    'GetTolerance'), ('output_origin', 'GetOutputOrigin'),
    ('output_spacing', 'GetOutputSpacing'), ('output_whole_extent',
    'GetOutputWholeExtent'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'output_origin', 'output_spacing',
    'output_whole_extent', 'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataToImageStencil, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['output_origin', 'output_spacing',
            'output_whole_extent', 'tolerance']),
            title='Edit PolyDataToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataToImageStencil properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

