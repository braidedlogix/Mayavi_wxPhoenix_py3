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

from tvtk.tvtk_classes.x3d_exporter_writer import X3DExporterWriter


class X3DExporterFIWriter(X3DExporterWriter):
    """
    X3DExporterFIWriter - 
    
    Superclass: X3DExporterWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkX3DExporterFIWriter, obj, update, **traits)
    
    fastest = tvtk_base.false_bool_trait(help=\
        """
        Use fastest instead of best compression
        """
    )

    def _fastest_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFastest,
                        self.fastest_)

    def _get_fastest_max_value(self):
        return self._vtk_obj.GetFastestMaxValue()
    fastest_max_value = traits.Property(_get_fastest_max_value, help=\
        """
        Use fastest instead of best compression
        """
    )

    def _get_fastest_min_value(self):
        return self._vtk_obj.GetFastestMinValue()
    fastest_min_value = traits.Property(_get_fastest_min_value, help=\
        """
        Use fastest instead of best compression
        """
    )

    _updateable_traits_ = \
    (('fastest', 'GetFastest'), ('write_to_output_string',
    'GetWriteToOutputString'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'fastest', 'global_warning_display',
    'write_to_output_string'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(X3DExporterFIWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit X3DExporterFIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['fastest', 'write_to_output_string'], [], []),
            title='Edit X3DExporterFIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit X3DExporterFIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

