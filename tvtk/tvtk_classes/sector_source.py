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


class SectorSource(PolyDataAlgorithm):
    """
    SectorSource - create a sector of a disk
    
    Superclass: PolyDataAlgorithm
    
    SectorSource creates a sector of a polygonal disk. The disk has
    zero height. The user can specify the inner and outer radius of the
    disk, the z-coordinate, and the radial and circumferential resolution
    of the polygonal representation.
    @sa
    LinearExtrusionFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSectorSource, obj, update, **traits)
    
    circumferential_resolution = traits.Trait(6, traits.Range(3, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in circumferential direction.
        """
    )

    def _circumferential_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCircumferentialResolution,
                        self.circumferential_resolution)

    end_angle = traits.Trait(90.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the end angle of the sector.
        """
    )

    def _end_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndAngle,
                        self.end_angle)

    inner_radius = traits.Trait(1.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify inner radius of the sector.
        """
    )

    def _inner_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInnerRadius,
                        self.inner_radius)

    outer_radius = traits.Trait(2.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify outer radius of the sector.
        """
    )

    def _outer_radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOuterRadius,
                        self.outer_radius)

    radial_resolution = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of points in radius direction.
        """
    )

    def _radial_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadialResolution,
                        self.radial_resolution)

    start_angle = traits.Trait(0.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Set the start angle of the sector.
        """
    )

    def _start_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartAngle,
                        self.start_angle)

    z_coord = traits.Trait(0.0, traits.Range(0.0, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Specify the z coordinate of the sector.
        """
    )

    def _z_coord_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZCoord,
                        self.z_coord)

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

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('circumferential_resolution', 'GetCircumferentialResolution'),
    ('end_angle', 'GetEndAngle'), ('inner_radius', 'GetInnerRadius'),
    ('outer_radius', 'GetOuterRadius'), ('radial_resolution',
    'GetRadialResolution'), ('start_angle', 'GetStartAngle'), ('z_coord',
    'GetZCoord'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'circumferential_resolution', 'end_angle',
    'inner_radius', 'outer_radius', 'progress_text', 'radial_resolution',
    'start_angle', 'z_coord'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SectorSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SectorSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['circumferential_resolution', 'end_angle',
            'inner_radius', 'outer_radius', 'radial_resolution', 'start_angle',
            'z_coord']),
            title='Edit SectorSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SectorSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

