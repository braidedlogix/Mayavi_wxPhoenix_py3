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


class ThreadedImageAlgorithm(ImageAlgorithm):
    """
    ThreadedImageAlgorithm - Generic filter that has one input..
    
    Superclass: ImageAlgorithm
    
    ThreadedImageAlgorithm is a filter superclass that hides much of
    the pipeline  complexity. It handles breaking the pipeline execution
    into smaller extents so that the ImageData limits are observed. It
    also provides support for multithreading. If you don't need any of
    this functionality, consider using SimpleImageToImageAlgorithm
    instead.
    @sa
    SimpleImageToImageAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThreadedImageAlgorithm, obj, update, **traits)
    
    split_mode = traits.Trait('slab',
    tvtk_base.TraitRevPrefixMap({'slab': 0, 'beam': 1, 'block': 2}), help=\
        """
        Set the method used to divide the volume into pieces. Slab mode
        splits the volume along the Z direction first, Beam mode splits
        evenly along the Z and Y directions, and Block mode splits evenly
        along all three directions. Most filters use Slab mode as the
        default.
        """
    )

    def _split_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplitMode,
                        self.split_mode_)

    desired_bytes_per_piece = traits.Int(65536, enter_set=True, auto_set=False, help=\
        """
        The desired bytes per piece when volume is split for execution.
        When SMP is enabled, this is used to subdivide the volume into
        pieces. Smaller pieces allow for better dynamic load balancing,
        but increase the total overhead. The default is 65536 bytes.
        """
    )

    def _desired_bytes_per_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDesiredBytesPerPiece,
                        self.desired_bytes_per_piece)

    enable_smp = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Enable/Disable SMP for threading.
        """
    )

    def _enable_smp_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableSMP,
                        self.enable_smp)

    global_default_enable_smp = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Global Disable SMP for all derived Imaging filters.
        """
    )

    def _global_default_enable_smp_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalDefaultEnableSMP,
                        self.global_default_enable_smp)

    minimum_piece_size = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(16, 1, 1), cols=3, help=\
        """
        
        """
    )

    def _minimum_piece_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumPieceSize,
                        self.minimum_piece_size)

    number_of_threads = traits.Trait(12, traits.Range(1, 64, enter_set=True, auto_set=False), help=\
        """
        Get/Set the number of threads to create when rendering. This is
        ignored if enable_smp is On.
        """
    )

    def _number_of_threads_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfThreads,
                        self.number_of_threads)

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

    def split_extent(self, *args):
        """
        V.split_extent([int, int, int, int, int, int], [int, int, int, int,
             int, int], int, int) -> int
        C++: virtual int SplitExtent(int splitExt[6], int startExt[6],
            int num, int total)
        Putting this here until I merge graphics and imaging streaming.
        """
        ret = self._wrap_call(self._vtk_obj.SplitExtent, *args)
        return ret

    def threaded_execute(self, *args):
        """
        V.threaded_execute(ImageData, ImageData, [int, int, int, int,
             int, int], int)
        C++: virtual void ThreadedExecute(ImageData *inData,
            ImageData *outData, int extent[6], int threadId)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ThreadedExecute, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'split_mode', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThreadedImageAlgorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ThreadedImageAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['split_mode'], ['desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads']),
            title='Edit ThreadedImageAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThreadedImageAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

