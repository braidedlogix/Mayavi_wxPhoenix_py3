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


class GraphEdge(Object):
    """
    GraphEdge - Representation of a single graph edge.
    
    Superclass: Object
    
    A heavy-weight (vtk_object subclass) graph edge object that may be
    used instead of the EdgeType struct, for use with wrappers. The
    edge contains the source and target vertex ids, and the edge id.
    
    @sa
    Graph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGraphEdge, obj, update, **traits)
    
    id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The id of the edge.
        """
    )

    def _id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetId,
                        self.id)

    def _get_source(self):
        return self._vtk_obj.GetSource()
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        arg)
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        The source of the edge.
        """
    )

    target = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The target of the edge.
        """
    )

    def _target_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTarget,
                        self.target)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('id', 'GetId'), ('target', 'GetTarget'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'id', 'target'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GraphEdge, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GraphEdge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['id', 'target']),
            title='Edit GraphEdge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GraphEdge properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

