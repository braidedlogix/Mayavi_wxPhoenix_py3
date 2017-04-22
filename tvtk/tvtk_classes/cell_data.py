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

from tvtk.tvtk_classes.data_set_attributes import DataSetAttributes


class CellData(DataSetAttributes):
    """
    CellData - represent and manipulate cell attribute data
    
    Superclass: DataSetAttributes
    
    CellData is a class that is used to represent and manipulate cell
    attribute data (e.g., scalars, vectors, normals, texture coordinates,
    etc.) Special methods are provided to work with filter objects, such
    as passing data through filter, copying data from one cell to
    another, and interpolating data given cell interpolation weights.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellData, obj, update, **traits)
    
    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('copy_global_ids', 'GetCopyGlobalIds'),
    ('copy_normals', 'GetCopyNormals'), ('copy_pedigree_ids',
    'GetCopyPedigreeIds'), ('copy_scalars', 'GetCopyScalars'),
    ('copy_t_coords', 'GetCopyTCoords'), ('copy_tensors',
    'GetCopyTensors'), ('copy_vectors', 'GetCopyVectors'),
    ('number_of_tuples', 'GetNumberOfTuples'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'copy_global_ids',
    'copy_normals', 'copy_pedigree_ids', 'copy_scalars', 'copy_t_coords',
    'copy_tensors', 'copy_vectors', 'number_of_tuples'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CellData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['copy_global_ids', 'copy_normals', 'copy_pedigree_ids',
            'copy_scalars', 'copy_t_coords', 'copy_tensors', 'copy_vectors',
            'number_of_tuples']),
            title='Edit CellData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

