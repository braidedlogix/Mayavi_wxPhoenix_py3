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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class ResliceCursorPolyDataAlgorithm(PolyDataAlgorithm):
    """
    ResliceCursorPolyDataAlgorithm - generates a 2d reslice cursor
    polydata
    
    Superclass: PolyDataAlgorithm
    
    ResliceCursorPolyDataAlgorithm is a class that generates a 2d
    reslice cursor PolyData, suitable for rendering within a
    ResliceCursorActor. The class takes as input the reslice plane
    normal index (an index into the normal plane maintained by the
    reslice cursor object) and generates the polydata represeting the
    other two reslice axes suitable for rendering on a slice through this
    plane. The cursor consists of two intersection axes lines that meet
    at the cursor focus. These lines may have a user defined thickness.
    They need not be orthogonal to each other.
    @sa
    ResliceCursorActor ResliceCursor ResliceCursorWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceCursorPolyDataAlgorithm, obj, update, **traits)
    
    reslice_plane_normal = traits.Trait('x_axis',
    tvtk_base.TraitRevPrefixMap({'x_axis': 0, 'y_axis': 1, 'z_axis': 2}), help=\
        """
        Which of the 3 axes defines the reslice plane normal ?
        """
    )

    def _reslice_plane_normal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReslicePlaneNormal,
                        self.reslice_plane_normal_)

    def _get_reslice_cursor(self):
        return wrap_vtk(self._vtk_obj.GetResliceCursor())
    def _set_reslice_cursor(self, arg):
        old_val = self._get_reslice_cursor()
        self._wrap_call(self._vtk_obj.SetResliceCursor,
                        deref_vtk(arg))
        self.trait_property_changed('reslice_cursor', old_val, arg)
    reslice_cursor = traits.Property(_get_reslice_cursor, _set_reslice_cursor, help=\
        """
        Set the Reslice cursor from which to generate the polydata
        representation
        """
    )

    slice_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _slice_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceBounds,
                        self.slice_bounds)

    def _get_axis1(self):
        return self._vtk_obj.GetAxis1()
    axis1 = traits.Property(_get_axis1, help=\
        """
        Get the index of the axes and the planes that they represent
        """
    )

    def _get_axis2(self):
        return self._vtk_obj.GetAxis2()
    axis2 = traits.Property(_get_axis2, help=\
        """
        Get the index of the axes and the planes that they represent
        """
    )

    def _get_centerline_axis1(self):
        return wrap_vtk(self._vtk_obj.GetCenterlineAxis1())
    centerline_axis1 = traits.Property(_get_centerline_axis1, help=\
        """
        Get either one of the axes that this object produces. Depending
        on the mode, one renders either the centerline axes or both the
        centerline axes and the slab
        """
    )

    def _get_centerline_axis2(self):
        return wrap_vtk(self._vtk_obj.GetCenterlineAxis2())
    centerline_axis2 = traits.Property(_get_centerline_axis2, help=\
        """
        Get either one of the axes that this object produces. Depending
        on the mode, one renders either the centerline axes or both the
        centerline axes and the slab
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
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def get_other_plane_for_axis(self, *args):
        """
        V.get_other_plane_for_axis(int) -> int
        C++: int GetOtherPlaneForAxis(int p)
        Convenience method that, given one plane, returns the other plane
        that this class represents.
        """
        ret = self._wrap_call(self._vtk_obj.GetOtherPlaneForAxis, *args)
        return ret

    def _get_plane_axis1(self):
        return self._vtk_obj.GetPlaneAxis1()
    plane_axis1 = traits.Property(_get_plane_axis1, help=\
        """
        Get the index of the axes and the planes that they represent
        """
    )

    def _get_plane_axis2(self):
        return self._vtk_obj.GetPlaneAxis2()
    plane_axis2 = traits.Property(_get_plane_axis2, help=\
        """
        Get the index of the axes and the planes that they represent
        """
    )

    def _get_thick_slab_axis1(self):
        return wrap_vtk(self._vtk_obj.GetThickSlabAxis1())
    thick_slab_axis1 = traits.Property(_get_thick_slab_axis1, help=\
        """
        Get either one of the axes that this object produces. Depending
        on the mode, one renders either the centerline axes or both the
        centerline axes and the slab
        """
    )

    def _get_thick_slab_axis2(self):
        return wrap_vtk(self._vtk_obj.GetThickSlabAxis2())
    thick_slab_axis2 = traits.Property(_get_thick_slab_axis2, help=\
        """
        Get either one of the axes that this object produces. Depending
        on the mode, one renders either the centerline axes or both the
        centerline axes and the slab
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reslice_plane_normal', 'GetReslicePlaneNormal'), ('slice_bounds',
    'GetSliceBounds'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'reslice_plane_normal', 'progress_text',
    'slice_bounds'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceCursorPolyDataAlgorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceCursorPolyDataAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['reslice_plane_normal'], ['slice_bounds']),
            title='Edit ResliceCursorPolyDataAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceCursorPolyDataAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

