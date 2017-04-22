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

from tvtk.tvtk_classes.encoded_gradient_estimator import EncodedGradientEstimator


class FiniteDifferenceGradientEstimator(EncodedGradientEstimator):
    """
    FiniteDifferenceGradientEstimator - Use finite differences to
    estimate gradient.
    
    Superclass: EncodedGradientEstimator
    
    FiniteDifferenceGradientEstimator is a concrete subclass of
     EncodedGradientEstimator that uses a central differences
    technique to
     estimate the gradient. The gradient at some sample location (x,y,z)
     would be estimated by:
    
    
          nx = (f(x-dx,y,z) - f(x+dx,y,z)) / 2*dx;
          ny = (f(x,y-dy,z) - f(x,y+dy,z)) / 2*dy;
          nz = (f(x,y,z-dz) - f(x,y,z+dz)) / 2*dz;
    
    
     This value is normalized to determine a unit direction vector and a
     magnitude. The normal is computed in voxel space, and
     dx = dy = dz = sample_spacing_in_voxels. A scaling factor is applied to
     convert this normal from voxel space to world coordinates.
    
    @sa
    EncodedGradientEstimator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFiniteDifferenceGradientEstimator, obj, update, **traits)
    
    sample_spacing_in_voxels = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the spacing between samples for the finite differences
        method used to compute the normal. This spacing is in voxel
        units.
        """
    )

    def _sample_spacing_in_voxels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleSpacingInVoxels,
                        self.sample_spacing_in_voxels)

    _updateable_traits_ = \
    (('bounds_clip', 'GetBoundsClip'), ('compute_gradient_magnitudes',
    'GetComputeGradientMagnitudes'), ('cylinder_clip', 'GetCylinderClip'),
    ('zero_pad', 'GetZeroPad'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('sample_spacing_in_voxels', 'GetSampleSpacingInVoxels'), ('bounds',
    'GetBounds'), ('gradient_magnitude_bias', 'GetGradientMagnitudeBias'),
    ('gradient_magnitude_scale', 'GetGradientMagnitudeScale'),
    ('number_of_threads', 'GetNumberOfThreads'), ('zero_normal_threshold',
    'GetZeroNormalThreshold'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['bounds_clip', 'compute_gradient_magnitudes', 'cylinder_clip',
    'debug', 'global_warning_display', 'zero_pad', 'bounds',
    'gradient_magnitude_bias', 'gradient_magnitude_scale',
    'number_of_threads', 'sample_spacing_in_voxels',
    'zero_normal_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FiniteDifferenceGradientEstimator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FiniteDifferenceGradientEstimator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['bounds_clip', 'compute_gradient_magnitudes', 'cylinder_clip',
            'zero_pad'], [], ['bounds', 'gradient_magnitude_bias',
            'gradient_magnitude_scale', 'number_of_threads',
            'sample_spacing_in_voxels', 'zero_normal_threshold']),
            title='Edit FiniteDifferenceGradientEstimator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FiniteDifferenceGradientEstimator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

