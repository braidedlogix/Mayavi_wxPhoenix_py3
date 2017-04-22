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

from tvtk.tvtk_classes.hyper_octree_algorithm import HyperOctreeAlgorithm


class HyperOctreeFractalSource(HyperOctreeAlgorithm):
    """
    HyperOctreeFractalSource - Create an octree from a fractal.
    
    Superclass: HyperOctreeAlgorithm
    
    hyperoctree
    
    @sa
    HyperOctreeSampleFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperOctreeFractalSource, obj, update, **traits)
    
    dimension = traits.Trait(3, traits.Range(2, 3, enter_set=True, auto_set=False), help=\
        """
        Create a 2d or 3d fractal.
        """
    )

    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    maximum_level = traits.Int(5, enter_set=True, auto_set=False, help=\
        """
        Set the maximum number of levels of the hyperoctree. If
        get_min_levels()>=levels, get_min_levels() is changed to levels-1.
        \pre positive_levels: levels>=1
        \post is_set: this->_get_levels()==levels
        \post min_is_valid: this->_get_min_levels()<this->_get_levels()
        """
    )

    def _maximum_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLevel,
                        self.maximum_level)

    maximum_number_of_iterations = traits.Trait(100, traits.Range(1, 255, enter_set=True, auto_set=False), help=\
        """
        The maximum number of cycles run to see if the value goes over 2
        """
    )

    def _maximum_number_of_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfIterations,
                        self.maximum_number_of_iterations)

    minimum_level = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Return the minimal number of levels of systematic subdivision.
        \post positive_result: result>=0
        """
    )

    def _minimum_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumLevel,
                        self.minimum_level)

    origin_cx = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(-1.75, -1.25, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_cx_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginCX,
                        self.origin_cx)

    projection_axes = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 1, 2), cols=3, help=\
        """
        Set the projection from  the 4d space (4 parameters / 2 imaginary
        numbers) to the axes of the 3d Volume. 0=C_Real, 1=C_Imaginary,
        2=X_Real, 4=X_Imaginary
        """
    )

    def _projection_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionAxes,
                        self.projection_axes)

    size_cx = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(2.5, 2.5, 2.0, 1.5), cols=3, help=\
        """
        
        """
    )

    def _size_cx_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSizeCX,
                        self.size_cx)

    span_threshold = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Controls when a leaf gets subdivided.  If the corner values span
        a larger range than this value, the leaf is subdivided.  This
        defaults to 2.
        """
    )

    def _span_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpanThreshold,
                        self.span_threshold)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('dimension',
    'GetDimension'), ('maximum_level', 'GetMaximumLevel'),
    ('maximum_number_of_iterations', 'GetMaximumNumberOfIterations'),
    ('minimum_level', 'GetMinimumLevel'), ('origin_cx', 'GetOriginCX'),
    ('projection_axes', 'GetProjectionAxes'), ('size_cx', 'GetSizeCX'),
    ('span_threshold', 'GetSpanThreshold'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'dimension', 'maximum_level',
    'maximum_number_of_iterations', 'minimum_level', 'origin_cx',
    'progress_text', 'projection_axes', 'size_cx', 'span_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperOctreeFractalSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperOctreeFractalSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['dimension', 'maximum_level',
            'maximum_number_of_iterations', 'minimum_level', 'origin_cx',
            'projection_axes', 'size_cx', 'span_threshold']),
            title='Edit HyperOctreeFractalSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperOctreeFractalSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

