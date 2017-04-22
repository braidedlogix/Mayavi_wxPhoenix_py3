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


class RectilinearGridToTetrahedra(UnstructuredGridAlgorithm):
    """
    RectilinearGridToTetrahedra - create a Tetrahedral mesh from a
    rectilinear_grid
    
    Superclass: UnstructuredGridAlgorithm
    
    RectilinearGridToTetrahedra forms a mesh of Tetrahedra from a
    RectilinearGrid.  The tetrahedra can be 5 per cell, 6 per cell, or
    a mixture of 5 or 12 per cell. The resulting mesh is consistent,
    meaning that there are no edge crossings and that each tetrahedron
    face is shared by two tetrahedra, except those tetrahedra on the
    boundary. All tetrahedra are right handed.
    
    Note that 12 tetrahedra per cell means adding a point in the center
    of the cell.
    
    In order to subdivide some cells into 5 and some cells into 12
    tetrahedra: set_tetra_per_cell_to5_and12(); Set the Scalars of the Input
    rectilinear_grid to be 5 or 12 depending on what you want per cell of
    the rectilinear_grid.
    
    If you set remember_voxel_id, the scalars of the tetrahedron will be
    set to the Id of the Cell in the rectilinear_grid from which the
    tetrahedron came.
    
    @par Thanks:
       This class was developed by Samson J. Timoner of the
       MIT Artificial Intelligence Laboratory
    
    @sa
       Delaunay3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRectilinearGridToTetrahedra, obj, update, **traits)
    
    remember_voxel_id = tvtk_base.false_bool_trait(help=\
        """
        Should the tetrahedra have scalar data indicating which Voxel
        they came from in the RectilinearGrid?
        """
    )

    def _remember_voxel_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRememberVoxelId,
                        self.remember_voxel_id_)

    tetra_per_cell = traits.Trait('5',
    tvtk_base.TraitRevPrefixMap({'5': 5, '12': 12, '5_and12': -1, '6': 6}), help=\
        """
        Set the method to divide each cell (voxel) in the rectilinear_grid
        into tetrahedra.
        """
    )

    def _tetra_per_cell_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTetraPerCell,
                        self.tetra_per_cell_)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    
    def _set_input(self, obj):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput, deref_vtk(obj))
        self.trait_property_changed('input', old_val, obj)
    input = traits.Property(_get_input, _set_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_input(self, *args):
        """
        V.set_input((float, float, float), (float, float, float), float)
        C++: void SetInput(const double Extent[3],
            const double Spacing[3], const double tol=0.001)
        V.set_input(float, float, float, float, float, float, float)
        C++: void SetInput(const double ExtentX, const double ExtentY,
            const double ExtentZ, const double SpacingX,
            const double SpacingY, const double SpacingZ,
            const double tol=0.001)
        This function for convenience for creating a Rectilinear Grid If
        Spacing does not fit evenly into extent, the last cell will have
        a different width (or height or depth). If Extent[i]/Spacing[i]
        is within tol of an integer, then assume the programmer meant an
        integer for direction i.
        """
        ret = self._wrap_call(self._vtk_obj.SetInput, *args)
        return ret

    _updateable_traits_ = \
    (('remember_voxel_id', 'GetRememberVoxelId'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('tetra_per_cell', 'GetTetraPerCell'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'remember_voxel_id', 'tetra_per_cell',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RectilinearGridToTetrahedra, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RectilinearGridToTetrahedra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['remember_voxel_id'], ['tetra_per_cell'], []),
            title='Edit RectilinearGridToTetrahedra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RectilinearGridToTetrahedra properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

