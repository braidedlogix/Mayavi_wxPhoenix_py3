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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageIdealLowPass(ThreadedImageAlgorithm):
    """
    ImageIdealLowPass - Simple frequency domain band pass.
    
    Superclass: ThreadedImageAlgorithm
    
    This filter only works on an image after it has been converted to
    frequency domain by a ImageFFT filter.  A ImageRFFT filter can
    be used to convert the output back into the spatial domain.
    ImageIdealLowPass just sets a portion of the image to zero.  The
    result is an image with a lot of ringing.  Input and Output must be
    doubles. Dimensionality is set when the axes are set.  Defaults to 2d
    on X and Y axes.
    
    @sa
    ImageButterworthLowPass ImageIdealHighPass ImageFFT
    ImageRFFT
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageIdealLowPass, obj, update, **traits)
    
    cut_off = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1e+299, 1e+299, 1e+299), cols=3, help=\
        """
        
        """
    )

    def _cut_off_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCutOff,
                        self.cut_off)

    x_cut_off = traits.Float(1e+299, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cutoff frequency for each axis. The values are
        specified in the order X, Y, Z, Time. Units: Cycles per world
        unit (as defined by the data spacing).
        """
    )

    def _x_cut_off_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXCutOff,
                        self.x_cut_off)

    y_cut_off = traits.Float(1e+299, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cutoff frequency for each axis. The values are
        specified in the order X, Y, Z, Time. Units: Cycles per world
        unit (as defined by the data spacing).
        """
    )

    def _y_cut_off_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYCutOff,
                        self.y_cut_off)

    z_cut_off = traits.Float(1e+299, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cutoff frequency for each axis. The values are
        specified in the order X, Y, Z, Time. Units: Cycles per world
        unit (as defined by the data spacing).
        """
    )

    def _z_cut_off_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZCutOff,
                        self.z_cut_off)

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
    'GetSplitMode'), ('cut_off', 'GetCutOff'), ('x_cut_off',
    'GetXCutOff'), ('y_cut_off', 'GetYCutOff'), ('z_cut_off',
    'GetZCutOff'), ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'),
    ('enable_smp', 'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'split_mode', 'cut_off',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'minimum_piece_size', 'number_of_threads', 'progress_text',
    'x_cut_off', 'y_cut_off', 'z_cut_off'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageIdealLowPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageIdealLowPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['split_mode'], ['cut_off', 'desired_bytes_per_piece',
            'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'x_cut_off', 'y_cut_off', 'z_cut_off']),
            title='Edit ImageIdealLowPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageIdealLowPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

