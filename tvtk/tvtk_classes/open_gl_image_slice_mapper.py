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

from tvtk.tvtk_classes.image_slice_mapper import ImageSliceMapper


class OpenGLImageSliceMapper(ImageSliceMapper):
    """
    OpenGLImageSliceMapper - open_gl mapper for image slice display
    
    Superclass: ImageSliceMapper
    
    OpenGLImageSliceMapper is a concrete implementation of the
    abstract class ImageSliceMapper that interfaces to the open_gl
    library.@par Thanks: Thanks to David Gobbi at the Seaman Family MR
    Centre and Dept. of Clinical Neurosciences, Foothills Medical Centre,
    Calgary, for providing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLImageSliceMapper, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        The input data for this mapper.
        """
    )

    _updateable_traits_ = \
    (('cropping', 'GetCropping'), ('background', 'GetBackground'),
    ('border', 'GetBorder'), ('slice_at_focal_point',
    'GetSliceAtFocalPoint'), ('slice_faces_camera',
    'GetSliceFacesCamera'), ('streaming', 'GetStreaming'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('orientation',
    'GetOrientation'), ('cropping_region', 'GetCroppingRegion'),
    ('slice_number', 'GetSliceNumber'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'background', 'border', 'cropping', 'debug',
    'global_warning_display', 'release_data_flag', 'slice_at_focal_point',
    'slice_faces_camera', 'streaming', 'orientation', 'cropping_region',
    'number_of_threads', 'progress_text', 'slice_number'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLImageSliceMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLImageSliceMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['background', 'border', 'cropping', 'slice_at_focal_point',
            'slice_faces_camera', 'streaming'], ['orientation'],
            ['cropping_region', 'number_of_threads', 'slice_number']),
            title='Edit OpenGLImageSliceMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLImageSliceMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

