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


class StructuredGridGeometryFilter(PolyDataAlgorithm):
    """
    StructuredGridGeometryFilter - extract geometry for structured grid
    
    Superclass: PolyDataAlgorithm
    
    StructuredGridGeometryFilter is a filter that extracts geometry
    from a structured grid. By specifying appropriate i-j-k indices, it
    is possible to extract a point, a curve, a surface, or a "volume".
    Depending upon the type of data, the curve and surface may be curved
    or planar. (The volume is actually a (n x m x o) region of points.)
    
    The extent specification is zero-offset. That is, the first k-plane
    in a 50x50x50 structured grid is given by (0,49, 0,49, 0,0).
    
    The output of this filter is affected by the structured grid
    blanking. If blanking is on, and a blanking array defined, then those
    cells attached to blanked points are not output. (Blanking is a
    property of the input StructuredGrid.)
    
    @warning
    If you don't know the dimensions of the input dataset, you can use a
    large number to specify extent (the number will be clamped
    appropriately). For example, if the dataset dimensions are 50x50x50,
    and you want a the fifth k-plane, you can use the extents (0,100,
    0,100, 4,4). The 100 will automatically be clamped to 49.
    
    @sa
    GeometryFilter ExtractGrid StructuredGrid
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStructuredGridGeometryFilter, obj, update, **traits)
    
    extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, 2147483647, 0, 2147483647, 0, 2147483647), cols=3, help=\
        """
        Specify (imin,imax, jmin,jmax, kmin,kmax) indices.
        """
    )

    def _extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtent,
                        self.extent)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('extent',
    'GetExtent'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'extent', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StructuredGridGeometryFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StructuredGridGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['extent']),
            title='Edit StructuredGridGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StructuredGridGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

