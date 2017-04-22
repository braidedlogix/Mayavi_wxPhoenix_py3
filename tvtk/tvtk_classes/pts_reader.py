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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class PTSReader(PolyDataAlgorithm):
    """
    PTSReader - Read ASCII PTS Files.
    
    Superclass: PolyDataAlgorithm
    
    PTSReader reads either a text file of
     points. The first line is the number of points. Point information is
     either x y z intensity or x y z intensity r g b
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPTSReader, obj, update, **traits)
    
    create_cells = tvtk_base.true_bool_trait(help=\
        """
        Boolean value indicates whether or not to create cells for this
        dataset. Otherwise only points and scalars are created. Defaults
        to true.
        """
    )

    def _create_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCreateCells,
                        self.create_cells_)

    include_color_and_luminance = tvtk_base.true_bool_trait(help=\
        """
        Boolean value indicates when color values are present if
        luminance should be read in as well Defaults to true.
        """
    )

    def _include_color_and_luminance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncludeColorAndLuminance,
                        self.include_color_and_luminance_)

    limit_read_to_bounds = tvtk_base.false_bool_trait(help=\
        """
        Boolean value indicates whether or not to limit points read to a
        specified (_read_bounds) region.
        """
    )

    def _limit_read_to_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLimitReadToBounds,
                        self.limit_read_to_bounds_)

    limit_to_max_number_of_points = tvtk_base.false_bool_trait(help=\
        """
        Boolean value indicates whether or not to limit number of points
        read based on max_numbe_of_points.
        """
    )

    def _limit_to_max_number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLimitToMaxNumberOfPoints,
                        self.limit_to_max_number_of_points_)

    output_data_type_is_double = tvtk_base.false_bool_trait(help=\
        """
        The output type defaults to float, but can instead be double.
        """
    )

    def _output_data_type_is_double_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputDataTypeIsDouble,
                        self.output_data_type_is_double_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    max_number_of_points = traits.Trait(1000000, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        The maximum number of points to load if limit_to_max_number_of_points
        is on/true. Sets a temporary on_ratio.
        """
    )

    def _max_number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxNumberOfPoints,
                        self.max_number_of_points)

    read_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(1e+299, -1e+299, 1e+299, -1e+299, 1e+299, -1e+299), cols=3, help=\
        """
        
        """
    )

    def _read_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadBounds,
                        self.read_bounds)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('create_cells', 'GetCreateCells'), ('include_color_and_luminance',
    'GetIncludeColorAndLuminance'), ('limit_read_to_bounds',
    'GetLimitReadToBounds'), ('limit_to_max_number_of_points',
    'GetLimitToMaxNumberOfPoints'), ('output_data_type_is_double',
    'GetOutputDataTypeIsDouble'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('max_number_of_points', 'GetMaxNumberOfPoints'),
    ('read_bounds', 'GetReadBounds'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'create_cells', 'debug', 'global_warning_display',
    'include_color_and_luminance', 'limit_read_to_bounds',
    'limit_to_max_number_of_points', 'output_data_type_is_double',
    'release_data_flag', 'file_name', 'max_number_of_points',
    'progress_text', 'read_bounds'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PTSReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PTSReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['create_cells', 'include_color_and_luminance',
            'limit_read_to_bounds', 'limit_to_max_number_of_points',
            'output_data_type_is_double'], [], ['file_name',
            'max_number_of_points', 'read_bounds']),
            title='Edit PTSReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PTSReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

