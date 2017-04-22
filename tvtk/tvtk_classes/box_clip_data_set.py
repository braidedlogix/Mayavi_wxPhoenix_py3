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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class BoxClipDataSet(UnstructuredGridAlgorithm):
    """
    BoxClipDataSet - clip an unstructured grid
    
    Superclass: UnstructuredGridAlgorithm
    
    Clipping means that is actually 'cuts' through the cells of the
    dataset, returning tetrahedral cells inside of the box. The output of
    this filter is an unstructured grid.
    
    This filter can be configured to compute a second output. The second
    output is the part of the cell that is clipped away. Set the
    generate_clipped_data boolean on if you wish to access this output
    data.
    
    The BoxClipDataSet will triangulate all types of 3d cells (i.e,
    create tetrahedra). This is necessary to preserve compatibility
    across face neighbors.
    
    To use this filter,you can decide if you will be clipping with a box
    or a hexahedral box.
    1) Set orientation if(_set_orientation(_0)): box (parallel with
       coordinate axis) set_box_clip(xmin,xmax,ymin,ymax,zmin,zmax)
       if(_set_orientation(_1)): hexahedral box (Default)
       set_box_clip(n[_0],o[_0],n[_1],o[_1],n[_2],o[_2],n[_3],o[_3],n[_4],o[_4],n[_5],o
       [5]) plane_normal[] normal of each plane plane_point[] point on the
       plane
    2) Apply the generate_clip_scalars_on()
    3) Execute clipping  Update();
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBoxClipDataSet, obj, update, **traits)
    
    generate_clip_scalars = tvtk_base.false_bool_trait(help=\
        """
        If this flag is enabled, then the output scalar values will be
        interpolated, and not the input scalar data.
        """
    )

    def _generate_clip_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateClipScalars,
                        self.generate_clip_scalars_)

    generate_clipped_output = tvtk_base.false_bool_trait(help=\
        """
        Control whether a second output is generated. The second output
        contains the polygonal data that's been clipped away.
        """
    )

    def _generate_clipped_output_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateClippedOutput,
                        self.generate_clipped_output_)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a spatial locator for merging points. By default, an
        instance of MergePoints is used.
        """
    )

    orientation = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Tells if clipping happens with a box parallel with coordinate
        axis (0) or with an hexahedral box (1). Initial value is 1.
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    def _get_clipped_output(self):
        return wrap_vtk(self._vtk_obj.GetClippedOutput())
    clipped_output = traits.Property(_get_clipped_output, help=\
        """
        Return the Clipped output.
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
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_number_of_outputs(self):
        return self._vtk_obj.GetNumberOfOutputs()
    number_of_outputs = traits.Property(_get_number_of_outputs, help=\
        """
        Return the Clipped output.
        """
    )

    def cell_grid(self, *args):
        """
        V.cell_grid(int, int, (int, ...), CellArray)
        C++: void CellGrid(IdType typeobj, IdType npts,
            const IdType *cellIds, CellArray *newCellArray)"""
        my_args = deref_array(args, [('int', 'int', ('int', Ellipsis), 'vtkCellArray')])
        ret = self._wrap_call(self._vtk_obj.CellGrid, *my_args)
        return ret

    def clip_box(self, *args):
        """
        V.clip_box(Points, GenericCell, IncrementalPointLocator,
            CellArray, PointData, PointData, CellData, int,
            CellData)
        C++: void ClipBox(Points *newPoints, GenericCell *cell,
            IncrementalPointLocator *locator, CellArray *tets,
            PointData *inPD, PointData *outPD, CellData *inCD,
            IdType cellId, CellData *outCD)"""
        my_args = deref_array(args, [('vtkPoints', 'vtkGenericCell', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.ClipBox, *my_args)
        return ret

    def clip_box0_d(self, *args):
        """
        V.clip_box0_d(GenericCell, IncrementalPointLocator,
            CellArray, PointData, PointData, CellData, int,
            CellData)
        C++: void ClipBox0D(GenericCell *cell,
            IncrementalPointLocator *locator, CellArray *verts,
            PointData *inPD, PointData *outPD, CellData *inCD,
            IdType cellId, CellData *outCD)"""
        my_args = deref_array(args, [('vtkGenericCell', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.ClipBox0D, *my_args)
        return ret

    def clip_box1d(self, *args):
        """
        V.clip_box1d(Points, GenericCell, IncrementalPointLocator,
             CellArray, PointData, PointData, CellData, int,
            CellData)
        C++: void ClipBox1D(Points *newPoints, GenericCell *cell,
            IncrementalPointLocator *locator, CellArray *lines,
            PointData *inPD, PointData *outPD, CellData *inCD,
            IdType cellId, CellData *outCD)"""
        my_args = deref_array(args, [('vtkPoints', 'vtkGenericCell', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.ClipBox1D, *my_args)
        return ret

    def clip_box2d(self, *args):
        """
        V.clip_box2d(Points, GenericCell, IncrementalPointLocator,
             CellArray, PointData, PointData, CellData, int,
            CellData)
        C++: void ClipBox2D(Points *newPoints, GenericCell *cell,
            IncrementalPointLocator *locator, CellArray *tets,
            PointData *inPD, PointData *outPD, CellData *inCD,
            IdType cellId, CellData *outCD)"""
        my_args = deref_array(args, [('vtkPoints', 'vtkGenericCell', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.ClipBox2D, *my_args)
        return ret

    def clip_hexahedron(self, *args):
        """
        V.clip_hexahedron(Points, GenericCell,
            IncrementalPointLocator, CellArray, PointData,
            PointData, CellData, int, CellData)
        C++: void ClipHexahedron(Points *newPoints,
            GenericCell *cell, IncrementalPointLocator *locator,
            CellArray *tets, PointData *inPD, PointData *outPD,
            CellData *inCD, IdType cellId, CellData *outCD)"""
        my_args = deref_array(args, [('vtkPoints', 'vtkGenericCell', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.ClipHexahedron, *my_args)
        return ret

    def clip_hexahedron0_d(self, *args):
        """
        V.clip_hexahedron0_d(GenericCell, IncrementalPointLocator,
            CellArray, PointData, PointData, CellData, int,
            CellData)
        C++: void ClipHexahedron0D(GenericCell *cell,
            IncrementalPointLocator *locator, CellArray *verts,
            PointData *inPD, PointData *outPD, CellData *inCD,
            IdType cellId, CellData *outCD)"""
        my_args = deref_array(args, [('vtkGenericCell', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.ClipHexahedron0D, *my_args)
        return ret

    def clip_hexahedron1d(self, *args):
        """
        V.clip_hexahedron1d(Points, GenericCell,
            IncrementalPointLocator, CellArray, PointData,
            PointData, CellData, int, CellData)
        C++: void ClipHexahedron1D(Points *newPoints,
            GenericCell *cell, IncrementalPointLocator *locator,
            CellArray *lines, PointData *inPD, PointData *outPD,
            CellData *inCD, IdType cellId, CellData *outCD)"""
        my_args = deref_array(args, [('vtkPoints', 'vtkGenericCell', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.ClipHexahedron1D, *my_args)
        return ret

    def clip_hexahedron2d(self, *args):
        """
        V.clip_hexahedron2d(Points, GenericCell,
            IncrementalPointLocator, CellArray, PointData,
            PointData, CellData, int, CellData)
        C++: void ClipHexahedron2D(Points *newPoints,
            GenericCell *cell, IncrementalPointLocator *locator,
            CellArray *tets, PointData *inPD, PointData *outPD,
            CellData *inCD, IdType cellId, CellData *outCD)"""
        my_args = deref_array(args, [('vtkPoints', 'vtkGenericCell', 'vtkIncrementalPointLocator', 'vtkCellArray', 'vtkPointData', 'vtkPointData', 'vtkCellData', 'int', 'vtkCellData')])
        ret = self._wrap_call(self._vtk_obj.ClipHexahedron2D, *my_args)
        return ret

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified. The locator is used to merge coincident points.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    def create_tetra(self, *args):
        """
        V.create_tetra(int, (int, ...), CellArray)
        C++: void CreateTetra(IdType npts, const IdType *cellIds,
            CellArray *newCellArray)"""
        my_args = deref_array(args, [('int', ('int', Ellipsis), 'vtkCellArray')])
        ret = self._wrap_call(self._vtk_obj.CreateTetra, *my_args)
        return ret

    def interpolate_edge(self, *args):
        """
        V.interpolate_edge(DataSetAttributes, int, int, int, float)
        C++: static void InterpolateEdge(DataSetAttributes *attributes,
             IdType toId, IdType fromId1, IdType fromId2,
            double t)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InterpolateEdge, *my_args)
        return ret

    def min_edge_f(self, *args):
        """
        V.min_edge_f((int, ...), (int, ...), [int, ...])
        C++: void MinEdgeF(const unsigned int *id_v,
            const IdType *cellIds, unsigned int *edgF)"""
        ret = self._wrap_call(self._vtk_obj.MinEdgeF, *args)
        return ret

    def pyramid_to_tetra(self, *args):
        """
        V.pyramid_to_tetra((int, ...), (int, ...), CellArray)
        C++: void PyramidToTetra(const IdType *pyramId,
            const IdType *cellIds, CellArray *newCellArray)"""
        my_args = deref_array(args, [(('int', Ellipsis), ('int', Ellipsis), 'vtkCellArray')])
        ret = self._wrap_call(self._vtk_obj.PyramidToTetra, *my_args)
        return ret

    def set_box_clip(self, *args):
        """
        V.set_box_clip(float, float, float, float, float, float)
        C++: void SetBoxClip(double xmin, double xmax, double ymin,
            double ymax, double zmin, double zmax)
        V.set_box_clip((float, ...), (float, ...), (float, ...), (float,
            ...), (float, ...), (float, ...), (float, ...), (float, ...),
            (float, ...), (float, ...), (float, ...), (float, ...))
        C++: void SetBoxClip(const double *n0, const double *o0,
            const double *n1, const double *o1, const double *n2,
            const double *o2, const double *n3, const double *o3,
            const double *n4, const double *o4, const double *n5,
            const double *o5)
        Specify the Box with which to perform the clipping. If the box is
        not parallel to axis, you need to especify normal vector of each
        plane and a point on the plane.
        """
        ret = self._wrap_call(self._vtk_obj.SetBoxClip, *args)
        return ret

    def wedge_to_tetra(self, *args):
        """
        V.wedge_to_tetra((int, ...), (int, ...), CellArray)
        C++: void WedgeToTetra(const IdType *wedgeId,
            const IdType *cellIds, CellArray *newCellArray)"""
        my_args = deref_array(args, [(('int', Ellipsis), ('int', Ellipsis), 'vtkCellArray')])
        ret = self._wrap_call(self._vtk_obj.WedgeToTetra, *my_args)
        return ret

    _updateable_traits_ = \
    (('generate_clip_scalars', 'GetGenerateClipScalars'),
    ('generate_clipped_output', 'GetGenerateClippedOutput'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('orientation',
    'GetOrientation'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_clip_scalars',
    'generate_clipped_output', 'global_warning_display',
    'release_data_flag', 'orientation', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BoxClipDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BoxClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_clip_scalars', 'generate_clipped_output'], [],
            ['orientation']),
            title='Edit BoxClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BoxClipDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

