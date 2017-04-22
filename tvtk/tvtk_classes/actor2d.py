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

from tvtk.tvtk_classes.prop import Prop


class Actor2D(Prop):
    """
    Actor2D - a actor that draws 2d data
    
    Superclass: Prop
    
    Actor2D is similar to Actor, but it is made to be used with two
    dimensional images and annotation.  Actor2D has a position but
    does not use a transformation matrix like Actor (see the
    superclass Prop for information on positioning Actor2D). 
    Actor2D has a reference to a Mapper2D object which does the
    rendering.
    
    @sa
    Prop  Mapper2D Property2D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkActor2D, obj, update, **traits)
    
    height = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the height and width of the actor2d. The value is
        expressed as a fraction of the viewport. This really is just
        another way of setting the Position2 instance variable.
        """
    )

    def _height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeight,
                        self.height)

    layer_number = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the layer number in the overlay planes into which to
        render.
        """
    )

    def _layer_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLayerNumber,
                        self.layer_number)

    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    def _set_mapper(self, arg):
        old_val = self._get_mapper()
        self._wrap_call(self._vtk_obj.SetMapper,
                        deref_vtk(arg))
        self.trait_property_changed('mapper', old_val, arg)
    mapper = traits.Property(_get_mapper, _set_mapper, help=\
        """
        Set/Get the Mapper2D which defines the data to be drawn.
        """
    )

    position = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        Get the position_coordinate instance of Coordinate. This is
        used for for complicated or relative positioning. The position
        variable controls the lower left corner of the actor2d
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    position2 = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.5, 0.5), cols=2, help=\
        """
        Access the Position2 instance variable. This variable controls
        the upper right corner of the actor2d. It is by default relative
        to Position and in normalized viewport coordinates. Some 2d actor
        subclasses ignore the position2 variable
        """
    )

    def _position2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition2,
                        self.position2)

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Returns this actor's Property2D.  Creates a property if one
        doesn't already exist.
        """
    )

    width = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the height and width of the actor2d. The value is
        expressed as a fraction of the viewport. This really is just
        another way of setting the Position2 instance variable.
        """
    )

    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    def _get_actual_position2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetActualPosition2Coordinate())
    actual_position2_coordinate = traits.Property(_get_actual_position2_coordinate, help=\
        """
        Return the actual Coordinate reference that the mapper should
        use to position the actor. This is used internally by the mappers
        and should be overridden in specialized subclasses and otherwise
        ignored.
        """
    )

    def _get_actual_position_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetActualPositionCoordinate())
    actual_position_coordinate = traits.Property(_get_actual_position_coordinate, help=\
        """
        Return the actual Coordinate reference that the mapper should
        use to position the actor. This is used internally by the mappers
        and should be overridden in specialized subclasses and otherwise
        ignored.
        """
    )

    def _get_position2_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPosition2Coordinate())
    position2_coordinate = traits.Property(_get_position2_coordinate, help=\
        """
        Access the Position2 instance variable. This variable controls
        the upper right corner of the actor2d. It is by default relative
        to Position and in normalized viewport coordinates. Some 2d actor
        subclasses ignore the position2 variable
        """
    )

    def _get_position_coordinate(self):
        return wrap_vtk(self._vtk_obj.GetPositionCoordinate())
    position_coordinate = traits.Property(_get_position_coordinate, help=\
        """
        Get the position_coordinate instance of Coordinate. This is
        used for for complicated or relative positioning. The position
        variable controls the lower left corner of the actor2d
        """
    )

    def set_display_position(self, *args):
        """
        V.set_display_position(int, int)
        C++: void SetDisplayPosition(int, int)
        Set the prop2d's position in display coordinates.
        """
        ret = self._wrap_call(self._vtk_obj.SetDisplayPosition, *args)
        return ret

    _updateable_traits_ = \
    (('dragable', 'GetDragable'), ('pickable', 'GetPickable'),
    ('use_bounds', 'GetUseBounds'), ('visibility', 'GetVisibility'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('height', 'GetHeight'), ('layer_number',
    'GetLayerNumber'), ('position', 'GetPosition'), ('position2',
    'GetPosition2'), ('width', 'GetWidth'), ('estimated_render_time',
    'GetEstimatedRenderTime'), ('render_time_multiplier',
    'GetRenderTimeMultiplier'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'dragable', 'global_warning_display', 'pickable',
    'use_bounds', 'visibility', 'estimated_render_time', 'height',
    'layer_number', 'position', 'position2', 'render_time_multiplier',
    'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Actor2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Actor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['use_bounds', 'visibility'], [], ['estimated_render_time',
            'height', 'layer_number', 'position', 'position2',
            'render_time_multiplier', 'width']),
            title='Edit Actor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Actor2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

