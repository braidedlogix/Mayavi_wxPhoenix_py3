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


class ExodusIICache(Object):
    """
    ExodusIICache - no description provided.
    
    Superclass: Object
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExodusIICache, obj, update, **traits)
    
    def _get_space_left(self):
        return self._vtk_obj.GetSpaceLeft()
    space_left = traits.Property(_get_space_left, help=\
        """
        See how much cache space is left. This is the difference between
        the capacity and the size of the cache. The result is in mi_b.
        """
    )

    def clear(self):
        """
        V.clear()
        C++: void Clear()
        Empty the cache
        """
        ret = self._vtk_obj.Clear()
        return ret
        

    def insert(self, *args):
        """
        V.insert(ExodusIICacheKey, DataArray)
        C++: void Insert(ExodusIICacheKey &key, DataArray *value)
        Insert an entry into the cache (this can remove other cache
        entries to make space).
        """
        my_args = deref_array(args, [('vtkExodusIICacheKey', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.Insert, *my_args)
        return ret

    def invalidate(self, *args):
        """
        V.invalidate(ExodusIICacheKey) -> int
        C++: int Invalidate(ExodusIICacheKey key)
        V.invalidate(ExodusIICacheKey, ExodusIICacheKey) -> int
        C++: int Invalidate(ExodusIICacheKey key,
            ExodusIICacheKey pattern)
        Invalidate a cache entry (drop it from the cache) if the key
        exists. This does nothing if the cache entry does not exist.
        Returns 1 if the cache entry existed prior to this call and 0
        otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Invalidate, *my_args)
        return ret

    def reduce_to_size(self, *args):
        """
        V.reduce_to_size(float) -> int
        C++: int ReduceToSize(double newSize)
        Remove cache entries until the size of the cache is at or below
        the given size. Returns a nonzero value if deletions were
        required.
        """
        ret = self._wrap_call(self._vtk_obj.ReduceToSize, *args)
        return ret

    def set_cache_capacity(self, *args):
        """
        V.set_cache_capacity(float)
        C++: void SetCacheCapacity(double sizeInMiB)
        Set the maximum allowable cache size. This will remove cache
        entries if the capacity is reduced below the current size.
        """
        ret = self._wrap_call(self._vtk_obj.SetCacheCapacity, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExodusIICache, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExodusIICache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ExodusIICache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExodusIICache properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

