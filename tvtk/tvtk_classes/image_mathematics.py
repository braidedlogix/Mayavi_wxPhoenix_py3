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


class ImageMathematics(ThreadedImageAlgorithm):
    """
    ImageMathematics - Add, subtract, multiply, divide, invert, sin,
    cos, exp, log.
    
    Superclass: ThreadedImageAlgorithm
    
    ImageMathematics implements basic mathematic operations
    set_operation is used to select the filters behavior.  The filter can
    take two or one input.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMathematics, obj, update, **traits)
    
    divide_by_zero_to_c = tvtk_base.false_bool_trait(help=\
        """
        How to handle divide by zero. Default is 0.
        """
    )

    def _divide_by_zero_to_c_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivideByZeroToC,
                        self.divide_by_zero_to_c_)

    operation = traits.Trait('add',
    tvtk_base.TraitRevPrefixMap({'add': 0, 'atan': 14, 'atan2': 15, 'absolute_value': 9, 'add_constant': 17, 'complex_multiply': 19, 'conjugate': 18, 'cos': 6, 'divide': 3, 'exp': 7, 'invert': 4, 'log': 8, 'max': 13, 'min': 12, 'multiply': 2, 'multiply_by_k': 16, 'replace_c_by_k': 20, 'sin': 5, 'square': 10, 'square_root': 11, 'subtract': 1}), help=\
        """
        Set/Get the Operation to perform.
        """
    )

    def _operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperation,
                        self.operation_)

    constant_c = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        A constant used by some operations (typically additive). Default
        is 0.
        """
    )

    def _constant_c_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstantC,
                        self.constant_c)

    constant_k = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        A constant used by some operations (typically multiplicative).
        Default is 1.
        """
    )

    def _constant_k_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstantK,
                        self.constant_k)

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
        Set the two inputs to this filter. For some operations, the
        second input is not used.
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
    (('divide_by_zero_to_c', 'GetDivideByZeroToC'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('operation', 'GetOperation'),
    ('split_mode', 'GetSplitMode'), ('constant_c', 'GetConstantC'),
    ('constant_k', 'GetConstantK'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'divide_by_zero_to_c',
    'global_warning_display', 'release_data_flag', 'operation',
    'split_mode', 'constant_c', 'constant_k', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMathematics, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMathematics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['divide_by_zero_to_c'], ['operation', 'split_mode'],
            ['constant_c', 'constant_k', 'desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size',
            'number_of_threads']),
            title='Edit ImageMathematics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMathematics properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

