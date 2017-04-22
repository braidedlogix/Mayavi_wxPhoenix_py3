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

from tvtk.tvtk_classes.image_spatial_algorithm import ImageSpatialAlgorithm


class ImageDilateErode3D(ImageSpatialAlgorithm):
    """
    ImageDilateErode3D - Dilates one value and erodes another.
    
    Superclass: ImageSpatialAlgorithm
    
    ImageDilateErode3D will dilate one value and erode another. It
    uses an elliptical foot print, and only erodes/dilates on the
    boundary of the two values.  The filter is restricted to the X, Y,
    and Z axes for now.  It can degenerate to a 2 or 1 dimensional filter
    by setting the kernel size to 1 for a specific axis.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDilateErode3D, obj, update, **traits)
    
    dilate_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Dilate and Erode values to be used by this filter.
        """
    )

    def _dilate_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDilateValue,
                        self.dilate_value)

    erode_value = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Dilate and Erode values to be used by this filter.
        """
    )

    def _erode_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetErodeValue,
                        self.erode_value)

    kernel_size = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(1, 1, 1), cols=3, help=\
        """
        This method sets the size of the neighborhood.  It also sets the
        default middle of the neighborhood and computes the elliptical
        foot print.
        """
    )

    def _kernel_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKernelSize,
                        self.kernel_size)

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
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('dilate_value', 'GetDilateValue'), ('erode_value',
    'GetErodeValue'), ('kernel_size', 'GetKernelSize'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'split_mode', 'desired_bytes_per_piece',
    'dilate_value', 'enable_smp', 'erode_value',
    'global_default_enable_smp', 'kernel_size', 'minimum_piece_size',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDilateErode3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDilateErode3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['split_mode'], ['desired_bytes_per_piece', 'dilate_value',
            'enable_smp', 'erode_value', 'global_default_enable_smp',
            'kernel_size', 'minimum_piece_size', 'number_of_threads']),
            title='Edit ImageDilateErode3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDilateErode3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

