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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class TriangleFilter(PolyDataAlgorithm):
    """
    TriangleFilter - convert input polygons and strips to triangles
    
    Superclass: PolyDataAlgorithm
    
    TriangleFilter generates triangles from input polygons and
    triangle strips.  It also generates line segments from polylines
    unless pass_lines is off, and generates individual vertex cells from
    Vertex point lists unless pass_verts is off.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTriangleFilter, obj, update, **traits)
    
    pass_lines = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off passing lines through filter (default: on). If this
        is on, then the input polylines will be broken into line
        segments.  If it is off, then the input lines will be ignored and
        the output will have no lines.
        """
    )

    def _pass_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassLines,
                        self.pass_lines_)

    pass_verts = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off passing vertices through filter (default: on). If
        this is on, then the input vertex cells will be broken into
        individual vertex cells (one point per cell).  If it is off, the
        input vertex cells will be ignored.
        """
    )

    def _pass_verts_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassVerts,
                        self.pass_verts_)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('pass_lines', 'GetPassLines'), ('pass_verts', 'GetPassVerts'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'pass_lines',
    'pass_verts', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TriangleFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TriangleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_lines', 'pass_verts'], [], []),
            title='Edit TriangleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TriangleFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

