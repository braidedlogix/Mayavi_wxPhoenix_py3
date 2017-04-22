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


class ImageRectilinearWipe(ThreadedImageAlgorithm):
    """
    ImageRectilinearWipe - make a rectilinear combination of two
    images.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageRectilinearWipe makes a rectilinear combination of two
    images. The two input images must correspond in size, scalar type and
    number of components. The resulting image has four possible
    configurations called:
      Quad - alternate input 0 and input 1 horizontally and
        vertically. Select this with set_wipe_mode_to_quad. The Position
        specifies the location of the quad intersection.
      Corner - 3 of one input and 1 of the other. Select the location of
        input 0 with with set_wipe_mode_to_lower_left,
    set_wipe_mode_to_lower_right,
        set_wipe_mode_to_upper_left and set_wipe_mode_to_upper_right. The Position
        selects the location of the corner.
      Horizontal - alternate input 0 and input 1 with a vertical
        split. Select this with set_wipe_mode_to_horizontal. Position[0]
        specifies the location of the vertical transition between input 0
        and input 1.
      Vertical - alternate input 0 and input 1 with a horizontal
        split. Only the y The intersection point of the rectilinear
    points
        is controlled with the Point ivar.
    
    @par Thanks: This work was supported by PHS Research Grant No. 1 P41
    RR13218-01 from the National Center for Research Resources.
    
    @sa
    ImageCheckerboard
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageRectilinearWipe, obj, update, **traits)
    
    wipe = traits.Trait('quad',
    tvtk_base.TraitRevPrefixMap({'quad': 0, 'horizontal': 1, 'lower_left': 3, 'lower_right': 4, 'upper_left': 5, 'upper_right': 6, 'vertical': 2}), help=\
        """
        Specify the wipe mode. This mode determnis how input 0 and input
        1 are combined to produce the output. Each mode uses one or both
        of the values stored in Position. set_wipe_to_quad - alternate input
        0 and input 1 horizontally and vertically. The Position specifies
        the location of the quad intersection.
        set_wipe_to_lower_left{_lower_right,_upper_left._upper_right} - 3 of one
        input and 1 of the other. Select the location of input 0 to the
        lower_left{_lower_right,_upper_left,_upper_right}. Position selects the
        location of the corner. set_wipe_to_horizontal - alternate input 0
        and input 1 with a vertical split. Position[0] specifies the
        location of the vertical transition between input 0 and input 1.
        set_wipe_to_vertical - alternate input 0 and input 1 with a
        horizontal split. Position[1] specifies the location of the
        horizonal transition between input 0 and input 1.
        """
    )

    def _wipe_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWipe,
                        self.wipe_)

    axis = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 1), cols=2, help=\
        """
        
        """
    )

    def _axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxis,
                        self.axis)

    position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(0, 0), cols=2, help=\
        """
        
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

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

    def set_input1data(self, *args):
        """
        V.set_input1data(DataObject)
        C++: virtual void SetInput1Data(DataObject *in)
        Set the two inputs to this filter.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput1Data, *my_args)
        return ret

    def set_input2data(self, *args):
        """
        V.set_input2data(DataObject)
        C++: virtual void SetInput2Data(DataObject *in)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInput2Data, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('wipe',
    'GetWipe'), ('split_mode', 'GetSplitMode'), ('axis', 'GetAxis'),
    ('position', 'GetPosition'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'split_mode', 'wipe', 'axis',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'minimum_piece_size', 'number_of_threads', 'position',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageRectilinearWipe, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageRectilinearWipe properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['split_mode', 'wipe'], ['axis', 'desired_bytes_per_piece',
            'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads', 'position']),
            title='Edit ImageRectilinearWipe properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageRectilinearWipe properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

