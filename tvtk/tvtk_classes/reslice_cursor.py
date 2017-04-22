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

from tvtk.tvtk_classes.object import Object


class ResliceCursor(Object):
    """
    ResliceCursor - Geometry for a reslice cursor
    
    Superclass: Object
    
    This class represents a reslice cursor. It consists of two cross
    sectional hairs, with an optional thickness. The crosshairs hairs may
    have a hole in the center. These may be translated or rotated
    independent of each other in the view. The result is used to reslice
    the data along these cross sections. This allows the user to perform
    multi-planar thin or thick reformat of the data on an image view,
    rather than a 3d view.
    @sa
    ResliceCursorWidget ResliceCursor
    ResliceCursorPolyDataAlgorithm ResliceCursorRepresentation
    ResliceCursorThickLineRepresentation ResliceCursorActor
    ImagePlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceCursor, obj, update, **traits)
    
    thick_mode = tvtk_base.true_bool_trait(help=\
        """
        Enable disable thick mode. Default is to enable it.
        """
    )

    def _thick_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThickMode,
                        self.thick_mode_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the cente of the reslice cursor.
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    hole = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Show a hole in the center of the cursor, so its easy to see the
        pixels within the hole. ON by default
        """
    )

    def _hole_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHole,
                        self.hole)

    hole_width = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Set the width of the hole in mm
        """
    )

    def _hole_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHoleWidth,
                        self.hole_width)

    hole_width_in_pixels = traits.Float(16.0, enter_set=True, auto_set=False, help=\
        """
        Set the width of the hole in pixels. If set, this will override
        the hole with in mm.
        """
    )

    def _hole_width_in_pixels_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHoleWidthInPixels,
                        self.hole_width_in_pixels)

    def _get_image(self):
        return wrap_vtk(self._vtk_obj.GetImage())
    def _set_image(self, arg):
        old_val = self._get_image()
        self._wrap_call(self._vtk_obj.SetImage,
                        deref_vtk(arg))
        self.trait_property_changed('image', old_val, arg)
    image = traits.Property(_get_image, _set_image, help=\
        """
        Set the image (_3d) that we are slicing
        """
    )

    thickness = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThickness,
                        self.thickness)

    x_axis = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _x_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXAxis,
                        self.x_axis)

    y_axis = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 1.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _y_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYAxis,
                        self.y_axis)

    z_axis = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _z_axis_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZAxis,
                        self.z_axis)

    def get_axis(self, *args):
        """
        V.get_axis(int) -> (float, ...)
        C++: virtual double *GetAxis(int i)
        Get the computed axes directions
        """
        ret = self._wrap_call(self._vtk_obj.GetAxis, *args)
        return ret

    def get_centerline_axis_poly_data(self, *args):
        """
        V.get_centerline_axis_poly_data(int) -> PolyData
        C++: virtual PolyData *GetCenterlineAxisPolyData(int axis)
        Get the slab and centerline polydata along an axis
        """
        ret = self._wrap_call(self._vtk_obj.GetCenterlineAxisPolyData, *args)
        return wrap_vtk(ret)

    def get_plane(self, *args):
        """
        V.get_plane(int) -> Plane
        C++: virtual Plane *GetPlane(int n)
        Get the planes that represent normals along the X, Y and Z. The
        argument passed to this method must be an integer in the range
        0-2 (corresponding to the X, Y and Z axes.
        """
        ret = self._wrap_call(self._vtk_obj.GetPlane, *args)
        return wrap_vtk(ret)

    def _get_poly_data(self):
        return wrap_vtk(self._vtk_obj.GetPolyData())
    poly_data = traits.Property(_get_poly_data, help=\
        """
        Get the 3d poly_data representation
        """
    )

    def reset(self):
        """
        V.reset()
        C++: virtual void Reset()
        Reset the cursor to the default position, ie with the axes,
        normal to each other and axis aligned and with the cursor pointed
        at the center of the image.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def update(self):
        """
        V.update()
        C++: virtual void Update()
        Build the polydata
        """
        ret = self._vtk_obj.Update()
        return ret
        

    _updateable_traits_ = \
    (('thick_mode', 'GetThickMode'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('hole', 'GetHole'), ('hole_width', 'GetHoleWidth'),
    ('hole_width_in_pixels', 'GetHoleWidthInPixels'), ('thickness',
    'GetThickness'), ('x_axis', 'GetXAxis'), ('y_axis', 'GetYAxis'),
    ('z_axis', 'GetZAxis'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'thick_mode', 'center', 'hole',
    'hole_width', 'hole_width_in_pixels', 'thickness', 'x_axis', 'y_axis',
    'z_axis'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceCursor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['thick_mode'], [], ['center', 'hole', 'hole_width',
            'hole_width_in_pixels', 'thickness', 'x_axis', 'y_axis', 'z_axis']),
            title='Edit ResliceCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceCursor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

