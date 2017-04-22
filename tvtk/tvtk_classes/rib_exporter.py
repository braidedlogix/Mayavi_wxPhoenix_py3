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


class RIBExporter(Exporter):
    """
    RIBExporter - export a scene into render_man RIB format.
    
    Superclass: Exporter
    
    RIBExporter is a concrete subclass of Exporter that writes a
    Renderman .RIB files. The input specifies a RenderWindow. All
    visible actors and lights will be included in the rib file. The
    following file naming conventions apply:
      rib file - file_prefix.rib
      image file created by render_man - file_prefix.tif
      texture files - texture_prefix__0x_addr__mtime.tif This object does NOT
    generate an image file. The user must run either render_man or a
    render_man emulator like Blue Moon Ray Tracer (BMRT). vtk properties
    are convert to Renderman shaders as follows:
      Normal property, no texture map - plastic.sl
      Normal property with texture map - txtplastic.sl These two shaders
    must be compiled by the rendering package being used.  RIBExporter
    also supports custom shaders. The shaders are written using the
    Renderman Shading Language. See "The Renderman Companion", ISBN
    0-201-50868, 1989 for details on writing shaders. RIBProperty
    specifies the declarations and parameter settings for custom shaders.
    Tcl Example: generate a rib file for the current rendering.
    RIBExporter my_rib
      my_rib set_input $ren_win
      my_rib set_file_prefix mine
      my_rib Write This will create a file mine.rib. After running this
    file through a Renderman renderer a file mine.tif will contain the
    rendered image.
    
    @sa
    Exporter RIBProperty RIBLight
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRIBExporter, obj, update, **traits)
    
    background = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the background flag. Default is 0 (off). If set, the rib
        file will contain an image shader that will use the renderer
        window's background color. Normally, render_man does generate
        backgrounds. Backgrounds are composited into the scene with the
        tiffcomp program that comes with Pixar's render_man Toolkit.  In fact,
        Pixar's Renderman will accept an image shader but only sets the
        alpha of the background. Images created this way will still have
        a black background but contain an alpha of 1 at all pixels and
        CANNOT be subsequently composited with other images using
        tiffcomp.  However, other render_man compliant renderers like Blue
        Moon Ray Tracing (BMRT) do allow image shaders and properly set
        the background color. If this sounds too confusing, use the
        following rules: If you are using Pixar's Renderman, leave the
        Background off. Otherwise, try setting back_ground_on and see if
        you get the desired results.
        """
    )

    def _background_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackground,
                        self.background_)

    export_arrays = tvtk_base.false_bool_trait(help=\
        """
        Set or get the export_arrays. If export_arrays is set, then all
        point data, field data, and cell data arrays will get exported
        together with polygons. Default is Off (0).
        """
    )

    def _export_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExportArrays,
                        self.export_arrays_)

    file_prefix = tvtk_base.vtk_file_prefix("", help=\
        """
        Specify the prefix of the files to write out. The resulting file
        names will have .rib appended to them.
        """
    )

    def _file_prefix_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePrefix,
                        self.file_prefix)

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

    pixel_samples = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(2, 2), cols=2, help=\
        """
        
        """
    )

    def _pixel_samples_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPixelSamples,
                        self.pixel_samples)

    size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(-1, -1), cols=2, help=\
        """
        
        """
    )

    def _size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSize,
                        self.size)

    texture_prefix = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the prefix of any generated texture files.
        """
    )

    def _texture_prefix_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTexturePrefix,
                        self.texture_prefix)

    def _get_export_arrays_max_value(self):
        return self._vtk_obj.GetExportArraysMaxValue()
    export_arrays_max_value = traits.Property(_get_export_arrays_max_value, help=\
        """
        Set or get the export_arrays. If export_arrays is set, then all
        point data, field data, and cell data arrays will get exported
        together with polygons. Default is Off (0).
        """
    )

    def _get_export_arrays_min_value(self):
        return self._vtk_obj.GetExportArraysMinValue()
    export_arrays_min_value = traits.Property(_get_export_arrays_min_value, help=\
        """
        Set or get the export_arrays. If export_arrays is set, then all
        point data, field data, and cell data arrays will get exported
        together with polygons. Default is Off (0).
        """
    )

    _updateable_traits_ = \
    (('background', 'GetBackground'), ('export_arrays',
    'GetExportArrays'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_prefix', 'GetFilePrefix'),
    ('pixel_samples', 'GetPixelSamples'), ('size', 'GetSize'),
    ('texture_prefix', 'GetTexturePrefix'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['background', 'debug', 'export_arrays', 'global_warning_display',
    'file_prefix', 'pixel_samples', 'size', 'texture_prefix'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RIBExporter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RIBExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['background', 'export_arrays'], [], ['file_prefix',
            'pixel_samples', 'size', 'texture_prefix']),
            title='Edit RIBExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RIBExporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

