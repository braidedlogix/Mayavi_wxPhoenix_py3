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

from tvtk.tvtk_classes.object import Object


class XMLUtilities(Object):
    """
    XMLUtilities - XML utilities.
    
    Superclass: Object
    
    XMLUtilities provides XML-related convenience functions.
    @sa
    XMLDataElement
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLUtilities, obj, update, **traits)
    
    def factor_elements(self, *args):
        """
        V.factor_elements(XMLDataElement)
        C++: static void FactorElements(XMLDataElement *tree)
        Factor and unfactor a tree. This operation looks for duplicate
        elements in the tree, and replace them with references to a pool
        of elements. Unfactoring a non-factored element is harmless.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FactorElements, *my_args)
        return ret

    def read_element_from_file(self, *args):
        """
        V.read_element_from_file(string, int) -> XMLDataElement
        C++: static XMLDataElement *ReadElementFromFile(
            const char *filename, int encoding=VTK_ENCODING_NONE)
        Read a XMLDataElement from a stream, string or file. The
        'encoding' parameter will be used to set the internal encoding of
        the attributes of the data elements created by those functions
        (conversion from the XML stream encoding to that new encoding
        will be performed automatically). If set to VTK_ENCODING_NONE,
        the encoding won't be changed and will default to the default
        XMLDataElement encoding. Return the root element on success,
        NULL otherwise. Note that you have to call Delete() on the
        element returned by that function to ensure it is freed properly.
        """
        ret = self._wrap_call(self._vtk_obj.ReadElementFromFile, *args)
        return wrap_vtk(ret)

    def read_element_from_string(self, *args):
        """
        V.read_element_from_string(string, int) -> XMLDataElement
        C++: static XMLDataElement *ReadElementFromString(
            const char *str, int encoding=VTK_ENCODING_NONE)
        Read a XMLDataElement from a stream, string or file. The
        'encoding' parameter will be used to set the internal encoding of
        the attributes of the data elements created by those functions
        (conversion from the XML stream encoding to that new encoding
        will be performed automatically). If set to VTK_ENCODING_NONE,
        the encoding won't be changed and will default to the default
        XMLDataElement encoding. Return the root element on success,
        NULL otherwise. Note that you have to call Delete() on the
        element returned by that function to ensure it is freed properly.
        """
        ret = self._wrap_call(self._vtk_obj.ReadElementFromString, *args)
        return wrap_vtk(ret)

    def un_factor_elements(self, *args):
        """
        V.un_factor_elements(XMLDataElement)
        C++: static void UnFactorElements(XMLDataElement *tree)
        Factor and unfactor a tree. This operation looks for duplicate
        elements in the tree, and replace them with references to a pool
        of elements. Unfactoring a non-factored element is harmless.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnFactorElements, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLUtilities, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit XMLUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLUtilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

