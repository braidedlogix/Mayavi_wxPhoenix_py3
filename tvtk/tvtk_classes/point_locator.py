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

from tvtk.tvtk_classes.incremental_point_locator import IncrementalPointLocator


class PointLocator(IncrementalPointLocator):
    """
    PointLocator - quickly locate points in 3-space
    
    Superclass: IncrementalPointLocator
    
    PointLocator is a spatial search object to quickly locate points
    in 3d. PointLocator works by dividing a specified region of space
    into a regular array of "rectangular" buckets, and then keeping a
    list of points that lie in each bucket. Typical operation involves
    giving a position in 3d and finding the closest point.
    
    PointLocator has two distinct methods of interaction. In the first
    method, you supply it with a dataset, and it operates on the points
    in the dataset. In the second method, you supply it with an array of
    points, and the object operates on the array.
    
    @warning
    Many other types of spatial locators have been developed such as
    octrees and kd-trees. These are often more efficient for the
    operations described here.
    
    @sa
    CellPicker PointPicker StaticPointLocator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointLocator, obj, update, **traits)
    
    divisions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(50, 50, 50), cols=3, help=\
        """
        
        """
    )

    def _divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivisions,
                        self.divisions)

    number_of_points_per_bucket = traits.Trait(3, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the average number of points in each bucket.
        """
    )

    def _number_of_points_per_bucket_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPointsPerBucket,
                        self.number_of_points_per_bucket)

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    points = traits.Property(_get_points, help=\
        """
        Provide an accessor to the points.
        """
    )

    def get_points_in_bucket(self, *args):
        """
        V.get_points_in_bucket((float, float, float), [int, int, int])
            -> IdList
        C++: virtual IdList *GetPointsInBucket(const double x[3],
            int ijk[3])
        Given a position x, return the list of points in the bucket that
        contains the point. It is possible that NULL is returned. The
        user provides an ijk array that is the indices into the locator.
        This method is thread safe.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointsInBucket, *args)
        return wrap_vtk(ret)

    def find_distributed_points(self, *args):
        """
        V.find_distributed_points(int, (float, float, float), IdList,
            int)
        C++: virtual void FindDistributedPoints(int N, const double x[3],
            IdList *result, int M)
        V.find_distributed_points(int, float, float, float, IdList, int)
        C++: virtual void FindDistributedPoints(int N, double x, double y,
             double z, IdList *result, int M)
        Find the closest points to a position such that each octant of
        space around the position contains at least N points. Loosely
        limit the search to a maximum number of points evaluated, M.
        These methods are thread safe if build_locator() is directly or
        indirectly called from a single thread first.
        """
        my_args = deref_array(args, [('int', ('float', 'float', 'float'), 'vtkIdList', 'int'), ('int', 'float', 'float', 'float', 'vtkIdList', 'int')])
        ret = self._wrap_call(self._vtk_obj.FindDistributedPoints, *my_args)
        return ret

    _updateable_traits_ = \
    (('automatic', 'GetAutomatic'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('divisions',
    'GetDivisions'), ('number_of_points_per_bucket',
    'GetNumberOfPointsPerBucket'), ('max_level', 'GetMaxLevel'),
    ('tolerance', 'GetTolerance'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'global_warning_display', 'divisions',
    'max_level', 'number_of_points_per_bucket', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic'], [], ['divisions', 'max_level',
            'number_of_points_per_bucket', 'tolerance']),
            title='Edit PointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

