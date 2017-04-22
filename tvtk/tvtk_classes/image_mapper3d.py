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

from tvtk.tvtk_classes.abstract_mapper3d import AbstractMapper3D


class ImageMapper3D(AbstractMapper3D):
    """
    ImageMapper3D - abstract class for mapping images to the screen
    
    Superclass: AbstractMapper3D
    
    ImageMapper3D is a mapper that will draw a 2d image, or a slice of
    a 3d image.  The slice plane can be set automatically follow the
    camera, so that it slices through the focal point and faces the
    camera.@par Thanks: Thanks to David Gobbi at the Seaman Family MR
    Centre and Dept. of Clinical Neurosciences, Foothills Medical Centre,
    Calgary, for providing this class.
    @sa
    Image ImageProperty ImageResliceMapper ImageSliceMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMapper3D, obj, update, **traits)
    
    background = tvtk_base.false_bool_trait(help=\
        """
        Instead of rendering only to the image border, render out to the
        viewport boundary with the background color.  The background
        color will be the lowest color on the lookup table that is being
        used for the image.
        """
    )

    def _background_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackground,
                        self.background_)

    border = tvtk_base.false_bool_trait(help=\
        """
        Instead of displaying the image only out to the image bounds,
        include a half-voxel border around the image. Within this border,
        the image values will be extrapolated rather than interpolated.
        """
    )

    def _border_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorder,
                        self.border_)

    slice_at_focal_point = tvtk_base.false_bool_trait(help=\
        """
        Automatically set the slice position to the camera focal point.
        This provides a convenient way to interact with the image, since
        most Interactors directly control the camera.
        """
    )

    def _slice_at_focal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceAtFocalPoint,
                        self.slice_at_focal_point_)

    slice_faces_camera = tvtk_base.false_bool_trait(help=\
        """
        Automatically set the slice orientation so that it faces the
        camera. This provides a convenient way to interact with the
        image, since most Interactors directly control the camera.
        """
    )

    def _slice_faces_camera_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceFacesCamera,
                        self.slice_faces_camera_)

    streaming = tvtk_base.false_bool_trait(help=\
        """
        Turn on streaming, to pull the minimum amount of data from the
        input. Streaming decreases the memory required to display large
        images, since only one slice will be pulled through the input
        pipeline if only one slice is mapped to the screen.  The default
        behavior is to pull the full 3d input extent through the input
        pipeline, but to do this only when the input data changes.  The
        default behavior results in much faster follow-up renders when
        the input data is static.
        """
    )

    def _streaming_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStreaming,
                        self.streaming_)

    number_of_threads = traits.Trait(12, traits.Range(1, 64, enter_set=True, auto_set=False), help=\
        """
        The number of threads to create when rendering.
        """
    )

    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

    def _get_data_object_input(self):
        return wrap_vtk(self._vtk_obj.GetDataObjectInput())
    data_object_input = traits.Property(_get_data_object_input, help=\
        """
        The input data for this mapper.
        """
    )

    def _get_data_set_input(self):
        return wrap_vtk(self._vtk_obj.GetDataSetInput())
    data_set_input = traits.Property(_get_data_set_input, help=\
        """
        The input data for this mapper.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        The input data for this mapper.
        """
    )

    def _get_slice_plane(self):
        return wrap_vtk(self._vtk_obj.GetSlicePlane())
    slice_plane = traits.Property(_get_slice_plane, help=\
        """
        A plane that describes what slice of the input is being rendered
        by the mapper.  This plane is in world coordinates, not data
        coordinates.  Before using this plane, call Update or
        update_information to make sure the plane is up-to-date. These
        methods are automatically called by Render.
        """
    )

    def get_slice_plane_in_data_coords(self, *args):
        """
        V.get_slice_plane_in_data_coords(Matrix4x4, [float, float, float,
            float])
        C++: virtual void GetSlicePlaneInDataCoords(
            Matrix4x4 *propMatrix, double plane[4])
        Get the plane as a homogeneous 4-vector that gives the plane
        equation coefficients.  The prop_3d matrix must be provided so
        that the plane can be converted to data coords.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetSlicePlaneInDataCoords, *my_args)
        return ret

    def render(self, *args):
        """
        V.render(Renderer, ImageSlice)
        C++: virtual void Render(Renderer *renderer,
            ImageSlice *prop)
        This should only be called by the renderer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    def set_input_data(self, *args):
        """
        V.set_input_data(ImageData)
        C++: void SetInputData(ImageData *input)
        The input data for this mapper.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('background', 'GetBackground'), ('border', 'GetBorder'),
    ('slice_at_focal_point', 'GetSliceAtFocalPoint'),
    ('slice_faces_camera', 'GetSliceFacesCamera'), ('streaming',
    'GetStreaming'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_threads', 'GetNumberOfThreads'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'background', 'border', 'debug',
    'global_warning_display', 'release_data_flag', 'slice_at_focal_point',
    'slice_faces_camera', 'streaming', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMapper3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['background', 'border', 'slice_at_focal_point',
            'slice_faces_camera', 'streaming'], [], ['number_of_threads']),
            title='Edit ImageMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

