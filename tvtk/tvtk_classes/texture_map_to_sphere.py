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


class TextureMapToSphere(DataSetAlgorithm):
    """
    TextureMapToSphere - generate texture coordinates by mapping
    points to sphere
    
    Superclass: DataSetAlgorithm
    
    TextureMapToSphere is a filter that generates 2d texture
    coordinates by mapping input dataset points onto a sphere. The sphere
    can either be user specified or generated automatically. (The sphere
    is generated automatically by computing the center (i.e., averaged
    coordinates) of the sphere.)  Note that the generated texture
    coordinates range between (0,1). The s-coordinate lies in the angular
    direction around the z-axis, measured counter-clockwise from the
    x-axis. The t-coordinate lies in the angular direction measured down
    from the north pole towards the south pole.
    
    A special ivar controls how the s-coordinate is generated. If
    prevent_seam is set to true, the s-texture varies from 0->1 and then
    1->0 (corresponding to angles of 0->180 and 180->360).
    
    @warning
    The resulting texture coordinates will lie between (0,1), and the
    texture coordinates are determined with respect to the modeler's
    x-y-z coordinate system. Use the class TransformTextureCoords to
    linearly scale and shift the origin of the texture coordinates (if
    necessary).
    
    @sa
    TextureMapToPlane TextureMapToCylinder TransformTexture
    ThresholdTextureCoords
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextureMapToSphere, obj, update, **traits)
    
    automatic_sphere_generation = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off automatic sphere generation. This means it
        automatically finds the sphere center.
        """
    )

    def _automatic_sphere_generation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutomaticSphereGeneration,
                        self.automatic_sphere_generation_)

    prevent_seam = tvtk_base.true_bool_trait(help=\
        """
        Control how the texture coordinates are generated. If prevent_seam
        is set, the s-coordinate ranges from 0->1 and 1->0 corresponding
        to the theta angle variation between 0->180 and 180->0 degrees.
        Otherwise, the s-coordinate ranges from 0->1 between 0->360
        degrees.
        """
    )

    def _prevent_seam_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPreventSeam,
                        self.prevent_seam_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('automatic_sphere_generation', 'GetAutomaticSphereGeneration'),
    ('prevent_seam', 'GetPreventSeam'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('center', 'GetCenter'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'automatic_sphere_generation', 'debug',
    'global_warning_display', 'prevent_seam', 'release_data_flag',
    'center', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextureMapToSphere, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextureMapToSphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic_sphere_generation', 'prevent_seam'], [],
            ['center']),
            title='Edit TextureMapToSphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextureMapToSphere properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

