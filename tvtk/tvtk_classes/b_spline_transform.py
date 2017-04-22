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

from tvtk.tvtk_classes.warp_transform import WarpTransform


class BSplineTransform(WarpTransform):
    """
    BSplineTransform - a cubic b-spline deformation transformation
    
    Superclass: WarpTransform
    
    BSplineTransform computes a cubic b-spline transformation from a
    grid of b-spline coefficients.
    @warning
    The inverse grid transform is calculated using an iterative method,
    and is several times more expensive than the forward transform.
    @sa
    GeneralTransform TransformToGrid
    ImageBSplineCoefficients@par Thanks: This class was written by
    David Gobbi at the Seaman Family MR Research Centre, Foothills
    Medical Centre, Calgary, Alberta. DG Gobbi and YP Starreveld, "Uniform B-Splines for the VTK Imaging
    Pipeline," VTK Journal, 2011, http://hdl.handle.net/10380/3252
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBSplineTransform, obj, update, **traits)
    
    border_mode = traits.Trait('edge',
    tvtk_base.TraitRevPrefixMap({'edge': 0, 'zero': 1, 'zero_at_border': 2}), help=\
        """
        Set/Get the border mode, to alter behavior at the edge of the
        grid. The Edge mode allows the displacement to converge to the
        edge coefficient past the boundary, which is similar to the
        behavior of the GridTransform. The Zero mode allows the
        displacement to smoothly converge to zero two node-spacings past
        the boundary, which is useful when you want to create a localized
        transform. The zero_at_border mode sacrifices smoothness to further
        localize the transform to just one node-spacing past the
        boundary.
        """
    )

    def _border_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorderMode,
                        self.border_mode_)

    def _get_coefficient_data(self):
        return wrap_vtk(self._vtk_obj.GetCoefficientData())
    def _set_coefficient_data(self, arg):
        old_val = self._get_coefficient_data()
        self._wrap_call(self._vtk_obj.SetCoefficientData,
                        deref_vtk(arg))
        self.trait_property_changed('coefficient_data', old_val, arg)
    coefficient_data = traits.Property(_get_coefficient_data, _set_coefficient_data, help=\
        """
        Set/Get the coefficient grid for the b-spline transform. The
        BSplineTransform class will never modify the data. Note that
        set_coefficient_data() does not setup a pipeline connection whereas
        set_coefficient_connection does.
        """
    )

    displacement_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get a scale to apply to the transformation.
        """
    )

    def _displacement_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementScale,
                        self.displacement_scale)

    def set_coefficient_connection(self, *args):
        """
        V.set_coefficient_connection(AlgorithmOutput)
        C++: virtual void SetCoefficientConnection(AlgorithmOutput *)
        Set/Get the coefficient grid for the b-spline transform. The
        BSplineTransform class will never modify the data. Note that
        set_coefficient_data() does not setup a pipeline connection whereas
        set_coefficient_connection does.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetCoefficientConnection, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('border_mode', 'GetBorderMode'),
    ('displacement_scale', 'GetDisplacementScale'), ('inverse_iterations',
    'GetInverseIterations'), ('inverse_tolerance', 'GetInverseTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'border_mode',
    'displacement_scale', 'inverse_iterations', 'inverse_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BSplineTransform, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BSplineTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['border_mode'], ['displacement_scale',
            'inverse_iterations', 'inverse_tolerance']),
            title='Edit BSplineTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BSplineTransform properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

