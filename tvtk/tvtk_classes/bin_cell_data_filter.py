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


class BinCellDataFilter(DataSetAlgorithm):
    """
    BinCellDataFilter - bin source cell data into input cells.
    
    Superclass: DataSetAlgorithm
    
    BinCellDataFilter takes a source mesh containing scalar cell data,
    an input mesh and a set of bin values and bins the source mesh's
    scalar cell data into the cells of the input mesh. The resulting
    output mesh is identical to the input mesh, with an additional cell
    data field, with tuple size equal to the number of bins + 1, that
    represents a histogram of the cell data values for all of the source
    cells whose centroid lie within the input cell.
    
    This filter is useful for analyzing the efficacy of an input mesh's
    ability to represent the cell data of the source mesh.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBinCellDataFilter, obj, update, **traits)
    
    compute_tolerance = tvtk_base.false_bool_trait(help=\
        """
        Set whether to use the Tolerance field or precompute the
        tolerance. When on, the tolerance will be computed and the field
        value is ignored. Off by default.
        """
    )

    def _compute_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeTolerance,
                        self.compute_tolerance_)

    spatial_match = tvtk_base.false_bool_trait(help=\
        """
        This flag is used only when a piece is requested to update.  By
        default the flag is off.  Because no spatial correspondence
        between input pieces and source pieces is known, all of the
        source has to be requested no matter what piece of the output is
        requested.  When there is a spatial correspondence, the
        user/application can set this flag.  This hint allows the breakup
        of the probe operation to be much more efficient.  When piece m
        of n is requested for update by the user, then only n of m needs
        to be requested of the source.
        """
    )

    def _spatial_match_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpatialMatch,
                        self.spatial_match_)

    store_number_of_nonzero_bins = tvtk_base.true_bool_trait(help=\
        """
        Set whether to store the number of nonzero bins for each cell. On
        by default.
        """
    )

    def _store_number_of_nonzero_bins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStoreNumberOfNonzeroBins,
                        self.store_number_of_nonzero_bins_)

    array_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get which component of the scalar array to bin; defaults to
        0.
        """
    )

    def _array_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayComponent,
                        self.array_component)

    def _get_cell_locator(self):
        return wrap_vtk(self._vtk_obj.GetCellLocator())
    def _set_cell_locator(self, arg):
        old_val = self._get_cell_locator()
        self._wrap_call(self._vtk_obj.SetCellLocator,
                        deref_vtk(arg))
        self.trait_property_changed('cell_locator', old_val, arg)
    cell_locator = traits.Property(_get_cell_locator, _set_cell_locator, help=\
        """
        Set/Get a spatial locator for speeding the search process. By
        default an instance of CellLocator is used.
        """
    )

    cell_overlap_method = traits.Trait(0, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Set whether cell overlap is determined by source cell centroid or
        by source cell points. Centroid by default.
        """
    )

    def _cell_overlap_method_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellOverlapMethod,
                        self.cell_overlap_method)

    number_of_bins = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Methods to set / get bin values.
        """
    )

    def _number_of_bins_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBins,
                        self.number_of_bins)

    number_of_nonzero_bins_array_name = traits.String('NumberOfNonzeroBins', enter_set=True, auto_set=False, help=\
        """
        Returns the name of the id array added to the output that holds
        the number of nonzero bins per cell. Set to "_number_of_nonzero_bins"
        by default.
        """
    )

    def _number_of_nonzero_bins_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfNonzeroBinsArrayName,
                        self.number_of_nonzero_bins_array_name)

    tolerance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the tolerance used to compute whether a cell centroid in the
        source is in a cell of the input.  This value is only used if
        compute_tolerance is off.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def get_value(self, *args):
        """
        V.get_value(int) -> float
        C++: double GetValue(int i)
        Methods to set / get bin values.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, float)
        C++: void SetValue(int i, double value)
        Methods to set / get bin values.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

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
        Specify the data set whose cells will be counted. The Input gives
        the geometry (the points and cells) for the output, while the
        Source is used to determine how many source cells lie within each
        input cell.
        """
    )

    def _get_values(self):
        return self._vtk_obj.GetValues()
    values = traits.Property(_get_values, help=\
        """
        Methods to set / get bin values.
        """
    )

    def generate_values(self, *args):
        """
        V.generate_values(int, [float, float])
        C++: void GenerateValues(int numBins, double range[2])
        V.generate_values(int, float, float)
        C++: void GenerateValues(int numBins, double rangeStart,
            double rangeEnd)
        Methods to set / get bin values.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateValues, *args)
        return ret

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the data set whose cells will be counted. The Input gives
        the geometry (the points and cells) for the output, while the
        Source is used to determine how many source cells lie within each
        input cell.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(DataObject)
        C++: void SetSourceData(DataObject *source)
        Specify the data set whose cells will be counted. The Input gives
        the geometry (the points and cells) for the output, while the
        Source is used to determine how many source cells lie within each
        input cell.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('compute_tolerance', 'GetComputeTolerance'), ('spatial_match',
    'GetSpatialMatch'), ('store_number_of_nonzero_bins',
    'GetStoreNumberOfNonzeroBins'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('array_component', 'GetArrayComponent'), ('cell_overlap_method',
    'GetCellOverlapMethod'), ('number_of_bins', 'GetNumberOfBins'),
    ('number_of_nonzero_bins_array_name',
    'GetNumberOfNonzeroBinsArrayName'), ('tolerance', 'GetTolerance'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_tolerance', 'debug',
    'global_warning_display', 'release_data_flag', 'spatial_match',
    'store_number_of_nonzero_bins', 'array_component',
    'cell_overlap_method', 'number_of_bins',
    'number_of_nonzero_bins_array_name', 'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BinCellDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BinCellDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_tolerance', 'spatial_match',
            'store_number_of_nonzero_bins'], [], ['array_component',
            'cell_overlap_method', 'number_of_bins',
            'number_of_nonzero_bins_array_name', 'tolerance']),
            title='Edit BinCellDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BinCellDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

