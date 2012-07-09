# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.poly_data_painter import PolyDataPainter


class PrimitivePainter(PolyDataPainter):
    """
    PrimitivePainter - superclass for class that handle single
    
    Superclass: PolyDataPainter
    
    This is the abstract superclass for classes that handle single type
    of primitive i.e. verts, lines, polys or tstrips. Concrete subclasses
    will pass a Render() call to the delegate painter, if any, only if it
    could not render.
    
    Thanks:
    
    Support for generic vertex attributes in VTK was contributed in
    collaboration with Stephane Ploix at EDF.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPrimitivePainter, obj, update, **traits)
    
    def _get_supported_primitive(self):
        return self._vtk_obj.GetSupportedPrimitive()
    supported_primitive = traits.Property(_get_supported_primitive, help=\
        """
        Get the type of primitive supported by this painter. This must be
        set by concrete subclasses.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('progress',
    'GetProgress'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PrimitivePainter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit PrimitivePainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit PrimitivePainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PrimitivePainter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
