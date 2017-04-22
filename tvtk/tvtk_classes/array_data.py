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


class ArrayData(DataObject):
    """
    ArrayData - Pipeline data object that contains multiple Array
    objects.
    
    Superclass: DataObject
    
    Because Array cannot be stored as attributes of data objects
    (yet), a "carrier" object is needed to pass Array through the
    pipeline.  ArrayData acts as a container of zero-to-many Array
    instances, which can be retrieved via a zero-based index.  Note that
    a collection of arrays stored in ArrayData may-or-may-not have
    related types, dimensions, or extents.
    
    @sa
    ArrayDataAlgorithm, Array
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArrayData, obj, update, **traits)
    
    def get_array(self, *args):
        """
        V.get_array(int) -> Array
        C++: Array *GetArray(IdType index)
        Returns the n-th Array in the collection
        """
        ret = self._wrap_call(self._vtk_obj.GetArray, *args)
        return wrap_vtk(ret)

    def get_array_by_name(self, *args):
        """
        V.get_array_by_name(string) -> Array
        C++: Array *GetArrayByName(const char *name)
        Returns the array having called name from the collection
        """
        ret = self._wrap_call(self._vtk_obj.GetArrayByName, *args)
        return wrap_vtk(ret)

    def _get_number_of_arrays(self):
        return self._vtk_obj.GetNumberOfArrays()
    number_of_arrays = traits.Property(_get_number_of_arrays, help=\
        """
        Returns the number of Array instances in the collection
        """
    )

    def add_array(self, *args):
        """
        V.add_array(Array)
        C++: void AddArray(Array *)
        Adds a Array to the collection
        """
        my_args = deref_array(args, [['vtkArray']])
        ret = self._wrap_call(self._vtk_obj.AddArray, *my_args)
        return ret

    def clear_arrays(self):
        """
        V.clear_arrays()
        C++: void ClearArrays()
        Clears the contents of the collection
        """
        ret = self._vtk_obj.ClearArrays()
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
            return super(ArrayData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ArrayData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit ArrayData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArrayData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

