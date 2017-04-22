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

from tvtk.tvtk_classes.exporter import Exporter


class X3DExporter(Exporter):
    """
    X3DExporter - create an x3d file
    
    Superclass: Exporter
    
    X3DExporter is a render window exporter which writes out the
    renderered scene into an x3d file. x3d is an XML-based format for
    representation 3d scenes (similar to VRML). Check out
    http://www.web3d.org/x3d/ for more details.@par Thanks: x3d_exporter
    is contributed by Christophe Mouton at EDF.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkX3DExporter, obj, update, **traits)
    
    binary = tvtk_base.false_bool_trait(help=\
        """
        Turn on binary mode
        """
    )

    def _binary_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinary,
                        self.binary_)

    fastest = tvtk_base.false_bool_trait(help=\
        """
        In binary mode use fastest instead of best compression
        """
    )

    def _fastest_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFastest,
                        self.fastest_)

    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Enable writing to an output_string instead of the default, a file.
        """
    )

    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the output file name.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    def _set_input(self, arg):
        old_val = self._get_input()
        self._wrap_call(self._vtk_obj.SetInput,
                        deref_vtk(arg))
        self.trait_property_changed('input', old_val, arg)
    input = traits.Property(_get_input, _set_input, help=\
        """
        These methods are provided for backward compatibility. Will
        disappear soon.
        """
    )

    speed = traits.Float(4.0, enter_set=True, auto_set=False, help=\
        """
        Specify the Speed of navigation. Default is 4.
        """
    )

    def _speed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpeed,
                        self.speed)

    def _get_binary_max_value(self):
        return self._vtk_obj.GetBinaryMaxValue()
    binary_max_value = traits.Property(_get_binary_max_value, help=\
        """
        Turn on binary mode
        """
    )

    def _get_binary_min_value(self):
        return self._vtk_obj.GetBinaryMinValue()
    binary_min_value = traits.Property(_get_binary_min_value, help=\
        """
        Turn on binary mode
        """
    )

    def _get_binary_output_string(self):
        return self._vtk_obj.GetBinaryOutputString()
    binary_output_string = traits.Property(_get_binary_output_string, help=\
        """
        When write_to_output_string in on, then a string is allocated,
        written to, and can be retrieved with these methods.  The string
        is deleted during the next call to write ...
        """
    )

    def _get_fastest_max_value(self):
        return self._vtk_obj.GetFastestMaxValue()
    fastest_max_value = traits.Property(_get_fastest_max_value, help=\
        """
        In binary mode use fastest instead of best compression
        """
    )

    def _get_fastest_min_value(self):
        return self._vtk_obj.GetFastestMinValue()
    fastest_min_value = traits.Property(_get_fastest_min_value, help=\
        """
        In binary mode use fastest instead of best compression
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
        

    _updateable_traits_ = \
    (('binary', 'GetBinary'), ('fastest', 'GetFastest'),
    ('write_to_output_string', 'GetWriteToOutputString'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('file_name', 'GetFileName'), ('speed', 'GetSpeed'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['binary', 'debug', 'fastest', 'global_warning_display',
    'write_to_output_string', 'file_name', 'speed'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(X3DExporter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit X3DExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['binary', 'fastest', 'write_to_output_string'], [],
            ['file_name', 'speed']),
            title='Edit X3DExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit X3DExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

