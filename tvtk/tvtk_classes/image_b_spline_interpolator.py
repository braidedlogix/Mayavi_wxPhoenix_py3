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

from tvtk.tvtk_classes.abstract_image_interpolator import AbstractImageInterpolator


class ImageBSplineInterpolator(AbstractImageInterpolator):
    """
    ImageBSplineInterpolator - perform b-spline interpolation on images
    
    Superclass: AbstractImageInterpolator
    
    ImageBSplineInterpolator can be used to perform b-spline
    interpolation on images that have been filtered with
    ImageBSplineCoefficients.  The b-spline interpolants provide the
    maximum possible degree of continuity for a given kernel size, but
    require that the image data be pre-filtered to generate b-spline
    coefficients before the interpolation is performed. Interpolating
    data that has not been pre-filtered will give incorrect results.
    @sa
    ImageReslice ImageBSplineCoefficients BSplineTransform@par
    Thanks: This class was written by David Gobbi at the Seaman Family MR
    Research Centre, Foothills Medical Centre, Calgary, Alberta. DG Gobbi
    and YP Starreveld, "Uniform B-Splines for the VTK Imaging Pipeline,"
    VTK Journal, 2011, http://hdl.handle.net/10380/3252
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageBSplineInterpolator, obj, update, **traits)
    
    spline_degree = traits.Trait(3, traits.Range(0, 9, enter_set=True, auto_set=False), help=\
        """
        Set the degree of the spline polynomial.  The default value is 3,
        and the maximum is 9.  The data must be pre-filtered for the same
        degree of polynomial with ImageBSplineCoefficients.
        """
    )

    def _spline_degree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplineDegree,
                        self.spline_degree)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('border_mode', 'GetBorderMode'),
    ('spline_degree', 'GetSplineDegree'), ('component_count',
    'GetComponentCount'), ('component_offset', 'GetComponentOffset'),
    ('out_value', 'GetOutValue'), ('tolerance', 'GetTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'border_mode', 'component_count',
    'component_offset', 'out_value', 'spline_degree', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageBSplineInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageBSplineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['border_mode'], ['component_count', 'component_offset',
            'out_value', 'spline_degree', 'tolerance']),
            title='Edit ImageBSplineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageBSplineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

