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

from tvtk.tvtk_classes.depth_image_processing_pass import DepthImageProcessingPass


class PointFillPass(DepthImageProcessingPass):
    """
    PointFillPass - Implement a post-processing fillpass
    
    Superclass: DepthImageProcessingPass
    
    This pass is designed to fill in rendering of sparse point
    sets/coulds The delegate is used once and is usually set to a
    CameraPass or to a post-processing pass.
    
    @sa
    RenderPass
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointFillPass, obj, update, **traits)
    
    candidate_point_ratio = traits.Float(0.9900000095367432, enter_set=True, auto_set=False, help=\
        """
        How far in front of a point must a neighboring point be to be
        used as a filler candidate.  Expressed as a multiple of the
        points distance from the camera. Defaults to 0.95
        """
    )

    def _candidate_point_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCandidatePointRatio,
                        self.candidate_point_ratio)

    minimum_candidate_angle = traits.Float(4.71238899230957, enter_set=True, auto_set=False, help=\
        """
        How large of an angle must the filler candidates span before a
        point will be filled. Expressed in radians. A value of pi will
        keep edges from growing out. Large values require more support,
        lower values less.
        """
    )

    def _minimum_candidate_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimumCandidateAngle,
                        self.minimum_candidate_angle)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('candidate_point_ratio',
    'GetCandidatePointRatio'), ('minimum_candidate_angle',
    'GetMinimumCandidateAngle'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'candidate_point_ratio',
    'minimum_candidate_angle'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointFillPass, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointFillPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['candidate_point_ratio', 'minimum_candidate_angle']),
            title='Edit PointFillPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointFillPass properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

