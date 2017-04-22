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

from tvtk.tvtk_classes.data_object import DataObject


class ImageStencilData(DataObject):
    """
    ImageStencilData - efficient description of an image stencil
    
    Superclass: DataObject
    
    ImageStencilData describes an image stencil in a manner which is
    efficient both in terms of speed and storage space.  The stencil
    extents are stored for each x-row across the image (multiple extents
    per row if necessary) and can be retrieved via the get_next_extent()
    method.
    @sa
    ImageStencilSource ImageStencil
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageStencilData, obj, update, **traits)
    
    extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, -1, 0, -1, 0, -1), cols=3, help=\
        """
        Set the extent of the data.  This is should be called only by
        ImageStencilSource, as it is part of the basic pipeline
        functionality.
        """
    )

    def _extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtent,
                        self.extent)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacing,
                        self.spacing)

    def get_next_extent(self, *args):
        """
        V.get_next_extent(int, int, int, int, int, int, int) -> int
        C++: int GetNextExtent(int &r1, int &r2, int xMin, int xMax,
            int yIdx, int zIdx, int &iter)
        Given the total output x extent [x_min,x_max] and the current y, z
        indices, return each sub-extent [r1,r2] that lies within within
        the unclipped region in sequence.  A value of '0' is returned if
        no more sub-extents are available.  The variable 'iter' must be
        initialized to zero before the first call, unless you want the
        complementary sub-extents in which case you must initialize
        'iter' to -1.  The variable 'iter' is used internally to keep
        track of which sub-extent should be returned next.
        """
        ret = self._wrap_call(self._vtk_obj.GetNextExtent, *args)
        return ret

    def add(self, *args):
        """
        V.add(ImageStencilData)
        C++: virtual void Add(ImageStencilData *)
        Add merges the stencil supplied as argument into Self.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Add, *my_args)
        return ret

    def allocate_extents(self):
        """
        V.allocate_extents()
        C++: void AllocateExtents()
        Allocate space for the sub-extents.  This is called by
        ImageStencilSource.
        """
        ret = self._vtk_obj.AllocateExtents()
        return ret
        

    def clip(self, *args):
        """
        V.clip([int, int, int, int, int, int]) -> int
        C++: virtual int Clip(int extent[6])
        Clip the stencil with the supplied extents. In other words,
        discard data outside the specified extents. Return 1 if something
        changed.
        """
        ret = self._wrap_call(self._vtk_obj.Clip, *args)
        return ret

    def fill(self):
        """
        V.fill()
        C++: void Fill()
        Fill the sub-extents.
        """
        ret = self._vtk_obj.Fill()
        return ret
        

    def insert_and_merge_extent(self, *args):
        """
        V.insert_and_merge_extent(int, int, int, int)
        C++: void InsertAndMergeExtent(int r1, int r2, int yIdx, int zIdx)
        Similar to insert_next_extent, except that the extent (r1,r2) at
        y_idx, z_idx is merged with other extents, (if any) on that row. So
        a unique extent may not necessarily be added. For instance, if an
        extent [5,11] already exists adding an extent, [7,9] will not
        affect the stencil. Likewise adding [10, 13] will replace the
        existing extent with [5,13].
        """
        ret = self._wrap_call(self._vtk_obj.InsertAndMergeExtent, *args)
        return ret

    def insert_next_extent(self, *args):
        """
        V.insert_next_extent(int, int, int, int)
        C++: void InsertNextExtent(int r1, int r2, int yIdx, int zIdx)
        This method is used by ImageStencilDataSource to add an x sub
        extent [r1,r2] for the x row (y_idx,z_idx).  The specified sub
        extent must not intersect any other sub extents along the same x
        row. As well, r1 and r2 must both be within the total x extent
        [Extent[0],Extent[1]].
        """
        ret = self._wrap_call(self._vtk_obj.InsertNextExtent, *args)
        return ret

    def internal_image_stencil_data_copy(self, *args):
        """
        V.internal_image_stencil_data_copy(ImageStencilData)
        C++: void InternalImageStencilDataCopy(ImageStencilData *s)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InternalImageStencilDataCopy, *my_args)
        return ret

    def is_inside(self, *args):
        """
        V.is_inside(int, int, int) -> int
        C++: int IsInside(int xIdx, int yIdx, int zIdx)
        Checks if an image index is inside the stencil. Even though
        get_next_extent and the ImageStencilIterator are faster if every
        voxel in the volume has to be checked, is_inside provides an
        efficient alternative for if just a single voxel has to be
        checked.
        """
        ret = self._wrap_call(self._vtk_obj.IsInside, *args)
        return ret

    def remove_extent(self, *args):
        """
        V.remove_extent(int, int, int, int)
        C++: void RemoveExtent(int r1, int r2, int yIdx, int zIdx)
        Remove the extent from (r1,r2) at y_idx, z_idx
        """
        ret = self._wrap_call(self._vtk_obj.RemoveExtent, *args)
        return ret

    def replace(self, *args):
        """
        V.replace(ImageStencilData)
        C++: virtual void Replace(ImageStencilData *)
        Replaces the portion of the stencil, supplied as argument, that
        lies within Self from Self.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Replace, *my_args)
        return ret

    def subtract(self, *args):
        """
        V.subtract(ImageStencilData)
        C++: virtual void Subtract(ImageStencilData *)
        Subtract removes the portion of the stencil, supplied as
        argument, that lies within Self from Self.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Subtract, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('extent', 'GetExtent'), ('origin', 'GetOrigin'), ('spacing',
    'GetSpacing'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'extent', 'origin', 'spacing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageStencilData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageStencilData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['extent', 'origin',
            'spacing']),
            title='Edit ImageStencilData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageStencilData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

