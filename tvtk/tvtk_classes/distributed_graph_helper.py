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


class DistributedGraphHelper(Object):
    """
    VertexPedigreeIdDistributionFunction - The type of a function used
    to determine how to distribute vertex pedigree IDs across processors
    in a Graph. The pedigree ID distribution function takes the
    pedigree ID of the vertex and a user-supplied void pointer and
    returns a hash value V. A vertex with that pedigree ID will reside on
    processor V % P, where P is the number of processors. This type is
    used in conjunction with the DistributedGraphHelper class.
    
    Superclass: Object
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDistributedGraphHelper, obj, update, **traits)
    
    def get_edge_index(self, *args):
        """
        V.get_edge_index(int) -> int
        C++: IdType GetEdgeIndex(IdType e_id)
        Returns local index of edge with ID e_id, by masking off top
        ceil(log2 P) bits of e_id.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgeIndex, *args)
        return ret

    def get_edge_owner(self, *args):
        """
        V.get_edge_owner(int) -> int
        C++: IdType GetEdgeOwner(IdType e_id)
        Returns owner of edge with ID e_id, by extracting top ceil(log2
        P) bits of e_id.
        """
        ret = self._wrap_call(self._vtk_obj.GetEdgeOwner, *args)
        return ret

    def get_vertex_index(self, *args):
        """
        V.get_vertex_index(int) -> int
        C++: IdType GetVertexIndex(IdType v)
        Returns local index of vertex v, by masking off top ceil(log2 P)
        bits of v.
        """
        ret = self._wrap_call(self._vtk_obj.GetVertexIndex, *args)
        return ret

    def get_vertex_owner(self, *args):
        """
        V.get_vertex_owner(int) -> int
        C++: IdType GetVertexOwner(IdType v)
        Returns owner of vertex v, by extracting top ceil(log2 P) bits of
        v.
        """
        ret = self._wrap_call(self._vtk_obj.GetVertexOwner, *args)
        return ret

    def get_vertex_owner_by_pedigree_id(self, *args):
        """
        V.get_vertex_owner_by_pedigree_id(Variant) -> int
        C++: IdType GetVertexOwnerByPedigreeId(
            const Variant &pedigreeId)
        Determine which processor owns the vertex with the given pedigree
        ID.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetVertexOwnerByPedigreeId, *my_args)
        return ret

    def clone(self):
        """
        V.clone() -> DistributedGraphHelper
        C++: virtual DistributedGraphHelper *Clone()
        Clones the distributed graph helper, returning another
        distributed graph helper of the same kind that can be used in
        another Graph.
        """
        ret = wrap_vtk(self._vtk_obj.Clone())
        return ret
        

    def DISTRIBUTEDEDGEIDS(self):
        """
        V.distributededgeids() -> InformationIntegerKey
        C++: static InformationIntegerKey *DISTRIBUTEDEDGEIDS()
        Information Keys that distributed graphs can append to attribute
        arrays to flag them as containing distributed IDs.  These can be
        used to let routines that migrate vertices (either repartitioning
        or collecting graphs to single nodes) to also modify the ids
        contained in the attribute arrays to maintain consistency.
        """
        ret = wrap_vtk(self._vtk_obj.DISTRIBUTEDEDGEIDS())
        return ret
        

    def DISTRIBUTEDVERTEXIDS(self):
        """
        V.distributedvertexids() -> InformationIntegerKey
        C++: static InformationIntegerKey *DISTRIBUTEDVERTEXIDS()
        Information Keys that distributed graphs can append to attribute
        arrays to flag them as containing distributed IDs.  These can be
        used to let routines that migrate vertices (either repartitioning
        or collecting graphs to single nodes) to also modify the ids
        contained in the attribute arrays to maintain consistency.
        """
        ret = wrap_vtk(self._vtk_obj.DISTRIBUTEDVERTEXIDS())
        return ret
        

    def make_distributed_id(self, *args):
        """
        V.make_distributed_id(int, int) -> int
        C++: IdType MakeDistributedId(int owner, IdType local)
        Builds a distributed ID consisting of the given owner and the
        local ID.
        """
        ret = self._wrap_call(self._vtk_obj.MakeDistributedId, *args)
        return ret

    def synchronize(self):
        """
        V.synchronize()
        C++: virtual void Synchronize()
        Synchronizes all of the processors involved in this distributed
        graph, so that all processors have a consistent view of the
        distributed graph for the computation that follows. This routine
        should be invoked after adding new edges into the distributed
        graph, so that other processors will see those edges (or their
        corresponding back-edges).
        """
        ret = self._vtk_obj.Synchronize()
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
            return super(DistributedGraphHelper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DistributedGraphHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit DistributedGraphHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DistributedGraphHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

