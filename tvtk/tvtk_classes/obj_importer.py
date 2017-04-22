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

from tvtk.tvtk_classes.importer import Importer


class OBJImporter(Importer):
    """
    OBJImporter - import from .obj wavefront files
    
    Superclass: Importer
    
    from Wavefront .obj & associated .mtl files.@par Thanks - Peter
    Karasev (Georgia Tech / Keysight Technologies Inc),:
                      Allen Tannenbaum (SUNY Stonybrook), Patricio Vela
    (Georgia Tech)
    @sa
     Importer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOBJImporter, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the file to read.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    file_name_mtl = traits.String('', enter_set=True, auto_set=False, help=\
        """
        Specify the name of the file to read.
        """
    )

    def _file_name_mtl_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileNameMTL,
                        self.file_name_mtl)

    texture_path = traits.String('.', enter_set=True, auto_set=False, help=\
        """
        Specify the name of the file to read.
        """
    )

    def _texture_path_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTexturePath,
                        self.texture_path)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('file_name_mtl', 'GetFileNameMTL'), ('texture_path',
    'GetTexturePath'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'file_name', 'file_name_mtl',
    'texture_path'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OBJImporter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OBJImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['file_name', 'file_name_mtl', 'texture_path']),
            title='Edit OBJImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OBJImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

