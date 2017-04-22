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

from tvtk.tvtk_classes.marching_cubes import MarchingCubes


class DiscreteMarchingCubes(MarchingCubes):
    """
    DiscreteMarchingCubes - generate object boundaries from labelled
    volumes
    
    Superclass: MarchingCubes
    
    takes as input a volume (e.g., 3d structured point set) of
    segmentation labels and generates on output one or more models
    representing the boundaries between the specified label and the
    adjacent structures.  One or more label values must be specified to
    generate the models.  The boundary positions are always defined to be
    half-way between adjacent voxels. This filter works best with
    integral scalar values. If compute_scalars is on (the default), each
    output cell will have cell data that corresponds to the scalar value
    (segmentation label) of the corresponding cube. Note that this
    differs from MarchingCubes, which stores the scalar value as point
    data. The rationale for this difference is that cell vertices may be
    shared between multiple cells. This also means that the resultant
    polydata may be non-manifold (cell faces may be coincident). To
    further process the polydata, users should either: 1) extract cells
    that have a common scalar value using Threshold, or 2) process the
    data with filters that can handle non-manifold polydata (e.g.
    WindowedSincPolyDataFilter). Also note, Normals and Gradients are
    not computed. If compute_adjacent_scalars is on (default is off), each
    output point will have point data that contains the label value of
    the neighbouring voxel. This allows to remove regions of the
    resulting PolyData that are adjacent to specific label meshes. For
    example, if the input is a label image that was created by running a
    watershed transformation on a distance map followed by masking with
    the original binary segmentation. For further details and images see
    the VTK Journal paper "Providing values of adjacent voxel with
    DiscreteMarchingCubes" by Roman Grothausmann:
    http://hdl.handle.net/10380/3559
    http://www.vtkjournal.org/browse/publication/975
    @warning
    This filter is specialized to volumes. If you are interested in
    contouring other types of data, use the general ContourFilter. If
    you want to contour an image (i.e., a volume slice), use
    MarchingSquares.
    @sa
    ContourFilter SliceCubes MarchingSquares DividingCubes
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDiscreteMarchingCubes, obj, update, **traits)
    
    compute_adjacent_scalars = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the computation of neighbouring voxel values.
        """
    )

    def _compute_adjacent_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeAdjacentScalars,
                        self.compute_adjacent_scalars_)

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
    (('compute_adjacent_scalars', 'GetComputeAdjacentScalars'),
    ('compute_gradients', 'GetComputeGradients'), ('compute_normals',
    'GetComputeNormals'), ('compute_scalars', 'GetComputeScalars'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_contours', 'GetNumberOfContours'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_adjacent_scalars', 'compute_gradients',
    'compute_normals', 'compute_scalars', 'debug',
    'global_warning_display', 'release_data_flag', 'number_of_contours',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DiscreteMarchingCubes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DiscreteMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_adjacent_scalars', 'compute_gradients',
            'compute_normals', 'compute_scalars'], [], ['number_of_contours']),
            title='Edit DiscreteMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DiscreteMarchingCubes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

