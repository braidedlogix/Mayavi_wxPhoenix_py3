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

from tvtk.tvtk_classes.abstract_cell_links import AbstractCellLinks


class StaticCellLinks(AbstractCellLinks):
    """
    StaticCellLinks - object represents upward pointers from points to
    list of cells using each point
    
    Superclass: AbstractCellLinks
    
    StaticCellLinks is a supplemental object to CellArray and
    CellTypes, enabling access from points to the cells using the
    points. StaticCellLinks is an array of links, each link represents
    a list of cell ids using a particular point. The information provided
    by this object can be used to determine neighbors and construct other
    local topological information. This class is a faster implementation
    of CellLinks. However, it cannot be incrementally constructed; it
    is meant to be constructed once (statically) and must be rebuilt if
    the cells change.
    
    @warning
    This is a drop-in replacement for CellLinks using static link
    construction. It uses the templated StaticCellLinksTemplate class,
    instantiating StaticCellLinksTemplate with a IdType template
    parameter. Note that for best performance, the
    StaticCellLinksTemplate class may be used directly, instantiating
    it with the appropriate id type. This class is also wrappable and can
    be used from an interpreted language such as Python.
    
    @sa
    CellLinks StaticCellLinksTemplate
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStaticCellLinks, obj, update, **traits)
    
    def get_cells(self, *args):
        """
        V.get_cells(int) -> (int, ...)
        C++: const IdType *GetCells(IdType ptId)
        Return a list of cell ids using the specified point.
        """
        ret = self._wrap_call(self._vtk_obj.GetCells, *args)
        return ret

    def get_ncells(self, *args):
        """
        V.get_ncells(int) -> int
        C++: unsigned short GetNcells(IdType ptId)
        Get the number of cells using the point specified by pt_id. This
        is an alias for get_number_of_cells(); consistent with the
        CellLinks API.
        """
        ret = self._wrap_call(self._vtk_obj.GetNcells, *args)
        return ret

    def get_number_of_cells(self, *args):
        """
        V.get_number_of_cells(int) -> int
        C++: IdType GetNumberOfCells(IdType ptId)
        Get the number of cells using the point specified by pt_id.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfCells, *args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Make sure any previously created links are cleaned up.
        """
        ret = self._vtk_obj.Initialize()
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
            return super(StaticCellLinks, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StaticCellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit StaticCellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StaticCellLinks properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

