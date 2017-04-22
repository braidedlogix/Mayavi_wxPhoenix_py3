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


class VolumeOutlineSource(PolyDataAlgorithm):
    """
    VolumeOutlineSource - outline of volume cropping region
    
    Superclass: PolyDataAlgorithm
    
    VolumeOutlineSource generates a wireframe outline that corresponds
    to the cropping region of a VolumeMapper.  It requires a
    VolumeMapper as input.  The generate_faces option turns on the
    solid faces of the outline, and the generate_scalars option generates
    color scalars.  When generate_scalars is on, it is possible to set an
    "_active_plane_id" value in the range [0..6] to highlight one of the six
    cropping planes.@par Thanks: Thanks to David Gobbi for contributing
    this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVolumeOutlineSource, obj, update, **traits)
    
    generate_faces = tvtk_base.false_bool_trait(help=\
        """
        Set whether to generate polygonal faces for the output.  By
        default, only lines are generated.  The faces will form a closed,
        watertight surface.
        """
    )

    def _generate_faces_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateFaces,
                        self.generate_faces_)

    generate_outline = tvtk_base.true_bool_trait(help=\
        """
        Set whether to generate an outline wherever an input face was cut
        by a plane.  This is on by default.
        """
    )

    def _generate_outline_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateOutline,
                        self.generate_outline_)

    generate_scalars = tvtk_base.false_bool_trait(help=\
        """
        Set whether to generate color scalars for the output.  By
        default, the output has no scalars and the color must be set in
        the property of the actor.
        """
    )

    def _generate_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateScalars,
                        self.generate_scalars_)

    active_plane_color = tvtk_base.vtk_color_trait((1.0, 1.0, 0.0), help=\
        """
        
        """
    )

    def _active_plane_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActivePlaneColor,
                        self.active_plane_color, False)

    active_plane_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the active plane, e.g. to display which plane is currently
        being modified by an interaction.  Set this to -1 if there is no
        active plane. The default value is -1.
        """
    )

    def _active_plane_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetActivePlaneId,
                        self.active_plane_id)

    color = tvtk_base.vtk_color_trait((1.0, 0.0, 0.0), help=\
        """
        
        """
    )

    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, False)

    def _get_volume_mapper(self):
        return wrap_vtk(self._vtk_obj.GetVolumeMapper())
    def _set_volume_mapper(self, arg):
        old_val = self._get_volume_mapper()
        self._wrap_call(self._vtk_obj.SetVolumeMapper,
                        deref_vtk(arg))
        self.trait_property_changed('volume_mapper', old_val, arg)
    volume_mapper = traits.Property(_get_volume_mapper, _set_volume_mapper, help=\
        """
        Set the mapper that has the cropping region that the outline will
        be generated for.  The mapper must have an input, because the
        bounds of the data must be computed in order to generate the
        outline.
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
    (('generate_faces', 'GetGenerateFaces'), ('generate_outline',
    'GetGenerateOutline'), ('generate_scalars', 'GetGenerateScalars'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('active_plane_color', 'GetActivePlaneColor'), ('active_plane_id',
    'GetActivePlaneId'), ('color', 'GetColor'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_faces', 'generate_outline',
    'generate_scalars', 'global_warning_display', 'release_data_flag',
    'active_plane_color', 'active_plane_id', 'color', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VolumeOutlineSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VolumeOutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_faces', 'generate_outline', 'generate_scalars'], [],
            ['active_plane_color', 'active_plane_id', 'color']),
            title='Edit VolumeOutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VolumeOutlineSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

