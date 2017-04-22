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


class InterpolationKernel(Object):
    """
    InterpolationKernel - base class for interpolation kernels
    
    Superclass: Object
    
    InterpolationKernel specifies an abstract interface for
    interpolation kernels. An interpolation kernel is used to produce an
    interpolated data value at a point X from the points + data in a
    local neighborhood surounding X. For example, given the N nearest
    points surrounding X, the interpolation kernel provides N weights,
    which when combined with the N data values associated with these
    nearest points, produces an interpolated data value at point X.
    
    Note that various kernel initialization methods are provided. The
    basic method requires providing a point locator to accelerate
    neigborhood queries. Some kernels may refer back to the original
    dataset, or the point attribute data associated with the dataset. The
    initialization method enables different styles of initialization and
    is kernel-dependent.
    
    Typically the kernels are invoked in two parts: first, the basis is
    computed using the supplied point locator and dataset. This basis is
    a local footprint of point surrounding a poitn_x. In this footprint
    are the neighboring points used to compute the interpolation weights.
    Then, the weights are computed from points forming the basis.
    However, advanced users can develop their own basis, skipping the
    compute_basis() method, and then invoke compute_weights() directly.
    
    @warning
    The compute_basis() and compute_weights() methods must be thread safe
    as they are used in threaded algorithms.
    
    @sa
    PointInterpolator PointInterpolator2D GeneralizedKernel
    GaussianKernel SPHKernel ShepardKernel VoronoiKernel
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInterpolationKernel, obj, update, **traits)
    
    requires_initialization = tvtk_base.true_bool_trait(help=\
        """
        Indicate whether the kernel needs initialization. By default this
        data member is true, and using classes will invoke Initialize()
        on the kernel. However, if the user takes over initialization
        manually, then set requires_initialization to false (0).
        """
    )

    def _requires_initialization_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRequiresInitialization,
                        self.requires_initialization_)

    def compute_basis(self, *args):
        """
        V.compute_basis([float, float, float], IdList, int) -> int
        C++: virtual IdType ComputeBasis(double x[3], IdList *pIds,
            IdType ptId=0)
        Given a point x (and optional associated point id), determine the
        points around x which form an interpolation basis. The user must
        provide the IdList p_ids, which will be dynamically resized as
        necessary. The method returns the number of points in the basis.
        Typically this method is called before compute_weights(). Note
        that pt_id is optional in most cases, although in some kernels it
        is used to facilitate basis computation.
        """
        my_args = deref_array(args, [(['float', 'float', 'float'], 'vtkIdList', 'int')])
        ret = self._wrap_call(self._vtk_obj.ComputeBasis, *my_args)
        return ret

    def compute_weights(self, *args):
        """
        V.compute_weights([float, float, float], IdList, DoubleArray)
             -> int
        C++: virtual IdType ComputeWeights(double x[3],
            IdList *pIds, DoubleArray *weights)
        Given a point x, and a list of basis points p_ids, compute
        interpolation weights associated with these basis points.  Note
        that both the nearby basis points list p_ids and the weights array
        are provided by the caller of the method, and may be dynamically
        resized as necessary. The method returns the number of weights
        (p_ids may be resized in some cases). Typically this method is
        called after compute_basis(), although advanced users can invoke
        compute_weights() and provide the interpolation basis points p_ids
        directly.
        """
        my_args = deref_array(args, [(['float', 'float', 'float'], 'vtkIdList', 'vtkDoubleArray')])
        ret = self._wrap_call(self._vtk_obj.ComputeWeights, *my_args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(AbstractPointLocator, DataSet, PointData)
        C++: virtual void Initialize(AbstractPointLocator *loc,
            DataSet *ds, PointData *pd)
        Initialize the kernel. Pass information into the kernel that is
        necessary to subsequently perform evaluation. The locator refers
        to the points that are to be interpolated from; these points (ds)
        and the associated point data (pd) are provided as well. Note
        that some kernels may require manual setup / initialization, in
        which case set requires_initialization to false, do not call
        Initialize(), and of course manually initialize the kernel.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    _updateable_traits_ = \
    (('requires_initialization', 'GetRequiresInitialization'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'requires_initialization'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InterpolationKernel, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InterpolationKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['requires_initialization'], [], []),
            title='Edit InterpolationKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InterpolationKernel properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

