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

from tvtk.tvtk_classes.abstract_point_locator import AbstractPointLocator


class StaticPointLocator(AbstractPointLocator):
    """
    StaticPointLocator - quickly locate points in 3-space
    
    Superclass: AbstractPointLocator
    
    StaticPointLocator is a spatial search object to quickly locate
    points in 3d.  StaticPointLocator works by dividing a specified
    region of space into a regular array of cuboid buckets, and then
    keeping a list of points that lie in each bucket. Typical operation
    involves giving a position in 3d and finding the closest point; or
    finding the N closest points.
    
    StaticPointLocator is an accelerated version of PointLocator.
    It is threaded (via SMPTools), and supports one-time static
    construction (i.e., incremental point insertion is not supported). If
    you need to incrementally insert points, use the PointLocator or
    its kin to do so.
    
    @warning
    This class is templated. It may run slower than serial execution if
    the code is not optimized during compilation. Build in Release or
    release_with_debug_info.
    
    @warning
    Make sure that you review the documentation for the superclasses
    AbstactPointLocator and Locator. In particular the Automatic
    data member can be used to automatically determine divisions based on
    the average number of points per bucket.
    
    @warning
    Other types of spatial locators have been developed such as octrees
    and kd-trees. These are often more efficient for the operations
    described here.
    
    @sa
    PointLocator CellLocator Locator AbstractPointLocator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStaticPointLocator, obj, update, **traits)
    
    divisions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(50, 50, 50), cols=3, help=\
        """
        
        """
    )

    def _divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivisions,
                        self.divisions)

    number_of_points_per_bucket = traits.Trait(5, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the average number of points in each bucket. This data
        member is used in conjunction with the Automatic data member (if
        enabled) to determine the number of locator x-y-z divisions.
        """
    )

    def _number_of_points_per_bucket_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPointsPerBucket,
                        self.number_of_points_per_bucket)

    def get_bucket_ids(self, *args):
        """
        V.get_bucket_ids(int, IdList)
        C++: void GetBucketIds(IdType bNum, IdList *bList)
        Given a bucket number b_num between 0 <= b_num <
        this->_get_number_of_buckets(), return a list of point ids contained
        within the bucket. The user must provide an instance of IdList
        to contain the result.
        """
        my_args = deref_array(args, [('int', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetBucketIds, *my_args)
        return ret

    def _get_large_ids(self):
        return self._vtk_obj.GetLargeIds()
    large_ids = traits.Property(_get_large_ids, help=\
        """
        Inform the user as to whether large ids are being used. This flag
        only has meaning after the locator has been built. Large ids are
        used when the number of binned points, or the number of bins, is
        >= the signed integer max value.
        """
    )

    def get_number_of_points_in_bucket(self, *args):
        """
        V.get_number_of_points_in_bucket(int) -> int
        C++: IdType GetNumberOfPointsInBucket(IdType bNum)
        Given a bucket number b_num between 0 <= b_num <
        this->_get_number_of_buckets(), return the number of points found in
        the bucket.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfPointsInBucket, *args)
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
            return super(StaticPointLocator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StaticPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic'], [], ['divisions', 'max_level',
            'number_of_points_per_bucket', 'tolerance']),
            title='Edit StaticPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StaticPointLocator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

