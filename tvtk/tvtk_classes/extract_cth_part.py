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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class ExtractCTHPart(MultiBlockDataSetAlgorithm):
    """
    ExtractCTHPart - Generates surface of a CTH volume fraction.
    
    Superclass: MultiBlockDataSetAlgorithm
    
    ExtractCTHPart is a filter that is specialized for creating
    visualizations for a CTH simulation. CTH datasets comprise of either
    NonOverlappingAMR or a multiblock of non-overlapping rectilinear
    grids with cell-data. Certain cell-arrays in the dataset identify the
    fraction of a particular material present in a given cell. This goal
    with this filter is to extract a surface contour demarcating the
    surface where the volume fraction for a particular material is equal
    to the user chosen value.
    
    To achieve that, this filter first converts the cell-data to
    point-data and then simply apply ContourFilter filter to extract
    the contour.
    
    ExtractCTHPart also provides the user with an option to clip the
    resultant contour using a Plane. Internally, it uses
    ClipClosedSurface to clip the contour using the Plane provided.
    
    The output of this filter is a MultiBlockDataSet with one block
    corresponding to each volume-fraction array requested. Each block
    itself is a PolyData for the contour generated on the current
    process (which may be null, for processes where no contour is
    generated).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExtractCTHPart, obj, update, **traits)
    
    capping = tvtk_base.true_bool_trait(help=\
        """
        On by default, enables logic to cap the material volume.
        """
    )

    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    generate_triangles = tvtk_base.true_bool_trait(help=\
        """
        Triangulate results. When set to false, the internal cut and
        contour filters are told not to triangulate results if possible.
        true by default.
        """
    )

    def _generate_triangles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateTriangles,
                        self.generate_triangles_)

    remove_ghost_cells = tvtk_base.true_bool_trait(help=\
        """
        When set to false, the output surfaces will not hide contours
        extracted from ghost cells. This results in overlapping contours
        but overcomes holes. Default is set to true.
        """
    )

    def _remove_ghost_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRemoveGhostCells,
                        self.remove_ghost_cells_)

    def _get_clip_plane(self):
        return wrap_vtk(self._vtk_obj.GetClipPlane())
    def _set_clip_plane(self, arg):
        old_val = self._get_clip_plane()
        self._wrap_call(self._vtk_obj.SetClipPlane,
                        deref_vtk(arg))
        self.trait_property_changed('clip_plane', old_val, arg)
    clip_plane = traits.Property(_get_clip_plane, _set_clip_plane, help=\
        """
        Set, get or manipulate the implicit clipping plane.
        """
    )

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Get/Set the parallel controller. By default, the value returned
        by MultiBlockDataSetAlgorithm::GetGlobalController() when the
        object is instantiated is used.
        """
    )

    volume_fraction_surface_value = traits.Trait(0.499, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set and get the volume fraction surface value. This value should
        be between 0 and 1
        """
    )

    def _volume_fraction_surface_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVolumeFractionSurfaceValue,
                        self.volume_fraction_surface_value)

    def _get_number_of_volume_array_names(self):
        return self._vtk_obj.GetNumberOfVolumeArrayNames()
    number_of_volume_array_names = traits.Property(_get_number_of_volume_array_names, help=\
        """
        Select cell-data arrays (volume-fraction arrays) to contour with.
        """
    )

    def get_volume_array_name(self, *args):
        """
        V.get_volume_array_name(int) -> string
        C++: const char *GetVolumeArrayName(int idx)
        Select cell-data arrays (volume-fraction arrays) to contour with.
        """
        ret = self._wrap_call(self._vtk_obj.GetVolumeArrayName, *args)
        return ret

    def add_volume_array_name(self, *args):
        """
        V.add_volume_array_name(string)
        C++: void AddVolumeArrayName(const char *)
        Select cell-data arrays (volume-fraction arrays) to contour with.
        """
        ret = self._wrap_call(self._vtk_obj.AddVolumeArrayName, *args)
        return ret

    def remove_volume_array_names(self):
        """
        V.remove_volume_array_names()
        C++: void RemoveVolumeArrayNames()
        Select cell-data arrays (volume-fraction arrays) to contour with.
        """
        ret = self._vtk_obj.RemoveVolumeArrayNames()
        return ret
        

    _updateable_traits_ = \
    (('capping', 'GetCapping'), ('generate_triangles',
    'GetGenerateTriangles'), ('remove_ghost_cells',
    'GetRemoveGhostCells'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('volume_fraction_surface_value', 'GetVolumeFractionSurfaceValue'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'capping', 'debug', 'generate_triangles',
    'global_warning_display', 'release_data_flag', 'remove_ghost_cells',
    'progress_text', 'volume_fraction_surface_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExtractCTHPart, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExtractCTHPart properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['capping', 'generate_triangles', 'remove_ghost_cells'], [],
            ['volume_fraction_surface_value']),
            title='Edit ExtractCTHPart properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExtractCTHPart properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

