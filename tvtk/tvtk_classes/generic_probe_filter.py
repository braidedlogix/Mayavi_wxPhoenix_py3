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


class GenericProbeFilter(DataSetAlgorithm):
    """
    GenericProbeFilter - sample data values at specified point
    locations
    
    Superclass: DataSetAlgorithm
    
    GenericProbeFilter is a filter that computes point attributes
    (e.g., scalars, vectors, etc.) at specified point positions. The
    filter has two inputs: the Input and Source. The Input geometric
    structure is passed through the filter. The point attributes are
    computed at the Input point positions by interpolating into the
    source data. For example, we can compute data values on a plane
    (plane specified as Input) from a volume (Source).
    
    This filter can be used to resample data, or convert one dataset form
    into another. For example, a generic dataset can be probed with a
    volume (three-dimensional ImageData), and then volume rendering
    techniques can be used to visualize the results. Another example: a
    line or curve can be used to probe data to produce x-y plots along
    that line or curve.
    
    This filter has been implemented to operate on generic datasets,
    rather than the typical DataSet (and subclasses).
    GenericDataSet is a more complex cousin of DataSet, typically
    consisting of nonlinear, higher-order cells. To process this type of
    data, generic cells are automatically tessellated into linear cells
    prior to isocontouring.
    
    @sa
    GenericProbeFilter ProbeFilter GenericDataSet
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenericProbeFilter, obj, update, **traits)
    
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    source = traits.Property(_get_source, help=\
        """
        Specify the point locations used to probe input. A generic
        dataset type is assumed.
        """
    )

    def _get_valid_points(self):
        return wrap_vtk(self._vtk_obj.GetValidPoints())
    valid_points = traits.Property(_get_valid_points, help=\
        """
        Get the list of point ids in the output that contain attribute
        data interpolated from the source.
        """
    )

    def set_source_data(self, *args):
        """
        V.set_source_data(GenericDataSet)
        C++: void SetSourceData(GenericDataSet *source)
        Specify the point locations used to probe input. A generic
        dataset type is assumed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenericProbeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GenericProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit GenericProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenericProbeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

