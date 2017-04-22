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

from tvtk.tvtk_classes.object import Object


class AbstractImageInterpolator(Object):
    """
    AbstractImageInterpolator - interpolate data values from images
    
    Superclass: Object
    
    AbstractImageInterpolator provides an abstract interface for
    interpolating image data.  You specify the data set you want to
    interpolate values from, then call Interpolate(x,y,z) to interpolate
    the data.@par Thanks: Thanks to David Gobbi at the Seaman Family MR
    Centre and Dept. of Clinical Neurosciences, Foothills Medical Centre,
    Calgary, for providing this class.
    @sa
    ImageReslice ImageInterpolator ImageSincInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractImageInterpolator, obj, update, **traits)
    
    border_mode = traits.Trait('clamp',
    tvtk_base.TraitRevPrefixMap({'clamp': 0, 'mirror': 2, 'repeat': 1}), help=\
        """
        The border mode (default: clamp).  This controls how
        out-of-bounds lookups are handled, i.e. how data will be
        extrapolated beyond the bounds of the image.  The default is to
        clamp the lookup point to the bounds.  The other modes wrap
        around to the opposite boundary, or mirror the image at the
        boundary.
        """
    )

    def _border_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorderMode,
                        self.border_mode_)

    component_count = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        This method specifies the number of components to extract.  The
        default value is -1, which extracts all available components. 
        When the interpolation is performed, this will be clamped to the
        number of available components.
        """
    )

    def _component_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentCount,
                        self.component_count)

    component_offset = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        This method specifies which component of the input will be
        interpolated, or if component_count is also set, it specifies the
        first component. When the interpolation is performed, it will be
        clamped to the number of available components.
        """
    )

    def _component_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponentOffset,
                        self.component_offset)

    out_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The value to return when the point is out of bounds.
        """
    )

    def _out_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutValue,
                        self.out_value)

    tolerance = traits.Float(7.62939453125e-06, enter_set=True, auto_set=False, help=\
        """
        The tolerance to apply when checking whether a point is out of
        bounds. This is a fractional distance relative to the voxel size,
        so a tolerance of 1 expands the bounds by one voxel.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    def _get_extent(self):
        return self._vtk_obj.GetExtent()
    extent = traits.Property(_get_extent, help=\
        """
        
        """
    )

    def _get_number_of_components(self):
        return self._vtk_obj.GetNumberOfComponents()
    number_of_components = traits.Property(_get_number_of_components, help=\
        """
        Get the number of components that will be returned when
        Interpolate() is called.  This is only valid after
        initialization.  Before then, use compute_number_of_components
        instead.
        """
    )

    def _get_origin(self):
        return self._vtk_obj.GetOrigin()
    origin = traits.Property(_get_origin, help=\
        """
        
        """
    )

    def _get_spacing(self):
        return self._vtk_obj.GetSpacing()
    spacing = traits.Property(_get_spacing, help=\
        """
        
        """
    )

    def _get_whole_extent(self):
        return self._vtk_obj.GetWholeExtent()
    whole_extent = traits.Property(_get_whole_extent, help=\
        """
        Get the whole extent of the data being interpolated, including
        parts of the data that are not currently in memory.
        """
    )

    def check_bounds_ijk(self, *args):
        """
        V.check_bounds_ijk((float, float, float)) -> bool
        C++: bool CheckBoundsIJK(const double x[3])
        Check an x,y,z point to see if it is within the bounds for the
        structured coords of the image.  This is meant to be called prior
        to interpolate_ijk.  The bounds that are checked against are the
        input image extent plus the tolerance.
        """
        ret = self._wrap_call(self._vtk_obj.CheckBoundsIJK, *args)
        return ret

    def compute_number_of_components(self, *args):
        """
        V.compute_number_of_components(int) -> int
        C++: int ComputeNumberOfComponents(int inputComponents)
        Compute the number of output components based on the
        component_offset, component_count, and the number of components in
        the input data.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeNumberOfComponents, *args)
        return ret

    def compute_support_size(self, *args):
        """
        V.compute_support_size((float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float), [int, int, int])
        C++: virtual void ComputeSupportSize(const double matrix[16],
            int support[3])
        Get the support size for use in computing update extents.  If the
        data will be sampled on a regular grid, then pass a matrix
        describing the structured coordinate transformation between the
        output and the input. Otherwise, pass NULL as the matrix to
        retrieve the full kernel size.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeSupportSize, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(AbstractImageInterpolator)
        C++: void DeepCopy(AbstractImageInterpolator *obj)
        Copy the interpolator.  It is possible to duplicate an
        interpolator by calling new_instance() followed by deep_copy().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(DataObject)
        C++: virtual void Initialize(DataObject *data)
        Initialize the interpolator with the data that you wish to
        interpolate.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def interpolate(self, *args):
        """
        V.interpolate(float, float, float, int) -> float
        C++: double Interpolate(double x, double y, double z,
            int component)
        V.interpolate((float, float, float), [float, ...]) -> bool
        C++: bool Interpolate(const double point[3], double *value)
        Get the result of interpolating the specified component of the
        input data, which should be set to zero if there is only one
        component. If the point is not within the bounds of the data set,
        then out_value will be returned.  This method is primarily meant
        for use by the wrapper languages.
        """
        ret = self._wrap_call(self._vtk_obj.Interpolate, *args)
        return ret

    def interpolate_ijk(self, *args):
        """
        V.interpolate_ijk((float, float, float), [float, ...])
        C++: void InterpolateIJK(const double point[3], double *value)
        A version of Interpolate that takes structured coords instead of
        data coords.  Structured coords are the data coords after
        subtracting the Origin and dividing by the Spacing.
        """
        ret = self._wrap_call(self._vtk_obj.InterpolateIJK, *args)
        return ret

    def is_separable(self):
        """
        V.is_separable() -> bool
        C++: virtual bool IsSeparable()
        True if the interpolation is separable, which means that the
        weights can be precomputed in order to accelerate the
        interpolation.  Any interpolator which is separable will
        implement the methods precompute_weights_for_extent and
        interpolate_row
        """
        ret = self._vtk_obj.IsSeparable()
        return ret
        

    def release_data(self):
        """
        V.release_data()
        C++: virtual void ReleaseData()
        Release any data stored by the interpolator.
        """
        ret = self._vtk_obj.ReleaseData()
        return ret
        

    def update(self):
        """
        V.update()
        C++: void Update()
        Update the interpolator.  If the interpolator has been modified
        by a Set method since Initialize() was called, you must call this
        method to update the interpolator before you can use it.
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('border_mode', 'GetBorderMode'),
    ('component_count', 'GetComponentCount'), ('component_offset',
    'GetComponentOffset'), ('out_value', 'GetOutValue'), ('tolerance',
    'GetTolerance'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'border_mode', 'component_count',
    'component_offset', 'out_value', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractImageInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractImageInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['border_mode'], ['component_count', 'component_offset',
            'out_value', 'tolerance']),
            title='Edit AbstractImageInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractImageInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

