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

from tvtk.tvtk_classes.implicit_function import ImplicitFunction


class Superquadric(ImplicitFunction):
    """
    Superquadric - implicit function for a Superquadric
    
    Superclass: ImplicitFunction
    
    Superquadric computes the implicit function and function gradient
    for a superquadric. Superquadric is a concrete implementation of
    ImplicitFunction.  The superquadric is centered at Center and axes
    of rotation is along the y-axis. (Use the superclass'
    ImplicitFunction transformation matrix if necessary to
    reposition.) Roundness parameters (_phi_roundness and theta_roundness)
    control the shape of the superquadric.  The Toroidal boolean controls
    whether a toroidal superquadric is produced.  If so, the Thickness
    parameter controls the thickness of the toroid:  0 is the thinnest
    allowable toroid, and 1 has a minimum sized hole.  The Scale
    parameters allow the superquadric to be scaled in x, y, and z (normal
    vectors are correctly generated in any case).  The Size parameter
    controls size of the superquadric.
    
    This code is based on "Rigid physically based superquadrics", A. H.
    Barr, in "Graphics Gems III", David Kirk, ed., Academic Press, 1992.
    
    @warning
    The Size and Thickness parameters control coefficients of
    superquadric generation, and may do not exactly describe the size of
    the superquadric.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSuperquadric, obj, update, **traits)
    
    toroidal = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0).
        """
    )

    def _toroidal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetToroidal,
                        self.toroidal_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    phi_roundness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric north/south roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders.
        """
    )

    def _phi_roundness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhiRoundness,
                        self.phi_roundness)

    scale = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    size = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric isotropic size.
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    theta_roundness = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get Superquadric east/west roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders.
        """
    )

    def _theta_roundness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThetaRoundness,
                        self.theta_roundness)

    thickness = traits.Trait(0.3333, traits.Range(0.0001, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid.
        """
    )

    def _thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThickness,
                        self.thickness)

    _updateable_traits_ = \
    (('toroidal', 'GetToroidal'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('phi_roundness', 'GetPhiRoundness'), ('scale',
    'GetScale'), ('size', 'GetSize'), ('theta_roundness',
    'GetThetaRoundness'), ('thickness', 'GetThickness'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'toroidal', 'center',
    'phi_roundness', 'scale', 'size', 'theta_roundness', 'thickness'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Superquadric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Superquadric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['toroidal'], [], ['center', 'phi_roundness', 'scale', 'size',
            'theta_roundness', 'thickness']),
            title='Edit Superquadric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Superquadric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

