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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class AssignCoordinates(PassInputTypeAlgorithm):
    """
    AssignCoordinates - Given two(or three) arrays take the values in
    those arrays and simply assign them to the coordinates of the
    vertices.
    
    Superclass: PassInputTypeAlgorithm
    
    Given two(or three) arrays take the values in those arrays and simply
    assign them to the coordinates of the vertices. Yes you could do this
    with the array calculator, but your mom wears army boots so we're not
    going to.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAssignCoordinates, obj, update, **traits)
    
    x_coord_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the x coordinate array name.
        """
    )

    def _x_coord_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXCoordArrayName,
                        self.x_coord_array_name)

    y_coord_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the y coordinate array name.
        """
    )

    def _y_coord_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYCoordArrayName,
                        self.y_coord_array_name)

    z_coord_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the z coordinate array name.
        """
    )

    def _z_coord_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZCoordArrayName,
                        self.z_coord_array_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def set_jitter(self, *args):
        """
        V.set_jitter(bool)
        C++: void SetJitter(bool a)
        Set if you want a random jitter
        """
        ret = self._wrap_call(self._vtk_obj.SetJitter, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('x_coord_array_name', 'GetXCoordArrayName'), ('y_coord_array_name',
    'GetYCoordArrayName'), ('z_coord_array_name', 'GetZCoordArrayName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'x_coord_array_name',
    'y_coord_array_name', 'z_coord_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AssignCoordinates, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AssignCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['x_coord_array_name', 'y_coord_array_name',
            'z_coord_array_name']),
            title='Edit AssignCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AssignCoordinates properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

