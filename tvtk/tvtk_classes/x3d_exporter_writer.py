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


class X3DExporterWriter(Object):
    """
    X3DExporterWriter - x3d Exporter Writer
    
    Superclass: Object
    
    X3DExporterWriter is the definition for classes that implement a
    encoding for the x3d exporter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkX3DExporterWriter, obj, update, **traits)
    
    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Enable writing to an output_string instead of the default, a file.
        """
    )

    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    def _get_binary_output_string(self):
        return self._vtk_obj.GetBinaryOutputString()
    binary_output_string = traits.Property(_get_binary_output_string, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

    def _get_output_string(self):
        return self._vtk_obj.GetOutputString()
    output_string = traits.Property(_get_output_string, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

    def _get_output_string_length(self):
        return self._vtk_obj.GetOutputStringLength()
    output_string_length = traits.Property(_get_output_string_length, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

    def close_file(self):
        """
        V.close_file()
        C++: virtual void CloseFile()"""
        ret = self._vtk_obj.CloseFile()
        return ret
        

    def end_document(self):
        """
        V.end_document()
        C++: virtual void EndDocument()
        Ends a document and sets all necessary informations or necessary
        bytes to finish the encoding correctly
        """
        ret = self._vtk_obj.EndDocument()
        return ret
        

    def end_node(self):
        """
        V.end_node()
        C++: virtual void EndNode()
        Starts/ends a new x3d node specified via node_id. The list of
        node_ids can be found in X3DExportWriterSymbols.h. The end_node
        function closes the last open node. So there must be
        corresponding start/_end_node() calls for every node
        """
        ret = self._vtk_obj.EndNode()
        return ret
        

    def flush(self):
        """
        V.flush()
        C++: virtual void Flush()"""
        ret = self._vtk_obj.Flush()
        return ret
        

    def open_file(self, *args):
        """
        V.open_file(string) -> int
        C++: virtual int OpenFile(const char *file)
        Opens the file specified with file returns 1 if successful
        otherwise 0
        """
        ret = self._wrap_call(self._vtk_obj.OpenFile, *args)
        return ret

    def open_stream(self):
        """
        V.open_stream() -> int
        C++: virtual int OpenStream()
        Init data support to be a stream instead of a file
        """
        ret = self._vtk_obj.OpenStream()
        return ret
        

    def register_and_get_output_string(self):
        """
        V.register_and_get_output_string() -> string
        C++: char *RegisterAndGetOutputString()
        This convenience method returns the string, sets the IVAR to
        NULL, so that the user is responsible for deleting the string. I
        am not sure what the name should be, so it may change in the
        future.
        """
        ret = self._vtk_obj.RegisterAndGetOutputString()
        return ret
        

    def set_field(self, *args):
        """
        V.set_field(int, string, bool)
        C++: virtual void SetField(int attributeID, const char *value,
            bool mfstring=false)
        V.set_field(int, int)
        C++: virtual void SetField(int attributeID, int)
        V.set_field(int, float)
        C++: virtual void SetField(int attributeID, double)
        V.set_field(int, bool)
        C++: virtual void SetField(int attributeID, bool)
        V.set_field(int, int, (float, ...))
        C++: virtual void SetField(int attributeID, int type,
            const double *a)
        V.set_field(int, int, DataArray)
        C++: virtual void SetField(int attributeID, int type,
            DataArray *a)
        V.set_field(int, (float, ...), int)
        C++: virtual void SetField(int attributeID, const double *values,
            size_t size)
        V.set_field(int, (int, ...), int, bool)
        C++: virtual void SetField(int attributeID, const int *values,
            size_t size, bool image=false)
        Sets the field specified with attribute_id of the active node to
        the given value. The type of the field is SFString and MFString
        virtual void set_field(int attribute_id, const std::string &value)
        = 0;
        """
        my_args = deref_array(args, [('int', 'string', 'bool'), ('int', 'int'), ('int', 'float'), ('int', 'bool'), ('int', 'int', 'tuple'), ('int', 'int', 'vtkDataArray'), ('int', 'tuple', 'int'), ('int', ('int', Ellipsis), 'int', 'bool')])
        ret = self._wrap_call(self._vtk_obj.SetField, *my_args)
        return ret

    def start_document(self):
        """
        V.start_document()
        C++: virtual void StartDocument()
        Starts a document and sets all necessary informations, i.e. the
        header of the implemented encoding
        """
        ret = self._vtk_obj.StartDocument()
        return ret
        

    def start_node(self, *args):
        """
        V.start_node(int)
        C++: virtual void StartNode(int nodeID)
        Starts/ends a new x3d node specified via node_id. The list of
        node_ids can be found in X3DExportWriterSymbols.h. The end_node
        function closes the last open node. So there must be
        corresponding start/_end_node() calls for every node
        """
        ret = self._wrap_call(self._vtk_obj.StartNode, *args)
        return ret

    _updateable_traits_ = \
    (('write_to_output_string', 'GetWriteToOutputString'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'write_to_output_string'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(X3DExporterWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit X3DExporterWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['write_to_output_string'], [], []),
            title='Edit X3DExporterWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit X3DExporterWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

