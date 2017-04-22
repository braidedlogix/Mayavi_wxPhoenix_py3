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

from tvtk.tvtk_classes.abstract_mapper import AbstractMapper


class AbstractMapper3D(AbstractMapper):
    """
    AbstractMapper3D - abstract class specifies interface to map 3d
    data
    
    Superclass: AbstractMapper
    
    AbstractMapper3D is an abstract class to specify interface between
    3d data and graphics primitives or software rendering techniques.
    Subclasses of AbstractMapper3D can be used for rendering geometry
    or rendering volumetric data.
    
    This class also defines an API to support hardware clipping planes
    (at most six planes can be defined). It also provides geometric data
    about the input data it maps, such as the bounding box and center.
    
    @sa
    AbstractMapper Mapper PolyDataMapper VolumeMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractMapper3D, obj, update, **traits)
    
    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Return bounding box (array of six doubles) of data expressed as
        (xmin,xmax, ymin,ymax, zmin,zmax). Update this->Bounds as a side
        effect.
        """
    )

    def _get_center(self):
        return self._vtk_obj.GetCenter()
    center = traits.Property(_get_center, help=\
        """
        Return the Center of this mapper's data.
        """
    )

    def get_clipping_plane_in_data_coords(self, *args):
        """
        V.get_clipping_plane_in_data_coords(Matrix4x4, int, [float, float,
            float, float])
        C++: void GetClippingPlaneInDataCoords(Matrix4x4 *propMatrix,
            int i, double planeEquation[4])
        Get the ith clipping plane as a homogeneous plane equation. Use
        get_number_of_clipping_planes to get the number of planes.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetClippingPlaneInDataCoords, *my_args)
        return ret

    def _get_length(self):
        return self._vtk_obj.GetLength()
    length = traits.Property(_get_length, help=\
        """
        Return the diagonal length of this mappers bounding box.
        """
    )

    def _get_number_of_clipping_planes(self):
        return self._vtk_obj.GetNumberOfClippingPlanes()
    number_of_clipping_planes = traits.Property(_get_number_of_clipping_planes, help=\
        """
        Get the number of clipping planes.
        """
    )

    def is_a_ray_cast_mapper(self):
        """
        V.is_a_ray_cast_mapper() -> int
        C++: virtual int IsARayCastMapper()
        Is this a ray cast mapper? A subclass would return 1 if the ray
        caster is needed to generate an image from this mapper.
        """
        ret = self._vtk_obj.IsARayCastMapper()
        return ret
        

    def is_a_render_into_image_mapper(self):
        """
        V.is_a_render_into_image_mapper() -> int
        C++: virtual int IsARenderIntoImageMapper()
        Is this a "render into image" mapper? A subclass would return 1
        if the mapper produces an image by rendering into a software
        image buffer.
        """
        ret = self._vtk_obj.IsARenderIntoImageMapper()
        return ret
        

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
            return super(AbstractMapper3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit AbstractMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractMapper3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

