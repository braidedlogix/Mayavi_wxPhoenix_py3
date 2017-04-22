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


class ResliceCursorPicker(Picker):
    """
    ResliceCursorPicker - ray-cast cell picker for the reslice cursor
    
    Superclass: Picker
    
    This class is is used by the ResliceCursorWidget to pick reslice
    axes drawn by a ResliceCursorActor. The class returns the axes
    picked if any, whether one has picked the center. It takes as input
    an instance of ResliceCursorPolyDataAlgorithm. This is all done
    internally by ResliceCursorWidget and as such users are not
    expected to use this class directly, unless they are overriding the
    behaviour of ResliceCursorWidget.
    @sa
    ResliceCursor ResliceCursorWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceCursorPicker, obj, update, **traits)
    
    def _get_reslice_cursor_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetResliceCursorAlgorithm())
    def _set_reslice_cursor_algorithm(self, arg):
        old_val = self._get_reslice_cursor_algorithm()
        self._wrap_call(self._vtk_obj.SetResliceCursorAlgorithm,
                        deref_vtk(arg))
        self.trait_property_changed('reslice_cursor_algorithm', old_val, arg)
    reslice_cursor_algorithm = traits.Property(_get_reslice_cursor_algorithm, _set_reslice_cursor_algorithm, help=\
        """
        Set the reslice cursor algorithm. One must be set
        """
    )

    def _get_picked_axis1(self):
        return self._vtk_obj.GetPickedAxis1()
    picked_axis1 = traits.Property(_get_picked_axis1, help=\
        """
        Get the picked axis
        """
    )

    def _get_picked_axis2(self):
        return self._vtk_obj.GetPickedAxis2()
    picked_axis2 = traits.Property(_get_picked_axis2, help=\
        """
        Get the picked axis
        """
    )

    def _get_picked_center(self):
        return self._vtk_obj.GetPickedCenter()
    picked_center = traits.Property(_get_picked_center, help=\
        """
        Get the picked axis
        """
    )

    def set_transform_matrix(self, *args):
        """
        V.set_transform_matrix(Matrix4x4)
        C++: virtual void SetTransformMatrix(Matrix4x4 *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTransformMatrix, *my_args)
        return ret

    _updateable_traits_ = \
    (('pick_from_list', 'GetPickFromList'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('tolerance',
    'GetTolerance'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'pick_from_list', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceCursorPicker, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceCursorPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pick_from_list'], [], ['tolerance']),
            title='Edit ResliceCursorPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceCursorPicker properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

