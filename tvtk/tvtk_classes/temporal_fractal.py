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

from tvtk.tvtk_classes.algorithm import Algorithm


class TemporalFractal(Algorithm):
    """
    TemporalFractal - A source to test AMR data object.
    
    Superclass: Algorithm
    
    TemporalFractal is a collection of uniform grids.  All have the
    same dimensions. Each block has a different origin and spacing.  It
    uses mandelbrot to create cell data. I scale the fractal array to
    look like a volme fraction. I may also add block id and level as
    extra cell arrays. This source produces a HierarchicalBoxDataSet
    when generate_rectilinear_grids is off, otherwise produces a
    MultiBlockDataSet.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTemporalFractal, obj, update, **traits)
    
    adaptive_subdivision = tvtk_base.true_bool_trait(help=\
        """
        Make the division adaptive or not, defaults to Adaptive
        """
    )

    def _adaptive_subdivision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAdaptiveSubdivision,
                        self.adaptive_subdivision_)

    discrete_time_steps = tvtk_base.false_bool_trait(help=\
        """
        Limit this source to discrete integer time steps Default is off
        (continuous)
        """
    )

    def _discrete_time_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiscreteTimeSteps,
                        self.discrete_time_steps_)

    generate_rectilinear_grids = tvtk_base.false_bool_trait(help=\
        """
        Generate either rectilinear grids either uniform grids. Default
        is false.
        """
    )

    def _generate_rectilinear_grids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateRectilinearGrids,
                        self.generate_rectilinear_grids_)

    ghost_levels = tvtk_base.false_bool_trait(help=\
        """
        For testing ghost levels.
        """
    )

    def _ghost_levels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGhostLevels,
                        self.ghost_levels_)

    two_dimensional = tvtk_base.true_bool_trait(help=\
        """
        Make a 2d data set to test.
        """
    )

    def _two_dimensional_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwoDimensional,
                        self.two_dimensional_)

    asymetric = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Test the case when the blocks do not have the same sizes. Adds 2
        to the x extent of the far x blocks (level 1).
        """
    )

    def _asymetric_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAsymetric,
                        self.asymetric)

    dimensions = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        XYZ dimensions of cells.
        """
    )

    def _dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensions,
                        self.dimensions)

    fractal_value = traits.Float(9.5, enter_set=True, auto_set=False, help=\
        """
        Essentially the iso surface value. The fractal array is scaled to
        map this value to 0.5 for use as a volume fraction.
        """
    )

    def _fractal_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFractalValue,
                        self.fractal_value)

    maximum_level = traits.Int(6, enter_set=True, auto_set=False, help=\
        """
        Any blocks touching a predefined line will be subdivided to this
        level. Other blocks are subdivided so that neighboring blocks
        only differ by one level.
        """
    )

    def _maximum_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLevel,
                        self.maximum_level)

    _updateable_traits_ = \
    (('adaptive_subdivision', 'GetAdaptiveSubdivision'),
    ('discrete_time_steps', 'GetDiscreteTimeSteps'),
    ('generate_rectilinear_grids', 'GetGenerateRectilinearGrids'),
    ('ghost_levels', 'GetGhostLevels'), ('two_dimensional',
    'GetTwoDimensional'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('asymetric',
    'GetAsymetric'), ('dimensions', 'GetDimensions'), ('fractal_value',
    'GetFractalValue'), ('maximum_level', 'GetMaximumLevel'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'adaptive_subdivision', 'debug',
    'discrete_time_steps', 'generate_rectilinear_grids', 'ghost_levels',
    'global_warning_display', 'release_data_flag', 'two_dimensional',
    'asymetric', 'dimensions', 'fractal_value', 'maximum_level',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TemporalFractal, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TemporalFractal properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['adaptive_subdivision', 'discrete_time_steps',
            'generate_rectilinear_grids', 'ghost_levels', 'two_dimensional'], [],
            ['asymetric', 'dimensions', 'fractal_value', 'maximum_level']),
            title='Edit TemporalFractal properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TemporalFractal properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

