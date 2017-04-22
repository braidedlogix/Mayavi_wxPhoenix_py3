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

from tvtk.tvtk_classes.labeled_data_mapper import LabeledDataMapper


class Dynamic2DLabelMapper(LabeledDataMapper):
    """
    Dynamic2DLabelMapper - draw text labels at 2d dataset points
    
    Superclass: LabeledDataMapper
    
    Dynamic2DLabelMapper is a mapper that renders text at dataset
    points such that the labels do not overlap. Various items can be
    labeled including point ids, scalars, vectors, normals, texture
    coordinates, tensors, and field data components. This mapper assumes
    that the points are located on the x-y plane and that the camera
    remains perpendicular to that plane with a y-up axis (this can be
    constrained using ImageInteractor). On the first render, the
    mapper computes the visiblility of all labels at all scales, and
    queries this information on successive renders. This causes the first
    render to be much slower. The visibility algorithm is a greedy
    approach based on the point id, so the label for a point will be
    drawn unless the label for a point with lower id overlaps it.
    
    @warning
    Use this filter in combination with SelectVisiblePoints if you
    want to label only points that are visible. If you want to label
    cells rather than points, use the filter CellCenters to generate
    points at the center of the cells. Also, you can use the class
    IdFilter to generate ids as scalars or field data, which can then
    be labeled.
    
    @sa
    LabeledDataMapper
    
    @par Thanks: This algorithm was developed in the paper Ken Been and
    Chee Yap. Dynamic Map Labeling. IEEE Transactions on Visualization
    and Computer Graphics, Vol. 12, No. 5, 2006. pp. 773-780.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDynamic2DLabelMapper, obj, update, **traits)
    
    reverse_priority = tvtk_base.false_bool_trait(help=\
        """
        Whether to reverse the priority order (i.e. low values have high
        priority). Default is off.
        """
    )

    def _reverse_priority_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReversePriority,
                        self.reverse_priority_)

    label_height_padding = traits.Float(50.0, enter_set=True, auto_set=False, help=\
        """
        Set the label height padding as a percentage. The percentage is a
        percentage of your label height. Default is 50%.
        """
    )

    def _label_height_padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelHeightPadding,
                        self.label_height_padding)

    label_width_padding = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set the label width padding as a percentage. The percentage is a
        percentage of your label ^height^ (yes, not a typo). Default is
        50%.
        """
    )

    def _label_width_padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelWidthPadding,
                        self.label_width_padding)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Use get_input_data_object() to get the input data object for
        composite datasets.
        """
    )

    def set_priority_array_name(self, *args):
        """
        V.set_priority_array_name(string)
        C++: void SetPriorityArrayName(const char *name)
        Set the points array name to use to give priority to labels.
        Defaults to "priority".
        """
        ret = self._wrap_call(self._vtk_obj.SetPriorityArrayName, *args)
        return ret

    _updateable_traits_ = \
    (('reverse_priority', 'GetReversePriority'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('label_mode', 'GetLabelMode'),
    ('label_height_padding', 'GetLabelHeightPadding'),
    ('label_width_padding', 'GetLabelWidthPadding'), ('coordinate_system',
    'GetCoordinateSystem'), ('field_data_array', 'GetFieldDataArray'),
    ('field_data_name', 'GetFieldDataName'), ('label_format',
    'GetLabelFormat'), ('labeled_component', 'GetLabeledComponent'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'reverse_priority', 'label_mode',
    'coordinate_system', 'field_data_array', 'field_data_name',
    'label_format', 'label_height_padding', 'label_width_padding',
    'labeled_component', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Dynamic2DLabelMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Dynamic2DLabelMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['reverse_priority'], ['label_mode'], ['coordinate_system',
            'field_data_array', 'field_data_name', 'label_format',
            'label_height_padding', 'label_width_padding', 'labeled_component']),
            title='Edit Dynamic2DLabelMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Dynamic2DLabelMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

