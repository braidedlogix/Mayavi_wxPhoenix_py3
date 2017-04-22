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

from tvtk.tvtk_classes.locator import Locator


class AbstractPointLocator(Locator):
    """
    AbstractPointLocator - abstract class to quickly locate points in
    3-space
    
    Superclass: Locator
    
    AbstractPointLocator is an abstract spatial search object to
    quickly locate points in 3d. AbstractPointLocator works by
    dividing a specified region of space into "rectangular" buckets, and
    then keeping a list of points that lie in each bucket. Typical
    operation involves giving a position in 3d and finding the closest
    point.  The points are provided from the specified dataset input.
    
    @sa
    PointLocator StaticPointLocator MergePoints
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractPointLocator, obj, update, **traits)
    
    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Provide an accessor to the bounds.
        """
    )

    def _get_number_of_buckets(self):
        return self._vtk_obj.GetNumberOfBuckets()
    number_of_buckets = traits.Property(_get_number_of_buckets, help=\
        """
        Return the total number of buckets in the locator. This has
        meaning only after the locator is constructed.
        """
    )

    def find_closest_n_points(self, *args):
        """
        V.find_closest_n_points(int, (float, float, float), IdList)
        C++: virtual void FindClosestNPoints(int N, const double x[3],
            IdList *result)
        V.find_closest_n_points(int, float, float, float, IdList)
        C++: void FindClosestNPoints(int N, double x, double y, double z,
            IdList *result)
        Find the closest N points to a position. This returns the closest
        N points to a position. A faster method could be created that
        returned N close points to a position, but necessarily the exact
        N closest. The returned points are sorted from closest to
        farthest. These methods are thread safe if build_locator() is
        directly or indirectly called from a single thread first.
        """
        my_args = deref_array(args, [('int', ('float', 'float', 'float'), 'vtkIdList'), ('int', 'float', 'float', 'float', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.FindClosestNPoints, *my_args)
        return ret

    def find_closest_point(self, *args):
        """
        V.find_closest_point((float, float, float)) -> int
        C++: virtual IdType FindClosestPoint(const double x[3])
        V.find_closest_point(float, float, float) -> int
        C++: IdType FindClosestPoint(double x, double y, double z)
        Given a position x, return the id of the point closest to it.
        Alternative method requires separate x-y-z values. These methods
        are thread safe if build_locator() is directly or indirectly
        called from a single thread first.
        """
        ret = self._wrap_call(self._vtk_obj.FindClosestPoint, *args)
        return ret

    def find_closest_point_within_radius(self, *args):
        """
        V.find_closest_point_within_radius(float, (float, float, float),
            float) -> int
        C++: virtual IdType FindClosestPointWithinRadius(double radius,
             const double x[3], double &dist2)
        Given a position x and a radius r, return the id of the point
        closest to the point in that radius. dist2 returns the squared
        distance to the point.
        """
        ret = self._wrap_call(self._vtk_obj.FindClosestPointWithinRadius, *args)
        return ret

    def find_points_within_radius(self, *args):
        """
        V.find_points_within_radius(float, (float, float, float), IdList)
        C++: virtual void FindPointsWithinRadius(double R,
            const double x[3], IdList *result)
        V.find_points_within_radius(float, float, float, float, IdList)
        C++: void FindPointsWithinRadius(double R, double x, double y,
            double z, IdList *result)
        Find all points within a specified radius R of position x. The
        result is not sorted in any specific manner. These methods are
        thread safe if build_locator() is directly or indirectly called
        from a single thread first.
        """
        my_args = deref_array(args, [('float', ('float', 'float', 'float'), 'vtkIdList'), ('float', 'float', 'float', 'float', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.FindPointsWithinRadius, *my_args)
        return ret

    _updateable_traits_ = \
    (('automatic', 'GetAutomatic'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('max_level',
    'GetMaxLevel'), ('tolerance', 'GetTolerance'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'global_warning_display', 'max_level',
    'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AbstractPointLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic'], [], ['max_level', 'tolerance']),
            title='Edit AbstractPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

