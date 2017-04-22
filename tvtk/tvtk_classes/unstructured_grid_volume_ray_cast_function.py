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


class UnstructuredGridVolumeRayCastFunction(Object):
    """
    UnstructuredGridVolumeRayCastFunction - a superclass for ray
    casting functions
    
    Superclass: Object
    
    UnstructuredGridVolumeRayCastFunction is a superclass for ray
    casting functions that can be used within a
    UnstructuredGridVolumeRayCastMapper.
    
    @sa
    UnstructuredGridVolumeRayCastMapper
    UnstructuredGridVolumeRayIntegrator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridVolumeRayCastFunction, obj, update, **traits)
    
    def finalize(self):
        """
        V.finalize()
        C++: virtual void Finalize()"""
        ret = self._vtk_obj.Finalize()
        return ret
        

    def initialize(self, *args):
        """
        V.initialize(Renderer, Volume)
        C++: virtual void Initialize(Renderer *ren, Volume *vol)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def new_iterator(self):
        """
        V.new_iterator() -> UnstructuredGridVolumeRayCastIterator
        C++: virtual UnstructuredGridVolumeRayCastIterator *NewIterator(
            )
        Returns a new object that will iterate over all the intersections
        of a ray with the cells of the input.  The calling code is
        responsible for deleting the returned object.
        """
        ret = wrap_vtk(self._vtk_obj.NewIterator())
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
            return super(UnstructuredGridVolumeRayCastFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridVolumeRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit UnstructuredGridVolumeRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridVolumeRayCastFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

