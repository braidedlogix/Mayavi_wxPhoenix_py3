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

from tvtk.tvtk_classes.image_writer import ImageWriter


class MetaImageWriter(ImageWriter):
    """
    MetaImageWriter - write a binary UNC meta image data
    
    Superclass: ImageWriter
    
    One of the formats for which a reader is already available in the
    toolkit is the meta_image file format. This is a fairly simple yet
    powerful format consisting of a text header and a binary data
    section. The following instructions describe how you can write a
    meta_image header for the data that you download from the brain_web
    page.
    
    The minimal structure of the meta_image header is the following:
    
    
       NDims = 3
       dim_size = 181 217 181
       element_type = MET_UCHAR
       element_spacing = 1.0 1.0 1.0
       element_byte_order_msb = False
       element_data_file = brainweb1.raw
    
    * NDims indicate that this is a 3d image. ITK can handle images of
      arbitrary dimension.
    * dim_size indicates the size of the volume in pixels along each
      direction.
    * element_type indicate the primitive type used for pixels. In this
      case is "unsigned char", implying that the data is digitized in 8
      bits / pixel.
    * element_spacing indicates the physical separation between the center
    of one pixel and the center of the next pixel along each direction in
    space. The units used are millimeters.
    * element_byte_order_msb indicates is the data is encoded in little or
      big endian order. You might want to play with this value when
      moving data between different computer platforms.
    * element_data_file is the name of the file containing the raw binary
      data of the image. This file must be in the same directory as the
      header.
    
    meta_image headers are expected to have extension: ".mha" or ".mhd"
    
    Once you write this header text file, it should be possible to read
    the image into your ITK based application using the
    itk::_file_io_to_image_filter class.
    
    @sa
    ImageWriter MetaImageReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMetaImageWriter, obj, update, **traits)
    
    compression = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _compression_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompression,
                        self.compression)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of meta file
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    raw_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the file name of the raw image data.
        """
    )

    def _raw_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRAWFileName,
                        self.raw_file_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input object from the image pipeline.
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('compression',
    'GetCompression'), ('file_name', 'GetFileName'), ('raw_file_name',
    'GetRAWFileName'), ('file_dimensionality', 'GetFileDimensionality'),
    ('file_pattern', 'GetFilePattern'), ('file_prefix', 'GetFilePrefix'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'compression', 'file_dimensionality',
    'file_name', 'file_pattern', 'file_prefix', 'progress_text',
    'raw_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MetaImageWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MetaImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['compression', 'file_dimensionality', 'file_name',
            'file_pattern', 'file_prefix', 'raw_file_name']),
            title='Edit MetaImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MetaImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

