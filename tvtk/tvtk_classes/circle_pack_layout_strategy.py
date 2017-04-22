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


class CirclePackLayoutStrategy(Object):
    """
    CirclePackLayoutStrategy - abstract superclass for all circle
    packing layout strategies.
    
    Superclass: Object
    
    All subclasses of this class perform a circle packing layout on a
    Tree. This involves assigning a circle to each vertex in the tree,
    and placing that information in a data array with three components
    per tuple representing (Xcenter, Ycenter, Radius).
    
    Instances of subclasses of this class may be assigned as the layout
    strategy to CirclePackLayout
    
    @par Thanks: Thanks to Thomas Otahal from Sandia National
    Laboratories for help developing this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCirclePackLayoutStrategy, obj, update, **traits)
    
    def layout(self, *args):
        """
        V.layout(Tree, DataArray, DataArray)
        C++: virtual void Layout(Tree *inputTree,
            DataArray *areaArray, DataArray *sizeArray)
        Perform the layout of the input tree, and store the circle bounds
        of each vertex as a tuple in a data array. (Xcenter, Ycenter,
        Radius).
        
        * The size_array may be NULL, or may contain the desired
        * size of each vertex in the tree.
        """
        my_args = deref_array(args, [('vtkTree', 'vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.Layout, *my_args)
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
            return super(CirclePackLayoutStrategy, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CirclePackLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit CirclePackLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CirclePackLayoutStrategy properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

