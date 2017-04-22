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


class BandedPolyDataContourFilter(PolyDataAlgorithm):
    """
    BandedPolyDataContourFilter - generate filled contours for
    PolyData
    
    Superclass: PolyDataAlgorithm
    
    BandedPolyDataContourFilter is a filter that takes as input
    PolyData and produces as output filled contours (also represented
    as PolyData). Filled contours are bands of cells that all have the
    same cell scalar value, and can therefore be colored the same. The
    method is also referred to as filled contour generation.
    
    To use this filter you must specify one or more contour values.  You
    can either use the method set_value() to specify each contour value,
    or use generate_values() to generate a series of evenly spaced
    contours.  Each contour value divides (or clips) the data into two
    pieces, values below the contour value, and values above it. The
    scalar values of each band correspond to the specified contour value.
     Note that if the first and last contour values are not the
    minimum/maximum contour range, then two extra contour values are
    added corresponding to the minimum and maximum range values. These
    extra contour bands can be prevented from being output by turning
    clipping on.
    
    @sa
    ClipDataSet ClipPolyData ClipVolume ContourFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBandedPolyDataContourFilter, obj, update, **traits)
    
    clipping = tvtk_base.false_bool_trait(help=\
        """
        Indicate whether to clip outside the range specified by the user.
        (The range is contour value[0] to contour value[num_contours-_1].)
        Clipping means all cells outside of the range specified are not
        sent to the output.
        """
    )

    def _clipping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClipping,
                        self.clipping_)

    generate_contour_edges = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off a flag to control whether contour edges are
        generated. Contour edges are the edges between bands. If enabled,
        they are generated from polygons/triangle strips and placed into
        the second output (the contour_edges_output).
        """
    )

    def _generate_contour_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateContourEdges,
                        self.generate_contour_edges_)

    scalar_mode = traits.Trait('index',
    tvtk_base.TraitRevPrefixMap({'index': 0, 'value': 1}), help=\
        """
        Control whether the cell scalars are output as an integer index
        or a scalar value. If an index, the index refers to the bands
        produced by the clipping range. If a value, then a scalar value
        which is a value between clip values is used.
        """
    )

    def _scalar_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarMode,
                        self.scalar_mode_)

    clip_tolerance = traits.Float(1.1920928955078125e-07, enter_set=True, auto_set=False, help=\
        """
        Set/Get the clip tolerance. Warning: setting this too large will
        certainly cause numerical issues. Change from the default value
        of FLT_EPSILON at your own risk. The actual internal clip
        tolerance is computed by multiplying clip_tolerance by the scalar
        range.
        """
    )

    def _clip_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClipTolerance,
                        self.clip_tolerance)

    component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the component to use of an input scalars array with more
        than one component. Default is 0.
        """
    )

    def _component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponent,
                        self.component)

    number_of_contours = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Methods to set / get contour values. A single value at a time can
        be set with set_value(). Multiple contour values can be set with
        generate_values(). Note that generate_values() generates n values
        inclusive of the start and end range values.
        """
    )

    def _number_of_contours_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfContours,
                        self.number_of_contours)

    def get_value(self, *args):
        """
        V.get_value(int) -> float
        C++: double GetValue(int i)
        Methods to set / get contour values. A single value at a time can
        be set with set_value(). Multiple contour values can be set with
        generate_values(). Note that generate_values() generates n values
        inclusive of the start and end range values.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, float)
        C++: void SetValue(int i, double value)
        Methods to set / get contour values. A single value at a time can
        be set with set_value(). Multiple contour values can be set with
        generate_values(). Note that generate_values() generates n values
        inclusive of the start and end range values.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

    def _get_contour_edges_output(self):
        return wrap_vtk(self._vtk_obj.GetContourEdgesOutput())
    contour_edges_output = traits.Property(_get_contour_edges_output, help=\
        """
        Get the second output which contains the edges dividing the
        contour bands. This output is empty unless generate_contour_edges
        is enabled.
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
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_values(self):
        return self._vtk_obj.GetValues()
    values = traits.Property(_get_values, help=\
        """
        Methods to set / get contour values. A single value at a time can
        be set with set_value(). Multiple contour values can be set with
        generate_values(). Note that generate_values() generates n values
        inclusive of the start and end range values.
        """
    )

    def generate_values(self, *args):
        """
        V.generate_values(int, [float, float])
        C++: void GenerateValues(int numContours, double range[2])
        V.generate_values(int, float, float)
        C++: void GenerateValues(int numContours, double rangeStart,
            double rangeEnd)
        Methods to set / get contour values. A single value at a time can
        be set with set_value(). Multiple contour values can be set with
        generate_values(). Note that generate_values() generates n values
        inclusive of the start and end range values.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateValues, *args)
        return ret

    _updateable_traits_ = \
    (('clipping', 'GetClipping'), ('generate_contour_edges',
    'GetGenerateContourEdges'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('scalar_mode',
    'GetScalarMode'), ('clip_tolerance', 'GetClipTolerance'),
    ('component', 'GetComponent'), ('number_of_contours',
    'GetNumberOfContours'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clipping', 'debug', 'generate_contour_edges',
    'global_warning_display', 'release_data_flag', 'scalar_mode',
    'clip_tolerance', 'component', 'number_of_contours', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BandedPolyDataContourFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BandedPolyDataContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clipping', 'generate_contour_edges'], ['scalar_mode'],
            ['clip_tolerance', 'component', 'number_of_contours']),
            title='Edit BandedPolyDataContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BandedPolyDataContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

