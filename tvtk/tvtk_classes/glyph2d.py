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

from tvtk.tvtk_classes.glyph3d import Glyph3D


class Glyph2D(Glyph3D):
    """
    Glyph2D - copy oriented and scaled glyph geometry to every input
    point (_2d specialization)
    
    Superclass: Glyph3D
    
    This subclass of Glyph3D is a specialization to 2d.
    Transformations (i.e., translation, scaling, and rotation) are
    constrained to the plane. For example, rotations due to a vector are
    computed from the x-y coordinates of the vector only, and are assumed
    to occur around the z-axis. (See Glyph3D for documentation on the
    interface to this class.)
    
    @sa
    TensorGlyph Glyph3D ProgrammableGlyphFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGlyph2D, obj, update, **traits)
    
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
    (('clamping', 'GetClamping'), ('fill_cell_data', 'GetFillCellData'),
    ('generate_point_ids', 'GetGeneratePointIds'), ('orient',
    'GetOrient'), ('scaling', 'GetScaling'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('color_mode', 'GetColorMode'),
    ('index_mode', 'GetIndexMode'), ('scale_mode', 'GetScaleMode'),
    ('vector_mode', 'GetVectorMode'), ('point_ids_name',
    'GetPointIdsName'), ('range', 'GetRange'), ('scale_factor',
    'GetScaleFactor'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamping', 'debug', 'fill_cell_data',
    'generate_point_ids', 'global_warning_display', 'orient',
    'release_data_flag', 'scaling', 'color_mode', 'index_mode',
    'scale_mode', 'vector_mode', 'point_ids_name', 'progress_text',
    'range', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Glyph2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Glyph2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clamping', 'fill_cell_data', 'generate_point_ids', 'orient',
            'scaling'], ['color_mode', 'index_mode', 'scale_mode', 'vector_mode'],
            ['point_ids_name', 'range', 'scale_factor']),
            title='Edit Glyph2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Glyph2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

