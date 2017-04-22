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


class Cursor3D(PolyDataAlgorithm):
    """
    Cursor3D - generate a 3d cursor representation
    
    Superclass: PolyDataAlgorithm
    
    Cursor3D is an object that generates a 3d representation of a
    cursor. The cursor consists of a wireframe bounding box, three
    intersecting axes lines that meet at the cursor focus, and "shadows"
    or projections of the axes against the sides of the bounding box.
    Each of these components can be turned on/off.
    
    This filter generates two output datasets. The first (Output) is just
    the geometric representation of the cursor. The second (Focus) is a
    single point at the focal point.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCursor3D, obj, update, **traits)
    
    axes = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe axes.
        """
    )

    def _axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxes,
                        self.axes_)

    outline = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe bounding box.
        """
    )

    def _outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutline,
                        self.outline_)

    translation_mode = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable the translation mode. If on, changes in cursor
        position cause the entire widget to translate along with the
        cursor. By default, translation mode is off.
        """
    )

    def _translation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationMode,
                        self.translation_mode_)

    wrap = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off cursor wrapping. If the cursor focus moves outside
        the specified bounds, the cursor will either be restrained
        against the nearest "wall" (Wrap=off), or it will wrap around
        (Wrap=on).
        """
    )

    def _wrap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrap,
                        self.wrap_)

    x_shadows = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe x-shadows.
        """
    )

    def _x_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXShadows,
                        self.x_shadows_)

    y_shadows = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe y-shadows.
        """
    )

    def _y_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYShadows,
                        self.y_shadows_)

    z_shadows = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the wireframe z-shadows.
        """
    )

    def _z_shadows_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZShadows,
                        self.z_shadows_)

    focal_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the position of cursor focus. If translation mode is on,
        then the entire cursor (including bounding box, cursor, and
        shadows) is translated. Otherwise, the focal point will either be
        clamped to the bounding box, or wrapped, if Wrap is on. (Note:
        this behavior requires that the bounding box is set prior to the
        focal point.)
        """
    )

    def _focal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFocalPoint,
                        self.focal_point)

    model_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), cols=3, help=\
        """
        Set / get the boundary of the 3d cursor.
        """
    )

    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    def _get_focus(self):
        return wrap_vtk(self._vtk_obj.GetFocus())
    focus = traits.Property(_get_focus, help=\
        """
        Get the focus for this filter.
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

    def all_off(self):
        """
        V.all_off()
        C++: void AllOff()
        Turn every part of the 3d cursor on or off.
        """
        ret = self._vtk_obj.AllOff()
        return ret
        

    def all_on(self):
        """
        V.all_on()
        C++: void AllOn()
        Turn every part of the 3d cursor on or off.
        """
        ret = self._vtk_obj.AllOn()
        return ret
        

    _updateable_traits_ = \
    (('axes', 'GetAxes'), ('outline', 'GetOutline'), ('translation_mode',
    'GetTranslationMode'), ('wrap', 'GetWrap'), ('x_shadows',
    'GetXShadows'), ('y_shadows', 'GetYShadows'), ('z_shadows',
    'GetZShadows'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('focal_point',
    'GetFocalPoint'), ('model_bounds', 'GetModelBounds'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'axes', 'debug', 'global_warning_display',
    'outline', 'release_data_flag', 'translation_mode', 'wrap',
    'x_shadows', 'y_shadows', 'z_shadows', 'focal_point', 'model_bounds',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Cursor3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Cursor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['axes', 'outline', 'translation_mode', 'wrap', 'x_shadows',
            'y_shadows', 'z_shadows'], [], ['focal_point', 'model_bounds']),
            title='Edit Cursor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Cursor3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

