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

from tvtk.tvtk_classes.point_cloud_filter import PointCloudFilter


class ExtractHierarchicalBins(PointCloudFilter):
    """
    ExtractHierarchicalBins - manipulate the output of
    HierarchicalBinningFilter
    
    Superclass: PointCloudFilter
    
    ExtractHierarchicalBins enables users to extract data from the
    output of HierarchicalBinningFilter. Points at a particular level,
    or at a level and bin number, can be filtered to the output. To
    perform these operations, the output must contain points sorted into
    bins (the Points), with offsets pointing to the beginning of each
    bin (a FieldData array named "_bin_offsets").
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    FiltersPointsFilter RadiusOutlierRemoval
    StatisticalOutlierRemoval ThresholdPoints ImplicitFunction
    ExtractGeoemtry FitImplicitFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractHierarchicalBins, obj, update, **traits)
    
    bin = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Specify the bin number to extract. If a non-negative value, then
        the points from the bin number specified are extracted. If
        negative, then entire levels of points are extacted (assuming the
        Level is non-negative). Note that the bin tree is flattened, a
        particular bin number may refer to a bin on any level.
        """
    )

    def _bin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBin,
                        self.bin)

    def _get_binning_filter(self):
        return wrap_vtk(self._vtk_obj.GetBinningFilter())
    def _set_binning_filter(self, arg):
        old_val = self._get_binning_filter()
        self._wrap_call(self._vtk_obj.SetBinningFilter,
                        deref_vtk(arg))
        self.trait_property_changed('binning_filter', old_val, arg)
    binning_filter = traits.Property(_get_binning_filter, _set_binning_filter, help=\
        """
        Specify the HierarchicalBinningFilter to query for relavant
        information. Make sure that this filter has executed prior to the
        execution of this filter. (This is generally a safe bet if
        connected in a pipeline.)
        """
    )

    level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the level to extract. If non-negative, with a negative
        bin number, then all points at this level are extracted and sent
        to the output. If negative, then the points from the specified
        bin are sent to the output. If both the level and bin number are
        negative values, then the input is sent to the output. By default
        the 0th level is extracted.
        """
    )

    def _level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLevel,
                        self.level)

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
    (('generate_outliers', 'GetGenerateOutliers'), ('generate_vertices',
    'GetGenerateVertices'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('bin',
    'GetBin'), ('level', 'GetLevel'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_outliers', 'generate_vertices',
    'global_warning_display', 'release_data_flag', 'bin', 'level',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractHierarchicalBins, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractHierarchicalBins properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_outliers', 'generate_vertices'], [], ['bin',
            'level']),
            title='Edit ExtractHierarchicalBins properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractHierarchicalBins properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

