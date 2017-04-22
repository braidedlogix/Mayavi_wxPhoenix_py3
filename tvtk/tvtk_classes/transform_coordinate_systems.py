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

from tvtk.tvtk_classes.point_set_algorithm import PointSetAlgorithm


class TransformCoordinateSystems(PointSetAlgorithm):
    """
    TransformCoordinateSystems - transform points into different
    coordinate systems
    
    Superclass: PointSetAlgorithm
    
    This filter transforms points from one coordinate system to another.
    The user must specify the coordinate systems in which the input and
    output are specified. The user must also specify the VTK viewport
    (i.e., renderer) in which the transformation occurs.
    
    @sa
    Coordinate TransformFilter TransformPolyData
    PolyDataMapper2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransformCoordinateSystems, obj, update, **traits)
    
    input_coordinate_system = traits.Trait('world',
    tvtk_base.TraitRevPrefixMap({'world': 5, 'display': 0, 'viewport': 2}), help=\
        """
        Set/get the coordinate system in which the input is specified.
        The current options are World, Viewport, and Display. By default
        the input coordinate system is World.
        """
    )

    def _input_coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputCoordinateSystem,
                        self.input_coordinate_system_)

    output_coordinate_system = traits.Trait('display',
    tvtk_base.TraitRevPrefixMap({'display': 0, 'viewport': 2, 'world': 5}), help=\
        """
        Set/get the coordinate system to which to transform the output.
        The current options are World, Viewport, and Display. By default
        the output coordinate system is Display.
        """
    )

    def _output_coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputCoordinateSystem,
                        self.output_coordinate_system_)

    def _get_viewport(self):
        return wrap_vtk(self._vtk_obj.GetViewport())
    def _set_viewport(self, arg):
        old_val = self._get_viewport()
        self._wrap_call(self._vtk_obj.SetViewport,
                        deref_vtk(arg))
        self.trait_property_changed('viewport', old_val, arg)
    viewport = traits.Property(_get_viewport, _set_viewport, help=\
        """
        In order for a successful coordinate transformation to occur, an
        instance of Viewport (e.g., a VTK renderer) must be specified.
        NOTE: this is a raw pointer, not a weak pointer nor a reference
        counted object, to avoid reference cycle loop between rendering
        classes and filter classes.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('input_coordinate_system', 'GetInputCoordinateSystem'),
    ('output_coordinate_system', 'GetOutputCoordinateSystem'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'input_coordinate_system',
    'output_coordinate_system', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TransformCoordinateSystems, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TransformCoordinateSystems properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['input_coordinate_system', 'output_coordinate_system'],
            []),
            title='Edit TransformCoordinateSystems properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TransformCoordinateSystems properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

