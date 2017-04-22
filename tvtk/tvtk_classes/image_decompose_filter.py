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

from tvtk.tvtk_classes.image_iterate_filter import ImageIterateFilter


class ImageDecomposeFilter(ImageIterateFilter):
    """
    ImageDecomposeFilter - Filters that execute axes in series.
    
    Superclass: ImageIterateFilter
    
    This superclass molds the ImageIterateFilter superclass so it
    iterates over the axes.  The filter uses dimensionality to determine
    how many axes to execute (starting from x). The filter also provides
    convenience methods for permuting information retrieved from input,
    output and ImageData.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDecomposeFilter, obj, update, **traits)
    
    dimensionality = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Dimensionality is the number of axes which are considered during
        execution. To process images dimensionality would be set to 2.
        """
    )

    def _dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensionality,
                        self.dimensionality)

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

    def permute_extent(self, *args):
        """
        V.permute_extent([int, ...], int, int, int, int, int, int)
        C++: void PermuteExtent(int *extent, int &min0, int &max0,
            int &min1, int &max1, int &min2, int &max2)
        Private methods kept public for template execute functions.
        """
        ret = self._wrap_call(self._vtk_obj.PermuteExtent, *args)
        return ret

    def permute_increments(self, *args):
        """
        V.permute_increments([int, ...], int, int, int)
        C++: void PermuteIncrements(IdType *increments,
            IdType &inc0, IdType &inc1, IdType &inc2)
        Private methods kept public for template execute functions.
        """
        ret = self._wrap_call(self._vtk_obj.PermuteIncrements, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('split_mode',
    'GetSplitMode'), ('dimensionality', 'GetDimensionality'),
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
    'dimensionality', 'enable_smp', 'global_default_enable_smp',
    'minimum_piece_size', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDecomposeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDecomposeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['split_mode'], ['desired_bytes_per_piece',
            'dimensionality', 'enable_smp', 'global_default_enable_smp',
            'minimum_piece_size', 'number_of_threads']),
            title='Edit ImageDecomposeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDecomposeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

