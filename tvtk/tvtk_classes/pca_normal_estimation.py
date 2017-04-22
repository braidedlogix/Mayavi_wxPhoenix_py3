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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class PCANormalEstimation(PolyDataAlgorithm):
    """
    PCANormalEstimation - generate point normals using local tangent
    planes
    
    Superclass: PolyDataAlgorithm
    
    PCANormalEstimation generates point normals using PCA (principal
    component analysis).  Basically this estimates a local tangent plane
    around each sample point p by considering a small neighborhood of
    points around p, and fitting a plane to the neighborhood (via PCA). A
    good introductory reference is Hoppe's "Surface reconstruction from
    unorganized points."
    
    To use this filter, specify a neighborhood size. This may have to be
    set via experimentation. In addition, the user may optionally specify
    a point locator (instead of the default locator), which is used to
    accelerate searches around the sample point. Finally, the user should
    specify how to generate consistently-oriented normals. As computed by
    PCA, normals may point in arbitrary +/- orientation, which may not be
    consistent with neighboring normals. There are three methods to
    address normal consistency: 1) leave the normals as computed, 2)
    adjust the +/- sign of the normals so that the normals all point
    towards a specified point, and
    3) perform a traversal of the point cloud and flip neighboring
       normals so that they are mutually consistent.
    
    The output of this filter is the same as the input except that a
    normal per point is produced. (Note that these are unit normals.)
    While any PointSet type can be provided as input, the output is
    represented by an explicit representation of points via a
    PolyData. This output polydata will populate its instance of
    Points, but no cells will be defined (i.e., no Vertex or
    PolyVertex are contained in the output).
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    PCACurvatureEstimation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPCANormalEstimation, obj, update, **traits)
    
    flip_normals = tvtk_base.false_bool_trait(help=\
        """
        The normal orientation can be flipped by enabling this flag.
        """
    )

    def _flip_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipNormals,
                        self.flip_normals_)

    normal_orientation = traits.Trait('point',
    tvtk_base.TraitRevPrefixMap({'point': 1, 'as_computed': 0, 'graph_traversal': 3}), help=\
        """
        Configure how the filter addresses consistency in normal
        oreientation. When initially computed using PCA, a point normal
        may point in the + or - direction, which may not be consistent
        with neighboring points. To address this, various strategies have
        been used to create consistent normals. The simplest approach is
        to do nothing (_as_computed). Another simple approach is to flip
        the normal based on its direction with respect to a specified
        point (i.e., point normals will point towrads the specified
        point). Finally, a full traversal of points across the graph of
        neighboring, connected points produces the best results but is
        computationally expensive.
        """
    )

    def _normal_orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalOrientation,
                        self.normal_orientation_)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a point locator. By default a StaticPointLocator is
        used. The locator performs efficient searches to locate points
        around a sample point.
        """
    )

    orientation_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _orientation_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientationPoint,
                        self.orientation_point)

    sample_size = traits.Trait(25, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        For each sampled point, specify the number of the closest,
        surrounding points used to estimate the normal (the so called
        k-neighborhood). By default 25 points are used. Smaller numbers
        may speed performance at the cost of accuracy.
        """
    )

    def _sample_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleSize,
                        self.sample_size)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('flip_normals', 'GetFlipNormals'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('normal_orientation',
    'GetNormalOrientation'), ('orientation_point', 'GetOrientationPoint'),
    ('sample_size', 'GetSampleSize'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'flip_normals', 'global_warning_display',
    'release_data_flag', 'normal_orientation', 'orientation_point',
    'progress_text', 'sample_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PCANormalEstimation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PCANormalEstimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['flip_normals'], ['normal_orientation'], ['orientation_point',
            'sample_size']),
            title='Edit PCANormalEstimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PCANormalEstimation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

