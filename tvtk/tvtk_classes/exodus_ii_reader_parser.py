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

from tvtk.tvtk_classes.xml_parser import XMLParser


class ExodusIIReaderParser(XMLParser):
    """
    ExodusIIReaderParser - internal parser used by ExodusIIReader.
    
    Superclass: XMLParser
    
    ExodusIIReaderParser is an internal XML parser used by
    ExodusIIReader. This is not for public use.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExodusIIReaderParser, obj, update, **traits)
    
    def get_block_name(self, *args):
        """
        V.get_block_name(int) -> string
        C++: std::string GetBlockName(int id)
        Given a block "id" return the name as determined from the xml.
        This is valid only after Go().
        """
        ret = self._wrap_call(self._vtk_obj.GetBlockName, *args)
        return ret

    def _get_sil(self):
        return wrap_vtk(self._vtk_obj.GetSIL())
    sil = traits.Property(_get_sil, help=\
        """
        Returns the SIL. This is valid only after Go().
        """
    )

    def go(self, *args):
        """
        V.go(string)
        C++: void Go(const char *filename)
        Trigger parsing of the XML file.
        """
        ret = self._wrap_call(self._vtk_obj.Go, *args)
        return ret

    def has_information_about_block(self, *args):
        """
        V.has_information_about_block(int) -> bool
        C++: bool HasInformationAboutBlock(int id)"""
        ret = self._wrap_call(self._vtk_obj.HasInformationAboutBlock, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('encoding', 'GetEncoding'), ('file_name',
    'GetFileName'), ('ignore_character_data', 'GetIgnoreCharacterData'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'encoding', 'file_name',
    'ignore_character_data'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExodusIIReaderParser, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExodusIIReaderParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['encoding', 'file_name', 'ignore_character_data']),
            title='Edit ExodusIIReaderParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExodusIIReaderParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

