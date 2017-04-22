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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class TimeSourceExample(UnstructuredGridAlgorithm):
    """
    TimeSourceExample - no description provided.
    
    Superclass: UnstructuredGridAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTimeSourceExample, obj, update, **traits)
    
    analytic = tvtk_base.false_bool_trait(help=\
        """
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
    )

    def _analytic_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAnalytic,
                        self.analytic_)

    growing = tvtk_base.false_bool_trait(help=\
        """
        When off (the default) this produces a single cell data set. When
        on the the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
        """
    )

    def _growing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGrowing,
                        self.growing_)

    x_amplitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        When 0.0 (the default) this produces a data set that is
        stationary. When on the data set moves in the X/Y plane over a
        sin wave over time, amplified by the value.
        """
    )

    def _x_amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAmplitude,
                        self.x_amplitude)

    y_amplitude = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        When 0.0 (the default) this produces a data set that is
        stationary. When on the data set moves in the X/Y plane over a
        sin wave over time, amplified by the value.
        """
    )

    def _y_amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAmplitude,
                        self.y_amplitude)

    def _get_analytic_max_value(self):
        return self._vtk_obj.GetAnalyticMaxValue()
    analytic_max_value = traits.Property(_get_analytic_max_value, help=\
        """
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
    )

    def _get_analytic_min_value(self):
        return self._vtk_obj.GetAnalyticMinValue()
    analytic_min_value = traits.Property(_get_analytic_min_value, help=\
        """
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
    )

    def _get_growing_max_value(self):
        return self._vtk_obj.GetGrowingMaxValue()
    growing_max_value = traits.Property(_get_growing_max_value, help=\
        """
        When off (the default) this produces a single cell data set. When
        on the the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
        """
    )

    def _get_growing_min_value(self):
        return self._vtk_obj.GetGrowingMinValue()
    growing_min_value = traits.Property(_get_growing_min_value, help=\
        """
        When off (the default) this produces a single cell data set. When
        on the the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('analytic', 'GetAnalytic'), ('growing', 'GetGrowing'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('x_amplitude',
    'GetXAmplitude'), ('y_amplitude', 'GetYAmplitude'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'analytic', 'debug', 'global_warning_display',
    'growing', 'release_data_flag', 'progress_text', 'x_amplitude',
    'y_amplitude'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TimeSourceExample, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TimeSourceExample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['analytic', 'growing'], [], ['x_amplitude', 'y_amplitude']),
            title='Edit TimeSourceExample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TimeSourceExample properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

