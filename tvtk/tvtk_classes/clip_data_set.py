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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class ClipDataSet(UnstructuredGridAlgorithm):
    """
    ClipDataSet - clip any dataset with user-specified implicit
    function or input scalar data
    
    Superclass: UnstructuredGridAlgorithm
    
    ClipDataSet is a filter that clips any type of dataset using
    either any subclass of ImplicitFunction, or the input scalar data.
    Clipping means that it actually "cuts" through the cells of the
    dataset, returning everything inside of the specified implicit
    function (or greater than the scalar value) including "pieces" of a
    cell. (Compare this with ExtractGeometry, which pulls out entire,
    uncut cells.) The output of this filter is an unstructured grid.
    
    To use this filter, you must decide if you will be clipping with an
    implicit function, or whether you will be using the input scalar
    data.  If you want to clip with an implicit function, you must:
    1) define an implicit function
    2) set it with the set_clip_function method
    3) apply the generate_clip_scalars_on method If a clip_function is not
       specified, or generate_clip_scalars is off (the default), then the
       input's scalar data will be used to clip the polydata.
    
    You can also specify a scalar value, which is used to decide what is
    inside and outside of the implicit function. You can also reverse the
    sense of what inside/outside is by setting the inside_out instance
    variable. (The clipping algorithm proceeds by computing an implicit
    function value or using the input scalar data for each point in the
    dataset. This is compared to the scalar value to determine
    inside/outside.)
    
    This filter can be configured to compute a second output. The second
    output is the part of the cell that is clipped away. Set the
    generate_clipped_data boolean on if you wish to access this output
    data.
    
    @warning
    ClipDataSet will triangulate all types of 3d cells (i.e., create
    tetrahedra). This is true even if the cell is not actually cut. This
    is necessary to preserve compatibility across face neighbors. 2d
    cells will only be triangulated if the cutting function passes
    through them.
    
    @sa
    ImplicitFunction Cutter ClipVolume ClipPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkClipDataSet, obj, update, **traits)
    
    generate_clip_scalars = tvtk_base.false_bool_trait(help=\
        """
        If this flag is enabled, then the output scalar values will be
        interpolated from the implicit function values, and not the input
        scalar data. If you enable this flag but do not provide an
        implicit function an error will be reported.
        """
    )

    def _generate_clip_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateClipScalars,
                        self.generate_clip_scalars_)

    generate_clipped_output = tvtk_base.false_bool_trait(help=\
        """
        Control whether a second output is generated. The second output
        contains the polygonal data that's been clipped away.
        """
    )

    def _generate_clipped_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateClippedOutput,
                        self.generate_clipped_output_)

    inside_out = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the inside_out flag. When off, a vertex is considered
        inside the implicit function if its value is greater than the
        Value ivar. When inside_outside is turned on, a vertex is
        considered inside the implicit function if its implicit function
        value is less than or equal to the Value ivar.  inside_out is off
        by default.
        """
    )

    def _inside_out_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInsideOut,
                        self.inside_out_)

    use_value_as_offset = tvtk_base.true_bool_trait(help=\
        """
        If use_value_as_offset is true, Value is used as an offset parameter
        to the implicit function. Otherwise, Value is used only when
        clipping using a scalar array. Default is true.
        """
    )

    def _use_value_as_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseValueAsOffset,
                        self.use_value_as_offset_)

    def _get_clip_function(self):
        return wrap_vtk(self._vtk_obj.GetClipFunction())
    def _set_clip_function(self, arg):
        old_val = self._get_clip_function()
        self._wrap_call(self._vtk_obj.SetClipFunction,
                        deref_vtk(arg))
        self.trait_property_changed('clip_function', old_val, arg)
    clip_function = traits.Property(_get_clip_function, _set_clip_function, help=\
        """
        Specify the implicit function with which to perform the clipping.
        If you do not define an implicit function, then the selected
        input scalar data will be used for clipping.
        """
    )

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a spatial locator for merging points. By default, an
        instance of MergePoints is used.
        """
    )

    merge_tolerance = traits.Trait(0.01, traits.Range(0.0001, 0.25, enter_set=True, auto_set=False), help=\
        """
        Set the tolerance for merging clip intersection points that are
        near the vertices of cells. This tolerance is used to prevent the
        generation of degenerate primitives. Note that only 3d cells
        actually use this instance variable.
        """
    )

    def _merge_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMergeTolerance,
                        self.merge_tolerance)

    output_points_precision = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the clipping value of the implicit function (if clipping with
        implicit function) or scalar value (if clipping with scalars).
        The default value is 0.0. This value is ignored if
        use_value_as_offset is true and a clip function is defined.
        """
    )

    def _value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetValue,
                        self.value)

    def _get_clipped_output(self):
        return wrap_vtk(self._vtk_obj.GetClippedOutput())
    clipped_output = traits.Property(_get_clipped_output, help=\
        """
        Return the Clipped output.
        """
    )

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
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified. The locator is used to merge coincident points.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('generate_clip_scalars', 'GetGenerateClipScalars'),
    ('generate_clipped_output', 'GetGenerateClippedOutput'),
    ('inside_out', 'GetInsideOut'), ('use_value_as_offset',
    'GetUseValueAsOffset'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('merge_tolerance', 'GetMergeTolerance'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('value', 'GetValue'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_clip_scalars',
    'generate_clipped_output', 'global_warning_display', 'inside_out',
    'release_data_flag', 'use_value_as_offset', 'merge_tolerance',
    'output_points_precision', 'progress_text', 'value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ClipDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_clip_scalars', 'generate_clipped_output',
            'inside_out', 'use_value_as_offset'], [], ['merge_tolerance',
            'output_points_precision', 'value']),
            title='Edit ClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

