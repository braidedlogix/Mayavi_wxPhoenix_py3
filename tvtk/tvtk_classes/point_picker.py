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

from tvtk.tvtk_classes.picker import Picker


class PointPicker(Picker):
    """
    PointPicker - select a point by shooting a ray into a graphics
    window
    
    Superclass: Picker
    
    PointPicker is used to select a point by shooting a ray into a
    graphics window and intersecting with actor's defining geometry -
    specifically its points. Beside returning coordinates, actor, and
    mapper, PointPicker returns the id of the point projecting closest
    onto the ray (within the specified tolerance).  Ties are broken
    (i.e., multiple points all projecting within the tolerance along the
    pick ray) by choosing the point closest to the ray.
    
    @sa
    Picker CellPicker.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointPicker, obj, update, **traits)
    
    use_cells = tvtk_base.false_bool_trait(help=\
        """
        Specify whether the point search should be based on cell points
        or directly on the point list.
        """
    )

    def _use_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseCells,
                        self.use_cells_)

    def _get_point_id(self):
        return self._vtk_obj.GetPointId()
    point_id = traits.Property(_get_point_id, help=\
        """
        Get the id of the picked point. If point_id = -1, nothing was
        picked.
        """
    )

    _updateable_traits_ = \
    (('use_cells', 'GetUseCells'), ('pick_from_list', 'GetPickFromList'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('tolerance', 'GetTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_from_list', 'use_cells',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointPicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pick_from_list', 'use_cells'], [], ['tolerance']),
            title='Edit PointPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

