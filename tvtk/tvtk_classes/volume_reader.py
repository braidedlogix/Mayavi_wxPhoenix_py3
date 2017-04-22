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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class VolumeReader(ImageAlgorithm):
    """
    VolumeReader - read image files
    
    Superclass: ImageAlgorithm
    
    VolumeReader is a source object that reads image files.
    
    volume_reader creates structured point datasets. The dimension of the
    dataset depends upon the number of files read. Reading a single file
    results in a 2d image, while reading more than one file results in a
    3d volume.
    
    File names are created using file_pattern and file_prefix as follows:
    sprintf (filename, file_pattern, file_prefix, number); where number is
    in the range image_range[_0] to image_range[_1]. If image_range[_1] <=
    image_range[_0], then slice number image_range[_0] is read. Thus to read
    an image set image_range[_0] = image_range[_1] = slice number. The
    default behavior is to read a single file (i.e., image slice 1).
    
    The data_mask instance variable is used to read data files with
    imbedded connectivity or segmentation information. For example, some
    data has the high order bit set to indicate connected surface. The
    data_mask allows you to select this data. Other important ivars
    include header_size, which allows you to skip over initial info, and
    swap_bytes, which turns on/off byte swapping. Consider using
    ImageReader as a replacement.
    
    @sa
    SliceCubes MarchingCubes PNMReader Volume16Reader
    ImageReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeReader, obj, update, **traits)
    
    data_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _data_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataOrigin,
                        self.data_origin)

    data_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _data_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataSpacing,
                        self.data_spacing)

    file_pattern = traits.String('%s.%d', enter_set=True, auto_set=False, help=\
        """
        The sprintf format used to build filename from file_prefix and
        number.
        """
    )

    def _file_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePattern,
                        self.file_pattern)

    file_prefix = tvtk_base.vtk_file_prefix("", help=\
        """
        Specify file prefix for the image file(s).
        """
    )

    def _file_prefix_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePrefix,
                        self.file_prefix)

    image_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(1, 1), cols=2, help=\
        """
        
        """
    )

    def _image_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageRange,
                        self.image_range)

    def get_image(self, *args):
        """
        V.get_image(int) -> ImageData
        C++: virtual ImageData *GetImage(int ImageNumber)
        Other objects make use of this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetImage, *args)
        return wrap_vtk(ret)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('data_origin',
    'GetDataOrigin'), ('data_spacing', 'GetDataSpacing'), ('file_pattern',
    'GetFilePattern'), ('file_prefix', 'GetFilePrefix'), ('image_range',
    'GetImageRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'data_origin', 'data_spacing', 'file_pattern',
    'file_prefix', 'image_range', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['data_origin', 'data_spacing', 'file_pattern',
            'file_prefix', 'image_range']),
            title='Edit VolumeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

