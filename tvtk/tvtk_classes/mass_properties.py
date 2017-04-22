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


class MassProperties(PolyDataAlgorithm):
    """
    MassProperties - estimate volume, area, shape index of triangle
    mesh
    
    Superclass: PolyDataAlgorithm
    
    MassProperties estimates the volume, the surface area, and the
    normalized shape index of a triangle mesh.  The algorithm implemented
    here is based on the discrete form of the divergence theorem.  The
    general assumption here is that the model is of closed surface.  For
    more details see the following reference (Alyassin A.M. et al,
    "Evaluation of new algorithms for the interactive measurement of
    surface area and volume", Med Phys 21(6) 1994.).
    
    @warning
    Currently only triangles are processed. Use TriangleFilter to
    convert any strips or polygons to triangles.
    
    @sa
    TriangleFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMassProperties, obj, update, **traits)
    
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

    def _get_kx(self):
        return self._vtk_obj.GetKx()
    kx = traits.Property(_get_kx, help=\
        """
        Compute and return the weighting factors for the maximum unit
        normal component (MUNC).
        """
    )

    def _get_ky(self):
        return self._vtk_obj.GetKy()
    ky = traits.Property(_get_ky, help=\
        """
        
        """
    )

    def _get_kz(self):
        return self._vtk_obj.GetKz()
    kz = traits.Property(_get_kz, help=\
        """
        
        """
    )

    def _get_max_cell_area(self):
        return self._vtk_obj.GetMaxCellArea()
    max_cell_area = traits.Property(_get_max_cell_area, help=\
        """
        Compute and return the max cell area.
        """
    )

    def _get_min_cell_area(self):
        return self._vtk_obj.GetMinCellArea()
    min_cell_area = traits.Property(_get_min_cell_area, help=\
        """
        Compute and return the min cell area.
        """
    )

    def _get_normalized_shape_index(self):
        return self._vtk_obj.GetNormalizedShapeIndex()
    normalized_shape_index = traits.Property(_get_normalized_shape_index, help=\
        """
        Compute and return the normalized shape index. This characterizes
        the deviation of the shape of an object from a sphere. A sphere's
        NSI is one. This number is always >= 1.0.
        """
    )

    def _get_surface_area(self):
        return self._vtk_obj.GetSurfaceArea()
    surface_area = traits.Property(_get_surface_area, help=\
        """
        Compute and return the area.
        """
    )

    def _get_volume(self):
        return self._vtk_obj.GetVolume()
    volume = traits.Property(_get_volume, help=\
        """
        Compute and return the volume.
        """
    )

    def _get_volume_projected(self):
        return self._vtk_obj.GetVolumeProjected()
    volume_projected = traits.Property(_get_volume_projected, help=\
        """
        Compute and return the projected volume. Typically you should
        compare this volume to the value returned by get_volume if you get
        an error (_get_volume()-_get_volume_projected())*_10000 that is greater
        than get_volume() this should identify a problem:
        * Either the polydata is not closed
        * Or the polydata contains triangle that are flipped
        """
    )

    def _get_volume_x(self):
        return self._vtk_obj.GetVolumeX()
    volume_x = traits.Property(_get_volume_x, help=\
        """
        Compute and return the volume projected on to each axis aligned
        plane.
        """
    )

    def _get_volume_y(self):
        return self._vtk_obj.GetVolumeY()
    volume_y = traits.Property(_get_volume_y, help=\
        """
        
        """
    )

    def _get_volume_z(self):
        return self._vtk_obj.GetVolumeZ()
    volume_z = traits.Property(_get_volume_z, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MassProperties, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MassProperties properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit MassProperties properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MassProperties properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

