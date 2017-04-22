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

from tvtk.tvtk_classes.generic_movie_writer import GenericMovieWriter


class AVIWriter(GenericMovieWriter):
    """
    AVIWriter - Writes Windows AVI files.
    
    Superclass: GenericMovieWriter
    
    AVIWriter writes AVI files. Note that this class in only available
    on the Microsoft Windows platform. The data type of the file is
    unsigned char regardless of the input type.
    @sa
    GenericMovieWriter MPEG2Writer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAVIWriter, obj, update, **traits)
    
    prompt_compression_options = tvtk_base.false_bool_trait(help=\
        """
        Set/Get if the user should be prompted for compression options,
        i.e. pick a compressor, set the compression rate (override Rate),
        etc.). Default is OFF (legacy).
        """
    )

    def _prompt_compression_options_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPromptCompressionOptions,
                        self.prompt_compression_options_)

    compressor_four_cc = traits.String('MSVC', enter_set=True, auto_set=False, help=\
        """
        Set/Get the compressor four_cc. A four_cc (literally,
        four-character code) is a sequence of four bytes used to uniquely
        identify data formats. [...] One of the most well-known uses of
        four_c_cs is to identify the video codec used in AVI files. Common
        identifiers include DIVX, XVID, and H264.
        http://en.wikipedia.org/wiki/_four_cc. Default value is:
        - MSVC Other examples include:
        - DIB: Full Frames (Uncompressed)
        - LAGS: Lagarith Lossless Codec
        - MJPG: M-JPG, aka Motion JPEG (say, Pegasus Imaging pic_video
          M-JPEG) Links:
        - http://www.fourcc.org/
        - http://www.microsoft.com/whdc/archive/fourcc.mspx
        - http://abcavi.kibi.ru/fourcc.php
        """
    )

    def _compressor_four_cc_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompressorFourCC,
                        self.compressor_four_cc)

    quality = traits.Trait(10000, 10000, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set/Get the compression quality. 0 means worst quality and
        smallest file size 2 means best quality and largest file size
        """
    )

    def _quality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuality,
                        self.quality)

    rate = traits.Trait(1000, traits.Range(1, 5000, enter_set=True, auto_set=False), help=\
        """
        Set/Get the frame rate, in frame/s.
        """
    )

    def _rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRate,
                        self.rate)

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

    _updateable_traits_ = \
    (('prompt_compression_options', 'GetPromptCompressionOptions'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('compressor_four_cc', 'GetCompressorFourCC'), ('quality',
    'GetQuality'), ('rate', 'GetRate'), ('file_name', 'GetFileName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'prompt_compression_options', 'release_data_flag',
    'compressor_four_cc', 'file_name', 'progress_text', 'quality',
    'rate'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AVIWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AVIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['prompt_compression_options'], [], ['compressor_four_cc',
            'file_name', 'quality', 'rate']),
            title='Edit AVIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AVIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

