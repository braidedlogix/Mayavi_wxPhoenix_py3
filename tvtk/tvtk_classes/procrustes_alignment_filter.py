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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class ProcrustesAlignmentFilter(MultiBlockDataSetAlgorithm):
    """
    ProcrustesAlignmentFilter - aligns a set of pointsets together
    
    Superclass: MultiBlockDataSetAlgorithm
    
    ProcrustesAlignmentFilter is a filter that takes a set of
    pointsets (any object derived from PointSet) and aligns them in a
    least-squares sense to their mutual mean. The algorithm is iterated
    until convergence, as the mean must be recomputed after each
    alignment.
    
    ProcrustesAlignmentFilter requires a MultiBlock input
    consisting of PointSets as first level children.
    
    The default (in LandmarkTransform) is for a similarity alignment.
    For a rigid-body alignment (to build a 'size-and-shape' model) use:
    
    
       get_landmark_transform()->_set_mode_to_rigid_body().
    
    Affine alignments are not normally used but are left in for
    completeness:
    
    
       get_landmark_transform()->_set_mode_to_affine().
    
    ProcrustesAlignmentFilter is an implementation of:
    
    
       J.C. Gower (1975)
       Generalized Procrustes Analysis. Psychometrika, 40:33-51.
    
    @warning
    All of the input pointsets must have the same number of points.
    
    @par Thanks: Tim Hutton and Rasmus Paulsen who developed and
    contributed this class
    
    @sa
    LandmarkTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProcrustesAlignmentFilter, obj, update, **traits)
    
    start_from_centroid = tvtk_base.false_bool_trait(help=\
        """
        When on, the initial alignment is to the centroid of the cohort
        curves.  When off, the alignment is to the centroid of the first
        input.  Default is off for backward compatibility.
        """
    )

    def _start_from_centroid_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartFromCentroid,
                        self.start_from_centroid_)

    output_points_precision = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings. If the
        desired precision is DEFAULT_PRECISION and any of the inputs are
        double precision, then the mean points will be double precision.
        Otherwise, if the desired precision is DEFAULT_PRECISION and all
        the inputs are single precision, then the mean points will be
        single precision.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    def _get_landmark_transform(self):
        return wrap_vtk(self._vtk_obj.GetLandmarkTransform())
    landmark_transform = traits.Property(_get_landmark_transform, help=\
        """
        Get the internal landmark transform. Use it to constrain the
        number of degrees of freedom of the alignment (i.e. rigid body,
        similarity, etc.). The default is a similarity alignment.
        """
    )

    def _get_mean_points(self):
        return wrap_vtk(self._vtk_obj.GetMeanPoints())
    mean_points = traits.Property(_get_mean_points, help=\
        """
        Get the estimated mean point cloud
        """
    )

    _updateable_traits_ = \
    (('start_from_centroid', 'GetStartFromCentroid'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'start_from_centroid', 'output_points_precision',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProcrustesAlignmentFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProcrustesAlignmentFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['start_from_centroid'], [], ['output_points_precision']),
            title='Edit ProcrustesAlignmentFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProcrustesAlignmentFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

