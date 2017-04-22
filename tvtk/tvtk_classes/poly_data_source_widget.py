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

from tvtk.tvtk_classes.three_d_widget import ThreeDWidget


class PolyDataSourceWidget(ThreeDWidget):
    """
    PolyDataSourceWidget - abstract poly_data_source-based 3d widget
    
    Superclass: ThreeDWidget
    
    This abstract class serves as parent to 3d widgets that have simple
    PolyDataSource instances defining their geometry.
    
    In addition to what is offered by the ThreeDWidget parent, this class
    makes it possible to manipulate the underlying polydatasource and to
    place_widget() according to that, instead of having to make use of
    set_input() or set_prop3d().
    
    Implementors of child classes HAVE to implement their
    place_widget(bounds) to check for the existence of Input and prop3d
    FIRST.  If these don't exist, place according to the underlying
    poly_data_source.  Child classes also have to imprement
    update_placement(), which updates the widget according to the geometry
    of the underlying poly_data_source.
    
    @sa
    ThreeDWidget LineWidget PlaneWidget SphereWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataSourceWidget, obj, update, **traits)
    
    def setup_observers(self):
        """Setup the observers for the object."""
        super(PolyDataSourceWidget, self).setup_observers()
        tvtk_base._object_cache.setup_observers(self._vtk_obj,
                                      'EndInteractionEvent',
                                      self.update_traits)
    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input dataset. This is not required, but if supplied,
        and no Prop3D is specified, it is used to initially position
        the widget.
        """
    )

    def _get_poly_data_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataAlgorithm())
    poly_data_algorithm = traits.Property(_get_poly_data_algorithm, help=\
        """
        Returns underlying PolyDataAlgorithm that determines geometry.
         This can be modified after which place_widget() or
        update_placement() can be called.  update_placement() will always
        update the planewidget according to the geometry of the
        underlying poly_data_algorithm.  place_widget() will only make use
        of this geometry if there is no Input and no prop3d set.
        """
    )

    def update_placement(self):
        """
        V.update_placement()
        C++: virtual void UpdatePlacement()
        If you've made changes to the underlying PolyDataSource AFTER
        your initial call to place_widget(), use this method to realise
        the changes in the widget.
        """
        ret = self._vtk_obj.UpdatePlacement()
        return ret
        

    _updateable_traits_ = \
    (('enabled', 'GetEnabled'), ('key_press_activation',
    'GetKeyPressActivation'), ('picking_managed', 'GetPickingManaged'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('handle_size', 'GetHandleSize'),
    ('place_factor', 'GetPlaceFactor'), ('key_press_activation_value',
    'GetKeyPressActivationValue'), ('priority', 'GetPriority'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'enabled', 'global_warning_display',
    'key_press_activation', 'picking_managed', 'handle_size',
    'key_press_activation_value', 'place_factor', 'priority'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataSourceWidget, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataSourceWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enabled', 'key_press_activation', 'picking_managed'], [],
            ['handle_size', 'key_press_activation_value', 'place_factor',
            'priority']),
            title='Edit PolyDataSourceWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataSourceWidget properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

