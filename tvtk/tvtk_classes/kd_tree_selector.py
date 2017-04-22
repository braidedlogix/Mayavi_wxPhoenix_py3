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

from tvtk.tvtk_classes.selection_algorithm import SelectionAlgorithm


class KdTreeSelector(SelectionAlgorithm):
    """
    KdTreeSelector - Selects point ids using a kd-tree.
    
    Superclass: SelectionAlgorithm
    
    If set_kd_tree is used, the filter ignores the input and selects based
    on that kd-tree.  If set_kd_tree is not used, the filter builds a
    kd-tree using the input point set and uses that tree for selection. 
    The output is a Selection containing the ids found in the kd-tree
    using the specified bounds.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkKdTreeSelector, obj, update, **traits)
    
    single_selection = tvtk_base.false_bool_trait(help=\
        """
        Whether to only allow up to one value in the result. The item
        selected is closest to the center of the bounds, if there are any
        points within the selection threshold. Default is off.
        """
    )

    def _single_selection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSingleSelection,
                        self.single_selection_)

    def _get_kd_tree(self):
        return wrap_vtk(self._vtk_obj.GetKdTree())
    def _set_kd_tree(self, arg):
        old_val = self._get_kd_tree()
        self._wrap_call(self._vtk_obj.SetKdTree,
                        deref_vtk(arg))
        self.trait_property_changed('kd_tree', old_val, arg)
    kd_tree = traits.Property(_get_kd_tree, _set_kd_tree, help=\
        """
        The kd-tree to use to find selected ids. The kd-tree must be
        initialized with the desired set of points. When this is set, the
        optional input is ignored.
        """
    )

    selection_attribute = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        The field attribute to use when generating the selection. If set,
        creates a PEDIGREEIDS or GLOBALIDS selection. If not set (or is
        set to -1), creates a INDICES selection. By default this is not
        set. NOTE: This should be set a constant in DataSetAttributes,
        not Selection.
        """
    )

    def _selection_attribute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionAttribute,
                        self.selection_attribute)

    selection_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, -1.0, 0.0, -1.0, -1e+299, 1e+299), cols=3, help=\
        """
        
        """
    )

    def _selection_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionBounds,
                        self.selection_bounds)

    selection_field_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The field name to use when generating the selection. If set,
        creates a VALUES selection. If not set (or is set to NULL),
        creates a INDICES selection. By default this is not set.
        """
    )

    def _selection_field_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionFieldName,
                        self.selection_field_name)

    single_selection_threshold = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The threshold for the single selection. A single point is added
        to the selection if it is within this threshold from the bounds
        center. Default is 1.
        """
    )

    def _single_selection_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSingleSelectionThreshold,
                        self.single_selection_threshold)

    _updateable_traits_ = \
    (('single_selection', 'GetSingleSelection'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('selection_attribute',
    'GetSelectionAttribute'), ('selection_bounds', 'GetSelectionBounds'),
    ('selection_field_name', 'GetSelectionFieldName'),
    ('single_selection_threshold', 'GetSingleSelectionThreshold'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'single_selection', 'progress_text',
    'selection_attribute', 'selection_bounds', 'selection_field_name',
    'single_selection_threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(KdTreeSelector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit KdTreeSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['single_selection'], [], ['selection_attribute',
            'selection_bounds', 'selection_field_name',
            'single_selection_threshold']),
            title='Edit KdTreeSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit KdTreeSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

