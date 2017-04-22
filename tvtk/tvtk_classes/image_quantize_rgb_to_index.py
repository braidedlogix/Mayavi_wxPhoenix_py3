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


class ImageQuantizeRGBToIndex(ImageAlgorithm):
    """
    ImageQuantizeRGBToIndex - generalized histograms up to 4 dimensions
    
    Superclass: ImageAlgorithm
    
    ImageQuantizeRGBToIndex takes a 3 component RGB image as input and
    produces a one component index image as output, along with a lookup
    table that contains the color definitions for the index values. This
    filter works on the entire input extent - it does not perform
    streaming, and it does not supported threaded execution (because it
    has to process the entire image).
    
    To use this filter, you typically set the number of colors (between 2
    and 65536), execute it, and then retrieve the lookup table. The
    colors can then be using the lookup table and the image index.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageQuantizeRGBToIndex, obj, update, **traits)
    
    build_tree_execute_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        For internal use only - set the times for execution
        """
    )

    def _build_tree_execute_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBuildTreeExecuteTime,
                        self.build_tree_execute_time)

    initialize_execute_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        For internal use only - set the times for execution
        """
    )

    def _initialize_execute_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitializeExecuteTime,
                        self.initialize_execute_time)

    lookup_index_execute_time = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        For internal use only - set the times for execution
        """
    )

    def _lookup_index_execute_time_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLookupIndexExecuteTime,
                        self.lookup_index_execute_time)

    number_of_colors = traits.Trait(256, traits.Range(2, 65536, enter_set=True, auto_set=False), help=\
        """
        Set / Get the number of color index values to produce - must be a
        number between 2 and 65536.
        """
    )

    def _number_of_colors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfColors,
                        self.number_of_colors)

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

    def _get_input_type(self):
        return self._vtk_obj.GetInputType()
    input_type = traits.Property(_get_input_type, help=\
        """
        For internal use only - get the type of the image
        """
    )

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    lookup_table = traits.Property(_get_lookup_table, help=\
        """
        Get the resulting lookup table that contains the color
        definitions corresponding to the index values in the output
        image.
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('build_tree_execute_time', 'GetBuildTreeExecuteTime'),
    ('initialize_execute_time', 'GetInitializeExecuteTime'),
    ('lookup_index_execute_time', 'GetLookupIndexExecuteTime'),
    ('number_of_colors', 'GetNumberOfColors'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'build_tree_execute_time',
    'initialize_execute_time', 'lookup_index_execute_time',
    'number_of_colors', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageQuantizeRGBToIndex, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageQuantizeRGBToIndex properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['build_tree_execute_time', 'initialize_execute_time',
            'lookup_index_execute_time', 'number_of_colors']),
            title='Edit ImageQuantizeRGBToIndex properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageQuantizeRGBToIndex properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

