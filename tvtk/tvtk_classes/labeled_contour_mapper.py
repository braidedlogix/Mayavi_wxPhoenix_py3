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

from tvtk.tvtk_classes.mapper import Mapper


class LabeledContourMapper(Mapper):
    """
    LabeledContourMapper - Draw labeled isolines.
    
    Superclass: Mapper
    
    Draw isolines with 3d inline labels.
    
    The lines in the input polydata will be drawn with labels displaying
    the scalar value.
    
    For this mapper to function properly, stenciling must be enabled in
    the render window (it is disabled by default). Otherwise the lines
    will be drawn through the labels.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabeledContourMapper, obj, update, **traits)
    
    label_visibility = tvtk_base.true_bool_trait(help=\
        """
        If true, labels will be placed and drawn during rendering.
        Otherwise, only the mapper returned by get_poly_data_mapper() will
        be rendered. The default is to draw labels.
        """
    )

    def _label_visibility_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelVisibility,
                        self.label_visibility_)

    skip_distance = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Ensure that there are at least skip_distance pixels between
        labels. This is only enforced on labels along the the same line.
        The default is 0.
        """
    )

    def _skip_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSkipDistance,
                        self.skip_distance)

    def _get_text_properties(self):
        return wrap_vtk(self._vtk_obj.GetTextProperties())
    def _set_text_properties(self, arg):
        old_val = self._get_text_properties()
        self._wrap_call(self._vtk_obj.SetTextProperties,
                        deref_vtk(arg))
        self.trait_property_changed('text_properties', old_val, arg)
    text_properties = traits.Property(_get_text_properties, _set_text_properties, help=\
        """
        The text properties used to label the lines. Note that both
        vertical and horizontal justifications will be reset to
        "Centered" prior to rendering.
        
        * If the text_property_mapping array exists, then it is used to
          identify which
        * text property to use for each label as follows: If the scalar
          value of a
        * line is found in the mapping, the index of the value in mapping
        is used to
        * lookup the text property in the collection. If there are more
          mapping
        * values than properties, the properties are looped through until
        the
        * mapping is exhausted.
        
        * Lines with scalar values missing from the mapping are assigned
          text
        * properties in a round-robin fashion starting from the beginning
        of the
        * collection, repeating from the start of the collection as
          necessary.
        * @sa set_text_property
        * @sa set_text_property_mapping
        """
    )

    def _get_text_property_mapping(self):
        return wrap_vtk(self._vtk_obj.GetTextPropertyMapping())
    def _set_text_property_mapping(self, arg):
        old_val = self._get_text_property_mapping()
        my_arg = deref_array([arg], [['vtkDoubleArray']])
        self._wrap_call(self._vtk_obj.SetTextPropertyMapping,
                        my_arg[0])
        self.trait_property_changed('text_property_mapping', old_val, arg)
    text_property_mapping = traits.Property(_get_text_property_mapping, _set_text_property_mapping, help=\
        """
        Values in this array correspond to TextProperty objects in the
        text_properties collection. If a contour line's scalar value
        exists in this array, the corresponding text property is used for
        the label. See set_text_properties for more information.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Specify the input data to map.
        """
    )

    def _get_poly_data_mapper(self):
        return wrap_vtk(self._vtk_obj.GetPolyDataMapper())
    poly_data_mapper = traits.Property(_get_poly_data_mapper, help=\
        """
        The polydata mapper used to render the contours.
        """
    )

    def set_input_data(self, *args):
        """
        V.set_input_data(PolyData)
        C++: void SetInputData(PolyData *in)
        Specify the input data to map.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    def set_text_property(self, *args):
        """
        V.set_text_property(TextProperty)
        C++: virtual void SetTextProperty(TextProperty *tprop)
        The text property used to label the lines. Note that both
        vertical and horizontal justifications will be reset to
        "Centered" prior to rendering.
        
        ote This is a convenience method that clears text_properties and
        inserts the argument as the only property in the collection.
        @sa set_text_properties
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTextProperty, *my_args)
        return ret

    _updateable_traits_ = \
    (('label_visibility', 'GetLabelVisibility'),
    ('global_immediate_mode_rendering',
    'GetGlobalImmediateModeRendering'), ('immediate_mode_rendering',
    'GetImmediateModeRendering'), ('interpolate_scalars_before_mapping',
    'GetInterpolateScalarsBeforeMapping'), ('scalar_visibility',
    'GetScalarVisibility'), ('static', 'GetStatic'),
    ('use_lookup_table_scalar_range', 'GetUseLookupTableScalarRange'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('color_mode',
    'GetColorMode'), ('resolve_coincident_topology',
    'GetResolveCoincidentTopology'), ('scalar_material_mode',
    'GetScalarMaterialMode'), ('scalar_mode', 'GetScalarMode'),
    ('skip_distance', 'GetSkipDistance'), ('field_data_tuple_id',
    'GetFieldDataTupleId'), ('force_compile_only', 'GetForceCompileOnly'),
    ('render_time', 'GetRenderTime'),
    ('resolve_coincident_topology_polygon_offset_faces',
    'GetResolveCoincidentTopologyPolygonOffsetFaces'),
    ('resolve_coincident_topology_z_shift',
    'GetResolveCoincidentTopologyZShift'), ('scalar_range',
    'GetScalarRange'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_immediate_mode_rendering',
    'global_warning_display', 'immediate_mode_rendering',
    'interpolate_scalars_before_mapping', 'label_visibility',
    'release_data_flag', 'scalar_visibility', 'static',
    'use_lookup_table_scalar_range', 'color_mode',
    'resolve_coincident_topology', 'scalar_material_mode', 'scalar_mode',
    'field_data_tuple_id', 'force_compile_only', 'progress_text',
    'render_time', 'resolve_coincident_topology_polygon_offset_faces',
    'resolve_coincident_topology_z_shift', 'scalar_range',
    'skip_distance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabeledContourMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LabeledContourMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_immediate_mode_rendering', 'immediate_mode_rendering',
            'interpolate_scalars_before_mapping', 'label_visibility',
            'scalar_visibility', 'static', 'use_lookup_table_scalar_range'],
            ['color_mode', 'resolve_coincident_topology', 'scalar_material_mode',
            'scalar_mode'], ['field_data_tuple_id', 'force_compile_only',
            'render_time', 'resolve_coincident_topology_polygon_offset_faces',
            'resolve_coincident_topology_z_shift', 'scalar_range',
            'skip_distance']),
            title='Edit LabeledContourMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabeledContourMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

