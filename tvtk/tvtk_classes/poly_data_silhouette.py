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


class PolyDataSilhouette(PolyDataAlgorithm):
    """
    PolyDataSilhouette - sort polydata along camera view direction
    
    Superclass: PolyDataAlgorithm
    
    PolyDataSilhouette extracts a subset of a polygonal mesh edges to
    generate an outline (silhouette) of the corresponding 3d object. In
    addition, this filter can also extracts sharp edges (aka feature
    angles). In order to use this filter you must specify the a point of
    view (origin) or a direction (vector).  given this direction or
    origin, a silhouette is generated wherever the surface's normal is
    orthogonal to the view direction.
    
    @warning
    when the active camera is used, almost everything is recomputed for
    each frame, keep this in mind when dealing with extremely large
    surface data sets.
    
    @par Thanks: Contribution by Thierry Carrard
    
    CEA/DIF - Commissariat a l'Energie Atomique, Centre DAM Ile-De-France
    
    BP12, F-91297 Arpajon, France.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataSilhouette, obj, update, **traits)
    
    border_edges = tvtk_base.false_bool_trait(help=\
        """
        Enables or Disables generation of border edges. Note: borders
        exist only in case of non closed surface
        """
    )

    def _border_edges_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorderEdges,
                        self.border_edges_)

    piece_invariant = tvtk_base.true_bool_trait(help=\
        """
        Enables or Disables piece invariance. This is useful when dealing
        with multi-block data sets. Note: requires one level of ghost
        cells
        """
    )

    def _piece_invariant_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPieceInvariant,
                        self.piece_invariant_)

    direction = traits.Trait('camera_origin',
    tvtk_base.TraitRevPrefixMap({'camera_origin': 2, 'camera_vector': 3, 'specified_origin': 1, 'specified_vector': 0}), help=\
        """
        Specify how view direction is computed. By default, the camera
        origin (eye) is used.
        """
    )

    def _direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirection,
                        self.direction_)

    def _get_camera(self):
        return wrap_vtk(self._vtk_obj.GetCamera())
    def _set_camera(self, arg):
        old_val = self._get_camera()
        self._wrap_call(self._vtk_obj.SetCamera,
                        deref_vtk(arg))
        self.trait_property_changed('camera', old_val, arg)
    camera = traits.Property(_get_camera, _set_camera, help=\
        """
        Specify a camera that is used to define the view direction.  This
        ivar only has effect if the direction is set to
        VTK_DIRECTION_CAMERA_ORIGIN or VTK_DIRECTION_CAMERA_VECTOR, and a
        camera is specified.
        """
    )

    enable_feature_angle = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Enables or Disables generation of silhouette edges along sharp
        edges
        """
    )

    def _enable_feature_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableFeatureAngle,
                        self.enable_feature_angle)

    feature_angle = traits.Float(60.0, enter_set=True, auto_set=False, help=\
        """
        Sets/Gets minimal angle for sharp edges detection. Default is 60
        """
    )

    def _feature_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFeatureAngle,
                        self.feature_angle)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    def _get_prop3d(self):
        return wrap_vtk(self._vtk_obj.GetProp3D())
    def _set_prop3d(self, arg):
        old_val = self._get_prop3d()
        self._wrap_call(self._vtk_obj.SetProp3D,
                        deref_vtk(arg))
        self.trait_property_changed('prop3d', old_val, arg)
    prop3d = traits.Property(_get_prop3d, _set_prop3d, help=\
        """
        Specify a transformation matrix (via the Prop3D::GetMatrix()
        method) that is used to include the effects of transformation.
        This ivar only has effect if the direction is set to
        VTK_DIRECTION_CAMERA_ORIGIN or VTK_DIRECTION_CAMERA_VECTOR, and a
        camera is specified. Specifying the Prop3D is optional.
        """
    )

    vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVector,
                        self.vector)

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
    (('border_edges', 'GetBorderEdges'), ('piece_invariant',
    'GetPieceInvariant'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('direction',
    'GetDirection'), ('enable_feature_angle', 'GetEnableFeatureAngle'),
    ('feature_angle', 'GetFeatureAngle'), ('origin', 'GetOrigin'),
    ('vector', 'GetVector'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'border_edges', 'debug', 'global_warning_display',
    'piece_invariant', 'release_data_flag', 'direction',
    'enable_feature_angle', 'feature_angle', 'origin', 'progress_text',
    'vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataSilhouette, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataSilhouette properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['border_edges', 'piece_invariant'], ['direction'],
            ['enable_feature_angle', 'feature_angle', 'origin', 'vector']),
            title='Edit PolyDataSilhouette properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataSilhouette properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

