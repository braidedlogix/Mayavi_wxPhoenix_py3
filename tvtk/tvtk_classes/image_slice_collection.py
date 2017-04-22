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

from tvtk.tvtk_classes.prop_collection import PropCollection


class ImageSliceCollection(PropCollection):
    """
    ImageSliceCollection - a sorted list of image slice objects
    
    Superclass: PropCollection
    
    ImageSliceCollection is a PropCollection that maintains a list
    of ImageSlice objects that are sorted by layer_number. This allows
    the images to be rendered in the correct order.
    @sa
    ImageSlice ImageAssembly
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSliceCollection, obj, update, **traits)
    
    def _get_next_image(self):
        return wrap_vtk(self._vtk_obj.GetNextImage())
    next_image = traits.Property(_get_next_image, help=\
        """
        Standard Collection methods.  You must call init_traversal before
        calling get_next_image.  If possible, you should use the
        get_next_image method that takes a collection iterator instead.
        """
    )

    def _get_next_item(self):
        return wrap_vtk(self._vtk_obj.GetNextItem())
    next_item = traits.Property(_get_next_item, help=\
        """
        Access routine provided for compatibility with previous versions
        of VTK.  Please use the get_next_image() variant where possible.
        """
    )

    def sort(self):
        """
        V.sort()
        C++: void Sort()
        Sorts the ImageSliceCollection by layer number.  Smaller layer
        numbers are first. Layer numbers can be any integer value. Items
        with the same layer number will be kept in the same relative
        order as before the sort.
        """
        ret = self._vtk_obj.Sort()
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
            return super(ImageSliceCollection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSliceCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ImageSliceCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSliceCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

