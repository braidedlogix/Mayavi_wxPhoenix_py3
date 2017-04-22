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


class ExtractPolyDataGeometry(PolyDataAlgorithm):
    """
    ExtractPolyDataGeometry - extract PolyData cells that lies
    either entirely inside or outside of a specified implicit function
    
    Superclass: PolyDataAlgorithm
    
    ExtractPolyDataGeometry extracts from its input PolyData all
    cells that are either completely inside or outside of a specified
    implicit function. This filter is specialized to PolyData. On
    output the filter generates PolyData.
    
    To use this filter you must specify an implicit function. You must
    also specify whether to extract cells laying inside or outside of the
    implicit function. (The inside of an implicit function is the
    negative values region.) An option exists to extract cells that are
    neither inside nor outside (i.e., boundary).
    
    Note that this filter also has the option to directly pass all points
    or cull the points that do not satisfy the implicit function test.
    Passing all points is a tad faster, but then points remain that do
    not pass the test and may mess up subsequent glyphing operations and
    so on. By default points are culled.
    
    A more general version of this filter is available for arbitrary
    DataSet input (see ExtractGeometry).
    
    @sa
    ExtractGeometry ClipPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractPolyDataGeometry, obj, update, **traits)
    
    extract_boundary_cells = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether to extract cells that are partially
        inside. By default, extract_boundary_cells is off.
        """
    )

    def _extract_boundary_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractBoundaryCells,
                        self.extract_boundary_cells_)

    extract_inside = tvtk_base.true_bool_trait(help=\
        """
        Boolean controls whether to extract cells that are inside of
        implicit function (_extract_inside == 1) or outside of implicit
        function (_extract_inside == 0).
        """
    )

    def _extract_inside_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtractInside,
                        self.extract_inside_)

    pass_points = tvtk_base.false_bool_trait(help=\
        """
        Boolean controls whether points are culled or simply passed
        through to the output.
        """
    )

    def _pass_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassPoints,
                        self.pass_points_)

    def _get_implicit_function(self):
        return wrap_vtk(self._vtk_obj.GetImplicitFunction())
    def _set_implicit_function(self, arg):
        old_val = self._get_implicit_function()
        self._wrap_call(self._vtk_obj.SetImplicitFunction,
                        deref_vtk(arg))
        self.trait_property_changed('implicit_function', old_val, arg)
    implicit_function = traits.Property(_get_implicit_function, _set_implicit_function, help=\
        """
        Specify the implicit function for inside/outside checks.
        """
    )

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
    (('extract_boundary_cells', 'GetExtractBoundaryCells'),
    ('extract_inside', 'GetExtractInside'), ('pass_points',
    'GetPassPoints'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'extract_boundary_cells',
    'extract_inside', 'global_warning_display', 'pass_points',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractPolyDataGeometry, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractPolyDataGeometry properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['extract_boundary_cells', 'extract_inside', 'pass_points'], [],
            []),
            title='Edit ExtractPolyDataGeometry properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractPolyDataGeometry properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

