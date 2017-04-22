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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class TextureMapToCylinder(DataSetAlgorithm):
    """
    TextureMapToCylinder - generate texture coordinates by mapping
    points to cylinder
    
    Superclass: DataSetAlgorithm
    
    TextureMapToCylinder is a filter that generates 2d texture
    coordinates by mapping input dataset points onto a cylinder. The
    cylinder can either be user specified or generated automatically.
    (The cylinder is generated automatically by computing the axis of the
    cylinder.)  Note that the generated texture coordinates for the
    s-coordinate ranges from (0-1) (corresponding to angle of 0->360
    around axis), while the mapping of the t-coordinate is controlled by
    the projection of points along the axis.
    
    To specify a cylinder manually, you must provide two points that
    define the axis of the cylinder. The length of the axis will affect
    the t-coordinates.
    
    A special ivar controls how the s-coordinate is generated. If
    prevent_seam is set to true, the s-texture varies from 0->1 and then
    1->0 (corresponding to angles of 0->180 and 180->360).
    
    @warning
    Since the resulting texture s-coordinate will lie between (0,1), and
    the origin of the texture coordinates is not user-controllable, you
    may want to use the class TransformTexture to linearly scale and
    shift the origin of the texture coordinates.
    
    @sa
    TextureMapToPlane TextureMapToSphere TransformTexture
    ThresholdTextureCoords
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextureMapToCylinder, obj, update, **traits)
    
    automatic_cylinder_generation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off automatic cylinder generation. This means it
        automatically finds the cylinder center and axis.
        """
    )

    def _automatic_cylinder_generation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticCylinderGeneration,
                        self.automatic_cylinder_generation_)

    prevent_seam = tvtk_base.true_bool_trait(help=\
        """
        Control how the texture coordinates are generated. If prevent_seam
        is set, the s-coordinate ranges from 0->1 and 1->0 corresponding
        to the angle variation from 0->180 and 180->0. Otherwise, the
        s-coordinate ranges from 0->1 from 0->360 degrees.
        """
    )

    def _prevent_seam_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreventSeam,
                        self.prevent_seam_)

    point1 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, -0.5), cols=3, help=\
        """
        
        """
    )

    def _point1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint1,
                        self.point1)

    point2 = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.5), cols=3, help=\
        """
        
        """
    )

    def _point2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoint2,
                        self.point2)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('automatic_cylinder_generation', 'GetAutomaticCylinderGeneration'),
    ('prevent_seam', 'GetPreventSeam'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('point1', 'GetPoint1'), ('point2',
    'GetPoint2'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'automatic_cylinder_generation', 'debug',
    'global_warning_display', 'prevent_seam', 'release_data_flag',
    'point1', 'point2', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextureMapToCylinder, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextureMapToCylinder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic_cylinder_generation', 'prevent_seam'], [],
            ['point1', 'point2']),
            title='Edit TextureMapToCylinder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextureMapToCylinder properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

