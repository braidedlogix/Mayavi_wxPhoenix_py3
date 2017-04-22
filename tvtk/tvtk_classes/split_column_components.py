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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class SplitColumnComponents(TableAlgorithm):
    """
    SplitColumnComponents - split multicomponent table columns
    
    Superclass: TableAlgorithm
    
    Splits any columns in a table that have more than one component into
    individual columns. Single component columns are passed through
    without any data duplication. naming_mode can be used to control how
    columns with multiple components are labelled in the output, e.g., if
    column names "Points" had three components this column would be split
    into "Points (0)", "Points (1)", and Points (2)" when naming_mode is
    NUMBERS_WITH_PARENS, into Points_0, Points_1, and Points_2 when
    naming_mode is NUMBERS_WITH_UNDERSCORES, into "Points (X)", "Points
    (Y)", and "Points (Z)" when naming_mode is NAMES_WITH_PARENS, and into
    Points_X, Points_Y, and Points_Z when naming_mode is
    NAMES_WITH_UNDERSCORES.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSplitColumnComponents, obj, update, **traits)
    
    naming_mode = traits.Trait('number_with_parens',
    tvtk_base.TraitRevPrefixMap({'number_with_parens': 0, 'names_with_parens': 1, 'names_with_underscores': 3, 'number_with_underscores': 2}), help=\
        """
        Get/Set the array naming mode. Description is
        NUMBERS_WITH_PARENS.
        """
    )

    def _naming_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNamingMode,
                        self.naming_mode_)

    calculate_magnitudes = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        If on this filter will calculate an additional magnitude column
        for all columns it splits with two or more components. Default is
        on.
        """
    )

    def _calculate_magnitudes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCalculateMagnitudes,
                        self.calculate_magnitudes)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('naming_mode',
    'GetNamingMode'), ('calculate_magnitudes', 'GetCalculateMagnitudes'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'naming_mode', 'calculate_magnitudes',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SplitColumnComponents, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SplitColumnComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['naming_mode'], ['calculate_magnitudes']),
            title='Edit SplitColumnComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SplitColumnComponents properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

