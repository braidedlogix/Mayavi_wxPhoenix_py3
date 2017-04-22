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


class LabelPlacer(PolyDataAlgorithm):
    """
    LabelPlacer - place a prioritized hierarchy of labels in screen
    space
    
    Superclass: PolyDataAlgorithm
    
    This class is deprecated and will be removed from VTK in a future
    release. Use LabelPlacementMapper instead.
    
    This should probably be a mapper unto itself (given that the polydata
    output could be large and will realistically always be iterated over
    exactly once before being tossed for the next frame of the render).
    
    In any event, it takes as input one (or more, eventually)
    LabelHierarchies that represent prioritized lists of labels sorted
    by their placement in space. As output, it provides PolyData
    containing only VTK_QUAD cells, each representing a single label from
    the input. Each quadrilateral has cell data indicating what label in
    the input it corresponds to (via an array named "_label_id").
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabelPlacer, obj, update, **traits)
    
    generate_perturbed_label_spokes = tvtk_base.false_bool_trait(help=\
        """
        Enable drawing spokes (lines) to anchor point coordinates that
        were perturbed for being coincident with other anchor point
        coordinates.
        """
    )

    def _generate_perturbed_label_spokes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePerturbedLabelSpokes,
                        self.generate_perturbed_label_spokes_)

    output_traversed_bounds = tvtk_base.false_bool_trait(help=\
        """
        In the second output, output the geometry of the traversed octree
        nodes.
        """
    )

    def _output_traversed_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputTraversedBounds,
                        self.output_traversed_bounds_)

    positions_as_normals = tvtk_base.false_bool_trait(help=\
        """
        Use label anchor point coordinates as normal vectors and
        eliminate those pointing away from the camera. Valid only when
        points are on a sphere centered at the origin (such as a 3d
        geographic view). Off by default.
        """
    )

    def _positions_as_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPositionsAsNormals,
                        self.positions_as_normals_)

    use_depth_buffer = tvtk_base.false_bool_trait(help=\
        """
        Use the depth buffer to test each label to see if it should not
        be displayed if it would be occluded by other objects in the
        scene. Off by default.
        """
    )

    def _use_depth_buffer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseDepthBuffer,
                        self.use_depth_buffer_)

    use_unicode_strings = tvtk_base.false_bool_trait(help=\
        """
        Set whether, or not, to use unicode strings.
        """
    )

    def _use_unicode_strings_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseUnicodeStrings,
                        self.use_unicode_strings_)

    gravity = traits.Int(36, enter_set=True, auto_set=False, help=\
        """
        The placement of the label relative to the anchor point.
        """
    )

    def _gravity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGravity,
                        self.gravity)

    iterator_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        The type of iterator used when traversing the labels. May be
        LabelHierarchy::FRUSTUM or LabelHierarchy::FULL_SORT.
        """
    )

    def _iterator_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIteratorType,
                        self.iterator_type)

    maximum_label_fraction = traits.Trait(0.05, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        The maximum amount of screen space labels can take up before
        placement terminates.
        """
    )

    def _maximum_label_fraction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumLabelFraction,
                        self.maximum_label_fraction)

    output_coordinate_system = traits.Trait(0, traits.Range(0, 1, enter_set=True, auto_set=False), help=\
        """
        Set/get the coordinate system used for output labels. The output
        datasets may have point coordinates reported in the world space
        or display space.
        """
    )

    def _output_coordinate_system_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputCoordinateSystem,
                        self.output_coordinate_system)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        
        """
    )

    def _get_anchor_transform(self):
        return wrap_vtk(self._vtk_obj.GetAnchorTransform())
    anchor_transform = traits.Property(_get_anchor_transform, help=\
        """
        
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

    def output_coordinate_system_display(self):
        """
        V.output_coordinate_system_display()
        C++: void OutputCoordinateSystemDisplay()
        Set/get the coordinate system used for output labels. The output
        datasets may have point coordinates reported in the world space
        or display space.
        """
        ret = self._vtk_obj.OutputCoordinateSystemDisplay()
        return ret
        

    def output_coordinate_system_world(self):
        """
        V.output_coordinate_system_world()
        C++: void OutputCoordinateSystemWorld()
        Set/get the coordinate system used for output labels. The output
        datasets may have point coordinates reported in the world space
        or display space.
        """
        ret = self._vtk_obj.OutputCoordinateSystemWorld()
        return ret
        

    _updateable_traits_ = \
    (('generate_perturbed_label_spokes',
    'GetGeneratePerturbedLabelSpokes'), ('output_traversed_bounds',
    'GetOutputTraversedBounds'), ('positions_as_normals',
    'GetPositionsAsNormals'), ('use_depth_buffer', 'GetUseDepthBuffer'),
    ('use_unicode_strings', 'GetUseUnicodeStrings'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('gravity', 'GetGravity'),
    ('iterator_type', 'GetIteratorType'), ('maximum_label_fraction',
    'GetMaximumLabelFraction'), ('output_coordinate_system',
    'GetOutputCoordinateSystem'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_perturbed_label_spokes',
    'global_warning_display', 'output_traversed_bounds',
    'positions_as_normals', 'release_data_flag', 'use_depth_buffer',
    'use_unicode_strings', 'gravity', 'iterator_type',
    'maximum_label_fraction', 'output_coordinate_system',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabelPlacer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LabelPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_perturbed_label_spokes', 'output_traversed_bounds',
            'positions_as_normals', 'use_depth_buffer', 'use_unicode_strings'],
            [], ['gravity', 'iterator_type', 'maximum_label_fraction',
            'output_coordinate_system']),
            title='Edit LabelPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabelPlacer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

