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


class HyperOctreePointsGrabber(Object):
    """
    HyperOctreePointsGrabber - An object used by filters to store
    points computed on face or edge of an hyperoctant.
    
    Superclass: Object
    
    It is an abstract class. ClipHyperOctree and HyperOctreeCutter
    use HyperOctreeClipCutPointsGrabber HyperOctreeContourFilter
    use an internal one: HyperOctreeContourFilterPointsGrabber.
    
    @sa
    HyperOctree, HyperOctreeClipCutPointsGrabber,
    ClipHyperOctree, HyperOctreeCutter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperOctreePointsGrabber, obj, update, **traits)
    
    dimension = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set the dimension of the hyperoctree.
        \pre valid_dim: (dim==2 || dim==3)
        \post is_set: get_dimension()==dim
        """
    )

    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    def init_point_insertion(self):
        """
        V.init_point_insertion()
        C++: virtual void InitPointInsertion()
        Initialize the points insertion scheme. Actually, it is just a
        trick to initialize the id_set from the filter. The id_set class
        cannot be shared with the filter because it is a Pimpl. It is
        used by clip,cut and contour filters to build the points that lie
        on an hyperoctant.
        \pre only_in_3d: get_dimension()==_3
        """
        ret = self._vtk_obj.InitPointInsertion()
        return ret
        

    def insert_point(self, *args):
        """
        V.insert_point(int, [float, float, float], [float, float, float],
            [int, int, int])
        C++: virtual void InsertPoint(IdType ptId, double pt[3],
            double pcoords[3], int ijk[3])
        Insert a point, assuming the point is unique and does not require
        a locator. Tt does not mean it does not use a locator. It just
        mean that some implementation may skip the use of a locator.
        """
        ret = self._wrap_call(self._vtk_obj.InsertPoint, *args)
        return ret

    def insert_point2d(self, *args):
        """
        V.insert_point2d([float, float, float], [int, int, int])
        C++: virtual void InsertPoint2D(double pt[3], int ijk[3])
        Insert a point in the quadtree case.
        """
        ret = self._wrap_call(self._vtk_obj.InsertPoint2D, *args)
        return ret

    def insert_point_with_merge(self, *args):
        """
        V.insert_point_with_merge(int, [float, float, float], [float, float,
            float], [int, int, int])
        C++: virtual void InsertPointWithMerge(IdType ptId,
            double pt[3], double pcoords[3], int ijk[3])
        Insert a point using a locator.
        """
        ret = self._wrap_call(self._vtk_obj.InsertPointWithMerge, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('dimension', 'GetDimension'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'dimension'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperOctreePointsGrabber, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperOctreePointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['dimension']),
            title='Edit HyperOctreePointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperOctreePointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

