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


class ImageMapToColors(ThreadedImageAlgorithm):
    """
    ImageMapToColors - map the input image through a lookup table
    
    Superclass: ThreadedImageAlgorithm
    
    The ImageMapToColors filter will take an input image of any valid
    scalar type, and map the first component of the image through a
    lookup table.  The result is an image of type VTK_UNSIGNED_CHAR. If
    the lookup table is not set, or is set to NULL, then the input data
    will be passed through if it is already of type VTK_UNSIGNED_CHAR.
    
    @sa
    LookupTable ScalarsToColors
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMapToColors, obj, update, **traits)
    
    pass_alpha_to_output = tvtk_base.false_bool_trait(help=\
        """
        Use the alpha component of the input when computing the alpha
        component of the output (useful when converting monochrome+alpha
        data to RGBA)
        """
    )

    def _pass_alpha_to_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassAlphaToOutput,
                        self.pass_alpha_to_output_)

    output_format = traits.Trait('rgba',
    tvtk_base.TraitRevPrefixMap({'rgba': 4, 'luminance': 1, 'luminance_alpha': 2, 'rgb': 3}), help=\
        """
        Set the output format, the default is RGBA.
        """
    )

    def _output_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputFormat,
                        self.output_format_)

    active_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the component to map for multi-component images (default: 0)
        """
    )

    def _active_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveComponent,
                        self.active_component)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set the lookup table.
        """
    )

    na_n_color = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=int, value=(0, 0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _na_n_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNaNColor,
                        self.na_n_color)

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
    (('pass_alpha_to_output', 'GetPassAlphaToOutput'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_format', 'GetOutputFormat'),
    ('split_mode', 'GetSplitMode'), ('active_component',
    'GetActiveComponent'), ('na_n_color', 'GetNaNColor'),
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
    'pass_alpha_to_output', 'release_data_flag', 'output_format',
    'split_mode', 'active_component', 'desired_bytes_per_piece',
    'enable_smp', 'global_default_enable_smp', 'minimum_piece_size',
    'na_n_color', 'number_of_threads', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMapToColors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMapToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_alpha_to_output'], ['output_format', 'split_mode'],
            ['active_component', 'desired_bytes_per_piece', 'enable_smp',
            'global_default_enable_smp', 'minimum_piece_size', 'na_n_color',
            'number_of_threads']),
            title='Edit ImageMapToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMapToColors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

