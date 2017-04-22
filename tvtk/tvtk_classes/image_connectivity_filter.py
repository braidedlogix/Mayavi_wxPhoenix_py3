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


class ImageConnectivityFilter(ImageAlgorithm):
    """
    ImageConnectivityFilter - Label an image by connectivity
    
    Superclass: ImageAlgorithm
    
    ImageConnectivityFilter will identify connected regions within an
    image and label them.  Only points with scalar values within a
    prescribed range are considered for inclusion, by default this range
    includes all scalar values with a value greater than zero.  Points
    within the prescribed scalar range are considered to be connected if
    a path exists between the points that does not traverse any points
    that are not within the prescribed scalar range. Adjacency of points
    is governed by 4-connectivity for 2d images, and 6-connectivity for
    3d images.
    
    The output of this filter is a label image.  By default, each region
    is assigned a different label, where the labels are integer values
    starting at a value of 1.  The set_label_mode() method can be used to
    change the way that labels are assigned.  Labels can be assigned by
    providing input seed points for each region to be labelled, or they
    can be assigned by ranking the regions by size.
    
    If a set of seeds is provided with the set_seed_data() method, then the
    default behavior is to only output the regions that are connected to
    the seeds, and if the seeds have scalars, then these scalars will be
    used to label the regions.  Seeds with a scalar value equal to zero
    are ignored.  See the documentation for the set_extraction_mode()
    method for details on how to control which regions will labeled.
    
    Regions can be selected by size with the set_size_range() method, which
    can be useful for identifying objects of a certain size, e.g. for
    rejecting small regions that are likely to be noise. It is also
    possible to label only the largest region and ignore all others, with
    set_extraction_mode_to_largest_region().
    
    In addition to the labels, the following additional information is
    provided: the number of regions identified, the size of each region,
    a list of all label values used, and the seed for each region (if
    seeds were used).  Optionally, this filter can also compute the
    extent of each region if generate_region_extents_on() is called.  These
    extents can be useful for cropping the output of the filter.
    
    @sa
    ConnectivityFilter, PolyDataConnectivityFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageConnectivityFilter, obj, update, **traits)
    
    generate_region_extents = tvtk_base.false_bool_trait(help=\
        """
        Turn this on to request creation of the extracted_region_extents
        array.
        """
    )

    def _generate_region_extents_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateRegionExtents,
                        self.generate_region_extents_)

    extraction_mode = traits.Trait('seeded_regions',
    tvtk_base.TraitRevPrefixMap({'seeded_regions': 0, 'all_regions': 1, 'largest_region': 2}), help=\
        """
        Set which regions to output from this filter. This can be all the
        regions, just the seeded regions, or the largest region (which
        will the the largest seeded region, if there are seeds). The
        default is to output all the seeded regions, if there are seeds,
        or to output all the regions, if there are no seeds.
        """
    )

    def _extraction_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractionMode,
                        self.extraction_mode_)

    label_mode = traits.Trait('seed_scalar',
    tvtk_base.TraitRevPrefixMap({'seed_scalar': 0, 'constant_value': 1, 'size_rank': 2}), help=\
        """
        Set the mode for applying labels to the output. Labeling by
        seed_scalar uses the scalars from the seeds as labels, if present,
        or the regions will be labeled consecutively starting at 1, if
        the seeds have no scalars. Labeling by size_rank means that the
        largest region is labeled 1 and other regions are labeled
        consecutively in order of decreasing size (if there is a tie,
        then the seed point ID is used as a tiebreaker).  Finally,
        Constant means that all regions will have the value of
        set_label_constant_value().  The default is to label using the seed
        scalars, if present, or to label consecutively, if no seed
        scalars are present.
        """
    )

    def _label_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelMode,
                        self.label_mode_)

    label_scalar_type = traits.Trait('unsigned_char',
    tvtk_base.TraitRevPrefixMap({'unsigned_char': 3, 'int': 6, 'short': 4, 'unsigned_short': 5}), help=\
        """
        Set the scalar type for the output label image. This should be
        one of unsigned_char, Short, unsigned_short, or Int depending on
        how many labels are expected.  The default is unsigned_char, which
        allows for 255 label values.  If the total number of regions is
        greater than the maximum label value N, then only the largest N
        regions will be kept and the rest will be discarded.
        """
    )

    def _label_scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelScalarType,
                        self.label_scalar_type_)

    active_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        For multi-component input images, select which component to use.
        """
    )

    def _active_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActiveComponent,
                        self.active_component)

    label_constant_value = traits.Int(255, enter_set=True, auto_set=False, help=\
        """
        The label used when label_mode is constant_value. The default value
        is 255.
        """
    )

    def _label_constant_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelConstantValue,
                        self.label_constant_value)

    scalar_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.5, 1e+299), cols=2, help=\
        """
        
        """
    )

    def _scalar_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarRange,
                        self.scalar_range)

    def _get_seed_connection(self):
        return wrap_vtk(self._vtk_obj.GetSeedConnection())
    def _set_seed_connection(self, arg):
        old_val = self._get_seed_connection()
        self._wrap_call(self._vtk_obj.SetSeedConnection,
                        deref_vtk(arg))
        self.trait_property_changed('seed_connection', old_val, arg)
    seed_connection = traits.Property(_get_seed_connection, _set_seed_connection, help=\
        """
        The input for seed locations (input port 1). Each point in the
        supplied data set will be used as a seed, unless the data set has
        scalars, in which case only the points with scalar values that
        are not equal to zero will be used as seeds.
        """
    )

    size_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(1, 9223372036854775807), cols=2, help=\
        """
        
        """
    )

    def _size_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSizeRange,
                        self.size_range)

    def _get_stencil_connection(self):
        return wrap_vtk(self._vtk_obj.GetStencilConnection())
    def _set_stencil_connection(self, arg):
        old_val = self._get_stencil_connection()
        self._wrap_call(self._vtk_obj.SetStencilConnection,
                        deref_vtk(arg))
        self.trait_property_changed('stencil_connection', old_val, arg)
    stencil_connection = traits.Property(_get_stencil_connection, _set_stencil_connection, help=\
        """
        The input for a stencil (input port 2). The output labels will be
        restricted to the region inside the stencil, as if no input
        voxels existed outside the stencil.  This allows you to apply
        this filter within an arbitrary region of interest.
        """
    )

    def _get_extracted_region_extents(self):
        return wrap_vtk(self._vtk_obj.GetExtractedRegionExtents())
    extracted_region_extents = traits.Property(_get_extracted_region_extents, help=\
        """
        Get the extent (a 6-tuples) for each output region. This is only
        valid if generate_region_extents_on() was called before the filter
        was executed.
        """
    )

    def _get_extracted_region_labels(self):
        return wrap_vtk(self._vtk_obj.GetExtractedRegionLabels())
    extracted_region_labels = traits.Property(_get_extracted_region_labels, help=\
        """
        Get the label used for each extracted region.
        """
    )

    def _get_extracted_region_seed_ids(self):
        return wrap_vtk(self._vtk_obj.GetExtractedRegionSeedIds())
    extracted_region_seed_ids = traits.Property(_get_extracted_region_seed_ids, help=\
        """
        Get the point_id of the seed for each region. If no seed was used,
        the point_id will be -1.
        """
    )

    def _get_extracted_region_sizes(self):
        return wrap_vtk(self._vtk_obj.GetExtractedRegionSizes())
    extracted_region_sizes = traits.Property(_get_extracted_region_sizes, help=\
        """
        
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
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_number_of_extracted_regions(self):
        return self._vtk_obj.GetNumberOfExtractedRegions()
    number_of_extracted_regions = traits.Property(_get_number_of_extracted_regions, help=\
        """
        Get the number of extracted regions.
        """
    )

    def set_seed_data(self, *args):
        """
        V.set_seed_data(DataSet)
        C++: void SetSeedData(DataSet *data)
        The input for seed locations (input port 1). Each point in the
        supplied data set will be used as a seed, unless the data set has
        scalars, in which case only the points with scalar values that
        are not equal to zero will be used as seeds.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSeedData, *my_args)
        return ret

    def set_stencil_data(self, *args):
        """
        V.set_stencil_data(ImageStencilData)
        C++: void SetStencilData(ImageStencilData *data)
        The input for a stencil (input port 2). The output labels will be
        restricted to the region inside the stencil, as if no input
        voxels existed outside the stencil.  This allows you to apply
        this filter within an arbitrary region of interest.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetStencilData, *my_args)
        return ret

    _updateable_traits_ = \
    (('generate_region_extents', 'GetGenerateRegionExtents'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('extraction_mode', 'GetExtractionMode'), ('label_mode',
    'GetLabelMode'), ('label_scalar_type', 'GetLabelScalarType'),
    ('active_component', 'GetActiveComponent'), ('label_constant_value',
    'GetLabelConstantValue'), ('scalar_range', 'GetScalarRange'),
    ('size_range', 'GetSizeRange'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_region_extents',
    'global_warning_display', 'release_data_flag', 'extraction_mode',
    'label_mode', 'label_scalar_type', 'active_component',
    'label_constant_value', 'progress_text', 'scalar_range',
    'size_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageConnectivityFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_region_extents'], ['extraction_mode', 'label_mode',
            'label_scalar_type'], ['active_component', 'label_constant_value',
            'scalar_range', 'size_range']),
            title='Edit ImageConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageConnectivityFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

