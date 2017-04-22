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


class AMRDataInternals(Object):
    """
    AMRDataInternals - container of UniformGrid for an AMR data set
    
    Superclass: Object
    
    AMRDataInternals stores a list of non-empty blocks of an AMR data
    set
    
    @sa
    OverlappingAMR, AMRBox
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRDataInternals, obj, update, **traits)
    
    def get_data_set(self, *args):
        """
        V.get_data_set(int) -> UniformGrid
        C++: UniformGrid *GetDataSet(unsigned int compositeIndex)"""
        ret = self._wrap_call(self._vtk_obj.GetDataSet, *args)
        return wrap_vtk(ret)

    def _get_number_of_blocks(self):
        return self._vtk_obj.GetNumberOfBlocks()
    number_of_blocks = traits.Property(_get_number_of_blocks, help=\
        """
        
        """
    )

    def empty(self):
        """
        V.empty() -> bool
        C++: bool Empty()"""
        ret = self._vtk_obj.Empty()
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()"""
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert(self, *args):
        """
        V.insert(int, UniformGrid)
        C++: void Insert(unsigned int index, UniformGrid *grid)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Insert, *my_args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(Object)
        C++: virtual void ShallowCopy(Object *src)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
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
            return super(AMRDataInternals, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRDataInternals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit AMRDataInternals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRDataInternals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

