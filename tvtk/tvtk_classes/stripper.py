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


class Stripper(PolyDataAlgorithm):
    """
    Stripper - create triangle strips and/or poly-lines
    
    Superclass: PolyDataAlgorithm
    
    Stripper is a filter that generates triangle strips and/or
    poly-lines from input polygons, triangle strips, and lines. Input
    polygons are assembled into triangle strips only if they are
    triangles; other types of polygons are passed through to the output
    and not stripped. (Use TriangleFilter to triangulate
    non-triangular polygons prior to running this filter if you need to
    strip all the data.) The filter will pass through (to the output)
    vertices if they are present in the input polydata. Also note that if
    triangle strips or polylines are defined in the input they are passed
    through and not joined nor extended. (If you wish to strip these use
    TriangleFilter to fragment the input into triangles and lines
    prior to running Stripper.)
    
    The ivar maximum_length can be used to control the maximum allowable
    triangle strip and poly-line length.
    
    By default, this filter discards any cell data associated with the
    input. Thus is because the cell structure changes and and the old
    cell data is no longer valid. When pass_cell_data_as_field_data flag is
    set, the cell data is passed as field_data to the output using the
    following rule:
    1) for every cell in the output that is not a triangle strip, the
       cell data is inserted once per cell in the output field data.
    2) for every triangle strip cell in the output: ii) 1 tuple is
       inserted for every point(j|j>=2) in the strip. This is the cell
       data for the cell formed by (j-2, j-1, j) in the input. The field
       data order is same as cell data i.e. (verts,line,polys,tsrips).
    
    @warning
    If triangle strips or poly-lines exist in the input data they will be
    passed through to the output data. This filter will only construct
    triangle strips if triangle polygons are available; and will only
    construct poly-lines if lines are available.
    
    @sa
    TriangleFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStripper, obj, update, **traits)
    
    join_contiguous_segments = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal segments will be joined if they are
        contiguous. This is useful after slicing a surface. The default
        is off.
        """
    )

    def _join_contiguous_segments_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetJoinContiguousSegments,
                        self.join_contiguous_segments_)

    pass_cell_data_as_field_data = tvtk_base.false_bool_trait(help=\
        """
        Enable/Disable passing of the cell_data in the input to the output
        as field_data. Note the field data is transformed.
        """
    )

    def _pass_cell_data_as_field_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassCellDataAsFieldData,
                        self.pass_cell_data_as_field_data_)

    pass_through_cell_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal dataset will have a celldata array
        that holds the cell index of the original 3d cell that produced
        each output cell. This is useful for picking. The default is off
        to conserve memory.
        """
    )

    def _pass_through_cell_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThroughCellIds,
                        self.pass_through_cell_ids_)

    pass_through_point_ids = tvtk_base.false_bool_trait(help=\
        """
        If on, the output polygonal dataset will have a pointdata array
        that holds the point index of the original vertex that produced
        each output vertex. This is useful for picking. The default is
        off to conserve memory.
        """
    )

    def _pass_through_point_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassThroughPointIds,
                        self.pass_through_point_ids_)

    maximum_length = traits.Trait(1000, traits.Range(4, 100000, enter_set=True, auto_set=False), help=\
        """
        Specify the maximum number of triangles in a triangle strip,
        and/or the maximum number of lines in a poly-line.
        """
    )

    def _maximum_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLength,
                        self.maximum_length)

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
    (('join_contiguous_segments', 'GetJoinContiguousSegments'),
    ('pass_cell_data_as_field_data', 'GetPassCellDataAsFieldData'),
    ('pass_through_cell_ids', 'GetPassThroughCellIds'),
    ('pass_through_point_ids', 'GetPassThroughPointIds'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('maximum_length', 'GetMaximumLength'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'join_contiguous_segments', 'pass_cell_data_as_field_data',
    'pass_through_cell_ids', 'pass_through_point_ids',
    'release_data_flag', 'maximum_length', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Stripper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Stripper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['join_contiguous_segments', 'pass_cell_data_as_field_data',
            'pass_through_cell_ids', 'pass_through_point_ids'], [],
            ['maximum_length']),
            title='Edit Stripper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Stripper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

