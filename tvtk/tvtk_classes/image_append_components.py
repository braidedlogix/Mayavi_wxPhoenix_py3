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


class ImageAppendComponents(ThreadedImageAlgorithm):
    """
    ImageAppendComponents - Collects components from two inputs into
    one output.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageAppendComponents takes the components from two inputs and
    merges them into one output. If Input1 has M components, and Input2
    has N components, the output will have M+N components with input1
    components coming first.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageAppendComponents, obj, update, **traits)
    
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
        C++: DataObject *GetInput(int num)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get one input to this filter. This method is only for support of
        old-style pipeline connections.  When writing new code you should
        use Algorithm::GetInputConnection(0, num).
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_number_of_inputs(self):
        return self._vtk_obj.GetNumberOfInputs()
    number_of_inputs = traits.Property(_get_number_of_inputs, help=\
        """
        Get the number of inputs to this filter. This method is only for
        support of old-style pipeline connections.  When writing new code
        you should use Algorithm::GetNumberOfInputConnections(0).
        """
    )

    def replace_nth_input_connection(self, *args):
        """
        V.replace_nth_input_connection(int, AlgorithmOutput)
        C++: virtual void ReplaceNthInputConnection(int idx,
            AlgorithmOutput *input)
        Replace one of the input connections with a new input.  You can
        only replace input connections that you previously created with
        add_input_connection() or, in the case of the first input, with
        set_input_connection().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReplaceNthInputConnection, *my_args)
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
            return super(ImageAppendComponents, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageAppendComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['split_mode'], ['desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads']),
            title='Edit ImageAppendComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageAppendComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

