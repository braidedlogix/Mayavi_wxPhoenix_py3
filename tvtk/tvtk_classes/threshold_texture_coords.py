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


class ThresholdTextureCoords(DataSetAlgorithm):
    """
    ThresholdTextureCoords - compute 1d, 2d, or 3d texture coordinates
    based on scalar threshold
    
    Superclass: DataSetAlgorithm
    
    ThresholdTextureCoords is a filter that generates texture
    coordinates for any input dataset type given a threshold criterion.
    The criterion can take three forms: 1) greater than a particular
    value (_threshold_by_upper());
    2) less than a particular value (_threshold_by_lower(); or 3) between
       two values (_threshold_between(). If the threshold criterion is
       satisfied, the "in" texture coordinate will be set (this can be
       specified by the user). If the threshold criterion is not
       satisfied the "out" is set.
    
    @warning
    There is a texture map - tex_thres.vtk - that can be used in
    conjunction with this filter. This map defines a "transparent" region
    for texture coordinates 0<=r<0.5, and an opaque full intensity map
    for texture coordinates 0.5<r<=1.0. There is a small transition
    region for r=0.5.
    
    @sa
    Threshold ThresholdPoints TextureMapToPlane
    TextureMapToSphere TextureMapToCylinder
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkThresholdTextureCoords, obj, update, **traits)
    
    in_texture_coord = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.75, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _in_texture_coord_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInTextureCoord,
                        self.in_texture_coord)

    out_texture_coord = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.25, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _out_texture_coord_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutTextureCoord,
                        self.out_texture_coord)

    texture_dimension = traits.Trait(2, traits.Range(1, 3, enter_set=True, auto_set=False), help=\
        """
        Set the desired dimension of the texture map.
        """
    )

    def _texture_dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureDimension,
                        self.texture_dimension)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_lower_threshold(self):
        return self._vtk_obj.GetLowerThreshold()
    lower_threshold = traits.Property(_get_lower_threshold, help=\
        """
        Return the upper and lower thresholds.
        """
    )

    def _get_upper_threshold(self):
        return self._vtk_obj.GetUpperThreshold()
    upper_threshold = traits.Property(_get_upper_threshold, help=\
        """
        Return the upper and lower thresholds.
        """
    )

    def threshold_between(self, *args):
        """
        V.threshold_between(float, float)
        C++: void ThresholdBetween(double lower, double upper)
        Criterion is cells whose scalars are between lower and upper
        thresholds.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdBetween, *args)
        return ret

    def threshold_by_lower(self, *args):
        """
        V.threshold_by_lower(float)
        C++: void ThresholdByLower(double lower)
        Criterion is cells whose scalars are less than lower threshold.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByLower, *args)
        return ret

    def threshold_by_upper(self, *args):
        """
        V.threshold_by_upper(float)
        C++: void ThresholdByUpper(double upper)
        Criterion is cells whose scalars are less than upper threshold.
        """
        ret = self._wrap_call(self._vtk_obj.ThresholdByUpper, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('in_texture_coord', 'GetInTextureCoord'), ('out_texture_coord',
    'GetOutTextureCoord'), ('texture_dimension', 'GetTextureDimension'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'in_texture_coord', 'out_texture_coord',
    'progress_text', 'texture_dimension'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ThresholdTextureCoords, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ThresholdTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['in_texture_coord', 'out_texture_coord',
            'texture_dimension']),
            title='Edit ThresholdTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ThresholdTextureCoords properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

