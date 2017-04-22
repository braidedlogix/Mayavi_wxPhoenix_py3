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


class AbstractCellLinks(Object):
    """
    AbstractCellLinks - an abstract base class for classes that build
    topological links from points to cells
    
    Superclass: Object
    
    AbstractCellLinks is a family of supplemental objects to
    CellArray and CellTypes, enabling fast access from points to
    the cells using the points. AbstractCellLinks is an array of
    links, each link representing a list of cell ids using a particular
    point. The information provided by this object can be used to
    determine neighbors and construct other local topological
    information.
    
    @sa
    CellLinks StaticCellLinks StaticCellLinksTemplate
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAbstractCellLinks, obj, update, **traits)
    
    def get_id_type(self, *args):
        """
        V.get_id_type(int, int, CellArray) -> int
        C++: static int GetIdType(IdType maxPtId, IdType maxCellId,
            CellArray *ca)
        Based on the input (i.e., number of points, number of cells, and
        length of connectivity array) this helper method returns the
        integral type to use when instantiating cell link-related classes
        in order to properly represent the data.  The return value is one
        of the types (VTK_ID_TYPE,VTK_INT,VTK_SHORT) defined in the file
        Type.h. Subclasses may choose to instantiate themselves with
        different integral types for performance and/or memory reasons.
        """
        my_args = deref_array(args, [('int', 'int', 'vtkCellArray')])
        ret = self._wrap_call(self._vtk_obj.GetIdType, *my_args)
        return ret

    def build_links(self, *args):
        """
        V.build_links(DataSet)
        C++: virtual void BuildLinks(DataSet *data)
        Build the link list array. All subclasses must implement this
        method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.BuildLinks, *my_args)
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
            return super(AbstractCellLinks, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AbstractCellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit AbstractCellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AbstractCellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

