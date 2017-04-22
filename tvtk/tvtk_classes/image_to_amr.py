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

from tvtk.tvtk_classes.overlapping_amr_algorithm import OverlappingAMRAlgorithm


class ImageToAMR(OverlappingAMRAlgorithm):
    """
    ImageToAMR - filter to convert any ImageData to a
    OverlappingAMR.
    
    Superclass: OverlappingAMRAlgorithm
    
    ImageToAMR is a simple filter that converts any ImageData to a
    OverlappingAMR dataset. The input ImageData is treated as the
    highest refinement available for the highest level. The lower
    refinements and the number of blocks is controlled properties
    specified on the filter.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageToAMR, obj, update, **traits)
    
    maximum_number_of_blocks = traits.Trait(100, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the maximun number of blocks in the output
        """
    )

    def _maximum_number_of_blocks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfBlocks,
                        self.maximum_number_of_blocks)

    number_of_levels = traits.Trait(2, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the maximum number of levels in the generated
        Overlapping-AMR.
        """
    )

    def _number_of_levels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfLevels,
                        self.number_of_levels)

    refinement_ratio = traits.Trait(2, traits.Range(2, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the refinement ratio for levels. This refinement ratio is
        used for all levels.
        """
    )

    def _refinement_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRefinementRatio,
                        self.refinement_ratio)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_number_of_blocks', 'GetMaximumNumberOfBlocks'),
    ('number_of_levels', 'GetNumberOfLevels'), ('refinement_ratio',
    'GetRefinementRatio'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'maximum_number_of_blocks', 'number_of_levels',
    'progress_text', 'refinement_ratio'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageToAMR, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageToAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['maximum_number_of_blocks', 'number_of_levels',
            'refinement_ratio']),
            title='Edit ImageToAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageToAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

