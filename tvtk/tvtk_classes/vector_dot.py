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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class VectorDot(DataSetAlgorithm):
    """
    VectorDot - generate scalars from dot product of vectors and
    normals (e.g., show displacement plot)
    
    Superclass: DataSetAlgorithm
    
    VectorDot is a filter to generate point scalar values from a
    dataset. The scalar value at a point is created by computing the dot
    product between the normal and vector at each point. Combined with
    the appropriate color map, this can show nodal lines/mode shapes of
    vibration, or a displacement plot.
    
    Note that by default the resulting scalars are mapped into a
    specified range. This requires an extra pass in the algorithm. This
    mapping pass can be disabled (set map_scalars to off).
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVectorDot, obj, update, **traits)
    
    map_scalars = tvtk_base.true_bool_trait(help=\
        """
        Enable/disable the mapping of scalars into a specified range.
        This will significantly improve the performance of the algorithm
        but the resulting scalar values will strictly be a function of
        the vector and normal data. By default, map_scalars is enabled,
        and the output scalar values will fall into the range
        scalar_range.
        """
    )

    def _map_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMapScalars,
                        self.map_scalars_)

    scalar_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(-1.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarRange,
                        self.scalar_range)

    def _get_actual_range(self):
        return self._vtk_obj.GetActualRange()
    actual_range = traits.Property(_get_actual_range, help=\
        """
        Return the actual range of the generated scalars (prior to
        mapping). Note that the data is valid only after the filter
        executes.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('map_scalars', 'GetMapScalars'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('scalar_range', 'GetScalarRange'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'map_scalars',
    'release_data_flag', 'progress_text', 'scalar_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VectorDot, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VectorDot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['map_scalars'], [], ['scalar_range']),
            title='Edit VectorDot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VectorDot properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

