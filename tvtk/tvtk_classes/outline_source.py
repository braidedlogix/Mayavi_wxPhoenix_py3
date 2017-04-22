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


class OutlineSource(PolyDataAlgorithm):
    """
    OutlineSource - create wireframe outline around bounding box
    
    Superclass: PolyDataAlgorithm
    
    OutlineSource creates a wireframe outline around a user-specified
    bounding box.  The outline may be created aligned with the {x,y,z}
    axis - in which case it is defined by the 6 bounds
    {xmin,xmax,ymin,ymax,zmin,zmax} via set_bounds(). Alternatively, the
    box may be arbitrarily aligned, in which case it should be set via
    the set_corners() member.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOutlineSource, obj, update, **traits)
    
    generate_faces = tvtk_base.false_bool_trait(help=\
        """
        Generate solid faces for the box. This is off by default.
        """
    )

    def _generate_faces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateFaces,
                        self.generate_faces_)

    box_type = traits.Trait('axis_aligned',
    tvtk_base.TraitRevPrefixMap({'axis_aligned': 0, 'oriented': 1}), help=\
        """
        Set box type to axis_aligned (default) or Oriented. Use the method
        set_bounds() with axis_aligned mode, and set_corners() with Oriented
        mode.
        """
    )

    def _box_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoxType,
                        self.box_type_)

    bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    corners = traits.Array(enter_set=True, auto_set=False, shape=(24,), dtype=float, value=(0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0), cols=3, help=\
        """
        Specify the corners of the outline when in Oriented mode, the
        values are supplied as 8*3 double values The correct corner
        ordering is using {x,y,z} convention for the unit cube as
        follows:
        {0,0,0},{1,0,0},{0,1,0},{1,1,0},{0,0,1},{1,0,1},{0,1,1},{1,1,1}.
        """
    )

    def _corners_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCorners,
                        self.corners)

    output_points_precision = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output points.
        Algorithm::SINGLE_PRECISION - Output single-precision floating
        point. Algorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

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
    (('generate_faces', 'GetGenerateFaces'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('box_type', 'GetBoxType'), ('bounds',
    'GetBounds'), ('corners', 'GetCorners'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_faces',
    'global_warning_display', 'release_data_flag', 'box_type', 'bounds',
    'corners', 'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OutlineSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_faces'], ['box_type'], ['bounds', 'corners',
            'output_points_precision']),
            title='Edit OutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

