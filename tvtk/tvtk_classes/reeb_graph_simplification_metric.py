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


class ReebGraphSimplificationMetric(Object):
    """
    ReebGraphSimplificationMetric - abstract class for custom Reeb
    graph simplification metric design.
    
    Superclass: Object
    
    This class makes it possible to design customized simplification
    metric evaluation algorithms, enabling the user to control the
    definition of what should be considered as noise or signal in the
    topological filtering process.
    
    References: "Topological persistence and simplification", H.
    Edelsbrunner, D. Letscher, and A. Zomorodian, Discrete Computational
    Geometry, 28:511-533, 2002.
    
    "Extreme elevation on a 2-manifold", P.K. Agarwal, H. Edelsbrunner,
    J. Harer, and Y. Wang, ACM Symposium on Computational Geometry, pp.
    357-365, 2004.
    
    "Simplifying flexible isosurfaces using local geometric measures", H.
    Carr, J. Snoeyink, M van de Panne, IEEE Visualization, 497-504, 2004
    
    "Loop surgery for volumetric meshes: Reeb graphs reduced to contour
    trees", J. Tierny, A. Gyulassy, E. Simon, V. Pascucci, IEEE Trans. on
    Vis. and Comp. Graph. (Proc of IEEE VIS), 15:1177-1184, 2009.
    
    See graphics/_testing/_cxx/_test_reeb_graph.cxx for an example of concrete
    implemetnation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkReebGraphSimplificationMetric, obj, update, **traits)
    
    lower_bound = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set the lowest possible value for the custom metric space. This
        value can be set prior to launching the Reeb graph simplification
        and then used inside the compute_metric call to make sure the
        returned value of compute_metric call is indeed between 0 and 1.
        """
    )

    def _lower_bound_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLowerBound,
                        self.lower_bound)

    upper_bound = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the highest possible value for the custom metric space. This
        value can be set prior to launching the Reeb graph simplification
        and then used inside the compute_metric call to make sure the
        returned value of compute_metric call is indeed between 0 and 1.
        """
    )

    def _upper_bound_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpperBound,
                        self.upper_bound)

    def compute_metric(self, *args):
        """
        V.compute_metric(DataSet, DataArray, int, AbstractArray,
            int) -> float
        C++: virtual double ComputeMetric(DataSet *mesh,
            DataArray *field, IdType startCriticalPoint,
            AbstractArray *vertexList, IdType endCriticalPoint)
        Function to implement in your simplification metric algorithm.
        Given the input mesh and the Ids of the vertices living on the
        Reeb graph arc to consider for removal, you should return a value
        between 0 and 1 (the smallest the more likely the arc will be
        removed, depending on the user-defined simplification threshold).
        """
        my_args = deref_array(args, [('vtkDataSet', 'vtkDataArray', 'int', 'vtkAbstractArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.ComputeMetric, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('lower_bound', 'GetLowerBound'),
    ('upper_bound', 'GetUpperBound'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'lower_bound', 'upper_bound'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ReebGraphSimplificationMetric, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ReebGraphSimplificationMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['lower_bound', 'upper_bound']),
            title='Edit ReebGraphSimplificationMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ReebGraphSimplificationMetric properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

