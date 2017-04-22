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


class EdgeSubdivisionCriterion(Object):
    """
    EdgeSubdivisionCriterion - how to decide whether a linear
    approximation to nonlinear geometry or field should be subdivided
    
    Superclass: Object
    
    Descendants of this abstract class are used to decide whether a
    piecewise linear approximation (triangles, lines, ... ) to some
    nonlinear geometry should be subdivided. This decision may be based
    on an absolute error metric (chord error) or on some view-dependent
    metric (chord error compared to device resolution) or on some
    abstract metric (color error). Or anything else, really. Just so long
    as you implement the evaluate_edge member, all will be well.
    
    @sa
    DataSetSubdivisionAlgorithm StreamingTessellator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEdgeSubdivisionCriterion, obj, update, **traits)
    
    def _get_field_ids(self):
        return self._vtk_obj.GetFieldIds()
    field_ids = traits.Property(_get_field_ids, help=\
        """
        Return the map from output field id to input field ids. That is,
        field i of any output vertex from StreamingTessellator will be
        associated with get_field_ids()[ i] on the input mesh.
        """
    )

    def _get_field_offsets(self):
        return self._vtk_obj.GetFieldOffsets()
    field_offsets = traits.Property(_get_field_offsets, help=\
        """
        Return the offset into an output vertex array of all fields. That
        is, field i of any output vertex, p, from StreamingTessellator
        will have its first entry at p[ get_field_offsets()[ i] ] .
        """
    )

    def _get_number_of_fields(self):
        return self._vtk_obj.GetNumberOfFields()
    number_of_fields = traits.Property(_get_number_of_fields, help=\
        """
        Return the number of fields being evaluated at each output
        vertex. This is the length of the arrays returned by
        get_field_ids() and_get_field_offsets().
        """
    )

    def get_output_field(self, *args):
        """
        V.get_output_field(int) -> int
        C++: int GetOutputField(int fieldId)
        Return the output ID of an input field. Returns -1 if field_id is
        not set to be passed to the output.
        """
        ret = self._wrap_call(self._vtk_obj.GetOutputField, *args)
        return ret

    def dont_pass_field(self, *args):
        """
        V.dont_pass_field(int, StreamingTessellator) -> bool
        C++: virtual bool DontPassField(int sourceId,
            StreamingTessellator *t)
        This does the opposite of pass_field(); it removes a field from
        the output (assuming the field was set to be passed). Returns
        true if any action was taken, false otherwise.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DontPassField, *my_args)
        return ret

    def evaluate_edge(self, *args):
        """
        V.evaluate_edge((float, ...), [float, ...], (float, ...), int)
            -> bool
        C++: virtual bool EvaluateEdge(const double *p0, double *p1,
            const double *p2, int field_start)
        You must implement this member function in a subclass. It will be
        called by StreamingTessellator for each edge in each primitive
        that StreamingTessellator generates.
        """
        ret = self._wrap_call(self._vtk_obj.EvaluateEdge, *args)
        return ret

    def pass_field(self, *args):
        """
        V.pass_field(int, int, StreamingTessellator) -> int
        C++: virtual int PassField(int sourceId, int sourceSize,
            StreamingTessellator *t)
        This is a helper routine called by pass_fields() which you may
        also call directly; it adds source_size to the size of the output
        vertex field values. The offset of the source_id field in the
        output vertex array is returned.
        -1 is returned if source_size would force the output to have more
           than StreamingTessellator::MaxFieldSize field values per
           vertex.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PassField, *my_args)
        return ret

    def reset_field_list(self):
        """
        V.reset_field_list()
        C++: virtual void ResetFieldList()
        Don't pass any field values in the vertex pointer. This is used
        to reset the list of fields to pass after a successful run of
        StreamingTessellator.
        """
        ret = self._vtk_obj.ResetFieldList()
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
            return super(EdgeSubdivisionCriterion, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EdgeSubdivisionCriterion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit EdgeSubdivisionCriterion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EdgeSubdivisionCriterion properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

