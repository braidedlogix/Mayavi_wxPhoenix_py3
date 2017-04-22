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

from tvtk.tvtk_classes.video_source import VideoSource


class Win32VideoSource(VideoSource):
    """
    Win32VideoSource - Video-for-Windows video digitizer
    
    Superclass: VideoSource
    
    Win32VideoSource grabs frames or streaming video from a Video for
    Windows compatible device on the Win32 platform.
    @warning
    With some capture cards, if this class is leaked and
    release_system_resources is not called, you may have to reboot before
    you can capture again. VideoSource used to keep a global list and
    delete the video sources if your program leaked, due to exit crashes
    that was removed.
    
    @sa
    VideoSource MILVideoSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWin32VideoSource, obj, update, **traits)
    
    preview = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the preview (overlay) window.
        """
    )

    def _preview_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreview,
                        self.preview_)

    frame_rate = traits.Float(30.0, enter_set=True, auto_set=False, help=\
        """
        Request a particular frame rate (default 30 frames per second).
        """
    )

    def _frame_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameRate,
                        self.frame_rate)

    frame_size = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(320, 240, 1), cols=3, help=\
        """
        Request a particular frame size (set the third value to 1).
        """
    )

    def _frame_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFrameSize,
                        self.frame_size)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def local_internal_grab(self, *args):
        """
        V.local_internal_grab(void)
        C++: void LocalInternalGrab(void *)
        For internal use only
        """
        ret = self._wrap_call(self._vtk_obj.LocalInternalGrab, *args)
        return ret

    def on_parent_wnd_destroy(self):
        """
        V.on_parent_wnd_destroy()
        C++: void OnParentWndDestroy()
        For internal use only
        """
        ret = self._vtk_obj.OnParentWndDestroy()
        return ret
        

    def video_format_dialog(self):
        """
        V.video_format_dialog()
        C++: void VideoFormatDialog()
        Bring up a modal dialog box for video format selection.
        """
        ret = self._vtk_obj.VideoFormatDialog()
        return ret
        

    def video_source_dialog(self):
        """
        V.video_source_dialog()
        C++: void VideoSourceDialog()
        Bring up a modal dialog box for video input selection.
        """
        ret = self._vtk_obj.VideoSourceDialog()
        return ret
        

    _updateable_traits_ = \
    (('preview', 'GetPreview'), ('auto_advance', 'GetAutoAdvance'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_format', 'GetOutputFormat'), ('frame_rate', 'GetFrameRate'),
    ('frame_size', 'GetFrameSize'), ('clip_region', 'GetClipRegion'),
    ('data_origin', 'GetDataOrigin'), ('data_spacing', 'GetDataSpacing'),
    ('frame_buffer_size', 'GetFrameBufferSize'), ('frame_count',
    'GetFrameCount'), ('number_of_output_frames',
    'GetNumberOfOutputFrames'), ('opacity', 'GetOpacity'),
    ('output_whole_extent', 'GetOutputWholeExtent'), ('start_time_stamp',
    'GetStartTimeStamp'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_advance', 'debug', 'global_warning_display',
    'preview', 'release_data_flag', 'output_format', 'clip_region',
    'data_origin', 'data_spacing', 'frame_buffer_size', 'frame_count',
    'frame_rate', 'frame_size', 'number_of_output_frames', 'opacity',
    'output_whole_extent', 'progress_text', 'start_time_stamp'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Win32VideoSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Win32VideoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_advance', 'preview'], ['output_format'], ['clip_region',
            'data_origin', 'data_spacing', 'frame_buffer_size', 'frame_count',
            'frame_rate', 'frame_size', 'number_of_output_frames', 'opacity',
            'output_whole_extent', 'start_time_stamp']),
            title='Edit Win32VideoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Win32VideoSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

