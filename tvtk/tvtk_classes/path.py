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

from tvtk.tvtk_classes.point_set import PointSet


class Path(PointSet):
    """
    Path - concrete dataset representing a path defined by Bezier
    curves.
    
    Superclass: PointSet
    
    Path provides a container for paths composed of line segments,
    2nd-order (quadratic) and 3rd-order (cubic) Bezier curves.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPath, obj, update, **traits)
    
    def _get_codes(self):
        return wrap_vtk(self._vtk_obj.GetCodes())
    def _set_codes(self, arg):
        old_val = self._get_codes()
        my_arg = deref_array([arg], [['vtkIntArray']])
        self._wrap_call(self._vtk_obj.SetCodes,
                        my_arg[0])
        self.trait_property_changed('codes', old_val, arg)
    codes = traits.Property(_get_codes, _set_codes, help=\
        """
        Set/Get the array of control point codes:
        """
    )

    def allocate(self, *args):
        """
        V.allocate(int, int)
        C++: void Allocate(IdType size=1000, int extSize=1000)
        Method allocates initial storage for points. Use this method
        before the method Path::InsertNextPoint().
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def insert_next_point(self, *args):
        """
        V.insert_next_point([float, float, float], int)
        C++: void InsertNextPoint(double pts[3], int code)
        V.insert_next_point(float, float, float, int)
        C++: void InsertNextPoint(double x, double y, double z, int code)
        Insert the next control point in the path.
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextPoint, *args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Begin inserting data all over again. Memory is not freed but
        otherwise objects are returned to their initial state.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Path, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Path properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit Path properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Path properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

