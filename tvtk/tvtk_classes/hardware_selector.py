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


class HardwareSelector(Object):
    """
    HardwareSelector - manager for open_gl-based selection.
    
    Superclass: Object
    
    HardwareSelector is a helper that orchestrates color buffer based
    selection. This relies on open_gl. HardwareSelector can be used to
    select visible cells or points within a given rectangle of the
    render_window. To use it, call in order:
    \li set_renderer() - to select the renderer in which we
    want to select the cells/points.
    \li set_area() - to set the rectangular region in the render window to
    select
    in.
    \li set_field_association() -  to select the attribute to select i.e.
    cells/points etc.
    \li Finally, call Select().
    Select will cause the attached Renderer to render in a special
    color mode, where each cell/point is given it own color so that later
    inspection of the Rendered Pixels can determine what cells are
    visible. Select() returns a new Selection instance with the
    cells/points selected.
    
    Limitations: Antialiasing will break this class. If your graphics
    card settings force their use this class will return invalid results.
    
    Currently only cells from poly_data_mappers can be selected from. When
    Renderer::Selector is non-null PainterPolyDataMapper uses the
    HardwareSelectionPolyDataPainter which make appropriate calls to
    begin_render_prop(), end_render_prop(), render_process_id(),
    render_attribute_id() to render colors correctly. Until alternatives to
    HardwareSelectionPolyDataPainter exist that can do a similar
    coloration of other DataSet types, only polygonal data can be
    selected. If you need to select other data types, consider using
    DataSetMapper and turning on it's pass_through_cell_ids feature, or
    using FrustumExtractor.
    
    Only Opaque geometry in Actors is selected from. Assemblies and
    LODMappers are not currently supported.
    
    During selection, visible datasets that can not be selected from are
    temporarily hidden so as not to produce invalid indices from their
    colors.
    
    @sa
    IdentColoredPainter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHardwareSelector, obj, update, **traits)
    
    area = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=int, value=(0, 0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _area_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArea,
                        self.area)

    field_association = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the field type to select. Valid values are
        \li DataObject::FIELD_ASSOCIATION_POINTS
        \li DataObject::FIELD_ASSOCIATION_CELLS
        \li DataObject::FIELD_ASSOCIATION_VERTICES
        \li DataObject::FIELD_ASSOCIATION_EDGES
        \li DataObject::FIELD_ASSOCIATION_ROWS
        Currently only FIELD_ASSOCIATION_POINTS and
        FIELD_ASSOCIATION_CELLS are supported.
        """
    )

    def _field_association_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldAssociation,
                        self.field_association)

    process_id = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Get/Set the process id. If process id < 0 (default -1), then the
        PROCESS_PASS is not rendered.
        """
    )

    def _process_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProcessID,
                        self.process_id)

    prop_color_value = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _prop_color_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPropColorValue,
                        self.prop_color_value, False)

    def _get_renderer(self):
        return wrap_vtk(self._vtk_obj.GetRenderer())
    def _set_renderer(self, arg):
        old_val = self._get_renderer()
        self._wrap_call(self._vtk_obj.SetRenderer,
                        deref_vtk(arg))
        self.trait_property_changed('renderer', old_val, arg)
    renderer = traits.Property(_get_renderer, _set_renderer, help=\
        """
        Get/Set the renderer to perform the selection on.
        """
    )

    use_process_id_from_data = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        In some parallel rendering setups, the process id for elements
        must be obtained from the data itself, rather than the rendering
        process' id. In that case, set this flag to ON (default OFF).
        """
    )

    def _use_process_id_from_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseProcessIdFromData,
                        self.use_process_id_from_data)

    def _get_current_pass(self):
        return self._vtk_obj.GetCurrentPass()
    current_pass = traits.Property(_get_current_pass, help=\
        """
        Get the current pass number.
        """
    )

    def get_prop_from_id(self, *args):
        """
        V.get_prop_from_id(int) -> Prop
        C++: Prop *GetPropFromID(int id)
        returns the prop associated with a ID. This is valid only until
        release_pix_buffers() gets called.
        """
        ret = self._wrap_call(self._vtk_obj.GetPropFromID, *args)
        return wrap_vtk(ret)

    def begin_render_prop(self):
        """
        V.begin_render_prop()
        C++: virtual void BeginRenderProp()
        Called by the mapper (vtk_hardware_selection_poly_data_painter) before
        and after rendering each prop.
        """
        ret = self._vtk_obj.BeginRenderProp()
        return ret
        

    def capture_buffers(self):
        """
        V.capture_buffers() -> bool
        C++: virtual bool CaptureBuffers()
        It is possible to use the HardwareSelector for a custom
        picking. (Look at ScenePicker). In that case instead of
        Select() on can use capture_buffers() to render the selection
        buffers and then get information about pixel locations suing
        get_pixel_information(). Use clear_buffers() to clear buffers after
        one's done with the scene. The optional final parameter max_dist
        will look for a cell within the specified number of pixels from
        display_position. When using the overload with the optional
        selected_position argument, selected_position is filled with the
        position for which the pixel_information is being returned. This
        is useful when max_dist > 0 to determine which position's pixel
        information is was returned.
        """
        ret = self._vtk_obj.CaptureBuffers()
        return ret
        

    def clear_buffers(self):
        """
        V.clear_buffers()
        C++: void ClearBuffers()
        It is possible to use the HardwareSelector for a custom
        picking. (Look at ScenePicker). In that case instead of
        Select() on can use capture_buffers() to render the selection
        buffers and then get information about pixel locations suing
        get_pixel_information(). Use clear_buffers() to clear buffers after
        one's done with the scene. The optional final parameter max_dist
        will look for a cell within the specified number of pixels from
        display_position. When using the overload with the optional
        selected_position argument, selected_position is filled with the
        position for which the pixel_information is being returned. This
        is useful when max_dist > 0 to determine which position's pixel
        information is was returned.
        """
        ret = self._vtk_obj.ClearBuffers()
        return ret
        

    def convert(self, *args):
        """
        V.convert(int, [float, float, float])
        C++: static void Convert(int id, float tcoord[3])"""
        ret = self._wrap_call(self._vtk_obj.Convert, *args)
        return ret

    def end_render_prop(self):
        """
        V.end_render_prop()
        C++: virtual void EndRenderProp()
        Called by the mapper (vtk_hardware_selection_poly_data_painter) before
        and after rendering each prop.
        """
        ret = self._vtk_obj.EndRenderProp()
        return ret
        

    def generate_polygon_selection(self, *args):
        """
        V.generate_polygon_selection([int, ...], int) -> Selection
        C++: virtual Selection *GeneratePolygonSelection(
            int *polygonPoints, IdType count)
        Generates the Selection from pixel buffers. Same as
        generate_selection, except this one use a polygon, instead of a
        rectangle region, and select elements inside the polygon. NOTE:
        The capture_buffers() needs to be called first.
        """
        ret = self._wrap_call(self._vtk_obj.GeneratePolygonSelection, *args)
        return wrap_vtk(ret)

    def generate_selection(self, *args):
        """
        V.generate_selection() -> Selection
        C++: virtual Selection *GenerateSelection()
        V.generate_selection([int, int, int, int]) -> Selection
        C++: virtual Selection *GenerateSelection(unsigned int r[4])
        V.generate_selection(int, int, int, int) -> Selection
        C++: virtual Selection *GenerateSelection(unsigned int x1,
            unsigned int y1, unsigned int x2, unsigned int y2)
        Generates the Selection from pixel buffers. Requires that
        capture_buffers() has already been called. Optionally you may pass
        a screen region (xmin, ymin, xmax, ymax) to generate a selection
        from. The region must be a subregion of the region specified by
        set_area(), otherwise it will be clipped to that region.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateSelection, *args)
        return wrap_vtk(ret)

    def pass_type_to_string(self, *args):
        """
        V.pass_type_to_string(PassTypes) -> string
        C++: std::string PassTypeToString(PassTypes type)
        Convert a pass_types enum value to a human readable string.
        """
        ret = self._wrap_call(self._vtk_obj.PassTypeToString, *args)
        return ret

    def render_attribute_id(self, *args):
        """
        V.render_attribute_id(int)
        C++: virtual void RenderAttributeId(IdType attribid)
        Called by any Mapper or Prop subclass to render an
        attribute's id.
        """
        ret = self._wrap_call(self._vtk_obj.RenderAttributeId, *args)
        return ret

    def render_composite_index(self, *args):
        """
        V.render_composite_index(int)
        C++: virtual void RenderCompositeIndex(unsigned int index)
        Called by any Mapper or Prop subclass to render a
        composite-index. Currently indices >= 0xffffff are not supported.
        """
        ret = self._wrap_call(self._vtk_obj.RenderCompositeIndex, *args)
        return ret

    def render_process_id(self, *args):
        """
        V.render_process_id(int)
        C++: virtual void RenderProcessId(unsigned int processid)
        Called by any Mapper or subclass to render process id. This
        has any effect when this->_use_process_id_from_data is true.
        """
        ret = self._wrap_call(self._vtk_obj.RenderProcessId, *args)
        return ret

    def select(self):
        """
        V.select() -> Selection
        C++: Selection *Select()
        Perform the selection. Returns  a new instance of Selection
        containing the selection on success.
        """
        ret = wrap_vtk(self._vtk_obj.Select())
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('area', 'GetArea'), ('field_association',
    'GetFieldAssociation'), ('process_id', 'GetProcessID'),
    ('prop_color_value', 'GetPropColorValue'),
    ('use_process_id_from_data', 'GetUseProcessIdFromData'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ('prop_color_value',)
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'area', 'field_association',
    'process_id', 'prop_color_value', 'use_process_id_from_data'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HardwareSelector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HardwareSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['area', 'field_association', 'process_id',
            'prop_color_value', 'use_process_id_from_data']),
            title='Edit HardwareSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HardwareSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

