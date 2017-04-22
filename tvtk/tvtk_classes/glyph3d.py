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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class Glyph3D(PolyDataAlgorithm):
    """
    Glyph3D - copy oriented and scaled glyph geometry to every input
    point
    
    Superclass: PolyDataAlgorithm
    
    Glyph3D is a filter that copies a geometric representation (called
    a glyph) to every point in the input dataset. The glyph is defined
    with polygonal data from a source filter input. The glyph may be
    oriented along the input vectors or normals, and it may be scaled
    according to scalar data or vector magnitude. More than one glyph may
    be used by creating a table of source objects, each defining a
    different glyph. If a table of glyphs is defined, then the table can
    be indexed into by using either scalar value or vector magnitude.
    
    To use this object you'll have to provide an input dataset and a
    source to define the glyph. Then decide whether you want to scale the
    glyph and how to scale the glyph (using scalar value or vector
    magnitude). Next decide whether you want to orient the glyph, and
    whether to use the vector data or normal data to orient it. Finally,
    decide whether to use a table of glyphs, or just a single glyph. If
    you use a table of glyphs, you'll have to decide whether to index
    into it with scalar value or with vector magnitude.
    
    @warning
    The scaling of the glyphs is controlled by the scale_factor ivar
    multiplied by the scalar value at each point (if VTK_SCALE_BY_SCALAR
    is set), or multiplied by the vector magnitude (if
    VTK_SCALE_BY_VECTOR is set), Alternatively (if
    VTK_SCALE_BY_VECTORCOMPONENTS is set), the scaling may be specified
    for x,y,z using the vector components. The scale factor can be
    further controlled by enabling clamping using the Clamping ivar. If
    clamping is enabled, the scale is normalized by the Range ivar, and
    then multiplied by the scale factor. The normalization process
    includes clamping the scale value between (0,1).
    
    @warning
    Typically this object operates on input data with scalar and/or
    vector data. However, scalar and/or vector aren't necessary, and it
    can be used to copy data from a single source to each point. In this
    case the scale factor can be used to uniformly scale the glyphs.
    
    @warning
    The object uses "vector" data to scale glyphs, orient glyphs, and/or
    index into a table of glyphs. You can choose to use either the vector
    or normal data at each input point. Use the method
    set_vector_mode_to_use_vector() to use the vector input data, and
    set_vector_mode_to_use_normal() to use the normal input data.
    
    @warning
    If you do use a table of glyphs, make sure to set the Range ivar to
    make sure the index into the glyph table is computed correctly.
    
    @warning
    You can turn off scaling of the glyphs completely by using the
    Scaling ivar. You can also turn off scaling due to data (either
    vector or scalar) by using the set_scale_mode_to_data_scaling_off() method.
    
    @warning
    You can set what arrays to use for the scalars, vectors, normals, and
    color scalars by using the set_input_array_to_process methods in
    Algorithm. The first array is scalars, the next vectors, the next
    normals and finally color scalars.
    
    @sa
    TensorGlyph
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGlyph3D, obj, update, **traits)
    
    clamping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off clamping of "scalar" values to range. (Scalar value
        may be vector magnitude if scale_by_vector() is enabled.)
        """
    )

    def _clamping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClamping,
                        self.clamping_)

    fill_cell_data = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable the generation of cell data as part of the output.
        The cell data at each cell will match the point data of the input
        at the glyphed point.
        """
    )

    def _fill_cell_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFillCellData,
                        self.fill_cell_data_)

    generate_point_ids = tvtk_base.false_bool_trait(help=\
        """
        Enable/disable the generation of point ids as part of the output.
        The point ids are the id of the input generating point. The point
        ids are stored in the output point field data and named
        "_input_point_ids". Point generation is useful for debugging and
        pick operations.
        """
    )

    def _generate_point_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePointIds,
                        self.generate_point_ids_)

    orient = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off orienting of input geometry along vector/normal.
        """
    )

    def _orient_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrient,
                        self.orient_)

    scaling = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off scaling of source geometry.
        """
    )

    def _scaling_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaling,
                        self.scaling_)

    color_mode = traits.Trait('color_by_scale',
    tvtk_base.TraitRevPrefixMap({'color_by_scale': 0, 'color_by_scalar': 1, 'color_by_vector': 2}), help=\
        """
        Either color by scale, scalar or by vector/normal magnitude.
        """
    )

    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    index_mode = traits.Trait('off',
    tvtk_base.TraitRevPrefixMap({'off': 0, 'scalar': 1, 'vector': 2}), help=\
        """
        Index into table of sources by scalar, by vector/normal
        magnitude, or no indexing. If indexing is turned off, then the
        first source glyph in the table of glyphs is used. Note that
        indexing mode will only use the input_scalars_selection array and
        not the input_color_scalars_selection as the scalar source if an
        array is specified.
        """
    )

    def _index_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIndexMode,
                        self.index_mode_)

    scale_mode = traits.Trait('scale_by_scalar',
    tvtk_base.TraitRevPrefixMap({'scale_by_scalar': 0, 'data_scaling_off': 3, 'scale_by_vector': 1, 'scale_by_vector_components': 2}), help=\
        """
        Either scale by scalar or by vector/normal magnitude.
        """
    )

    def _scale_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleMode,
                        self.scale_mode_)

    vector_mode = traits.Trait('use_vector',
    tvtk_base.TraitRevPrefixMap({'use_vector': 0, 'use_normal': 1, 'vector_rotation_off': 2}), help=\
        """
        Specify whether to use vector or normal to perform vector
        operations.
        """
    )

    def _vector_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorMode,
                        self.vector_mode_)

    point_ids_name = traits.String('InputPointIds', enter_set=True, auto_set=False, help=\
        """
        Set/Get the name of the point_ids array if generated. By default
        the Ids are named "_input_point_ids", but this can be changed with
        this function.
        """
    )

    def _point_ids_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPointIdsName,
                        self.point_ids_name)

    range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 1.0), cols=2, help=\
        """
        
        """
    )

    def _range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRange,
                        self.range)

    scale_factor = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify scale factor to scale object by.
        """
    )

    def _scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScaleFactor,
                        self.scale_factor)

    def _get_source_transform(self):
        return wrap_vtk(self._vtk_obj.GetSourceTransform())
    def _set_source_transform(self, arg):
        old_val = self._get_source_transform()
        self._wrap_call(self._vtk_obj.SetSourceTransform,
                        deref_vtk(arg))
        self.trait_property_changed('source_transform', old_val, arg)
    source_transform = traits.Property(_get_source_transform, _set_source_transform, help=\
        """
        When set, this is use to transform the source polydata before
        using it to generate the glyph. This is useful if one wanted to
        reorient the source, for example.
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def get_source(self, *args):
        """
        V.get_source(int) -> PolyData
        C++: PolyData *GetSource(int id=0)
        Get a pointer to a source object at a specified table location.
        """
        ret = self._wrap_call(self._vtk_obj.GetSource, *args)
        return wrap_vtk(ret)

    def is_point_visible(self, *args):
        """
        V.is_point_visible(DataSet, int) -> int
        C++: virtual int IsPointVisible(DataSet *, IdType)
        This can be overwritten by subclass to return 0 when a point is
        blanked. Default implementation is to always return 1;
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsPointVisible, *my_args)
        return ret

    def set_source_connection(self, *args):
        """
        V.set_source_connection(int, AlgorithmOutput)
        C++: void SetSourceConnection(int id,
            AlgorithmOutput *algOutput)
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify a source object at a specified table location. New style.
        Source connection is stored in port 1. This method is equivalent
        to set_input_connection(_1, id, output_port).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(PolyData)
        C++: void SetSourceData(PolyData *pd)
        V.set_source_data(int, PolyData)
        C++: void SetSourceData(int id, PolyData *pd)
        Set the source to use for the glyph. Note that this method does
        not connect the pipeline. The algorithm will work on the input
        data as it is without updating the producer of the data. See
        set_source_connection for connecting the pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('clamping', 'GetClamping'), ('fill_cell_data', 'GetFillCellData'),
    ('generate_point_ids', 'GetGeneratePointIds'), ('orient',
    'GetOrient'), ('scaling', 'GetScaling'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('color_mode', 'GetColorMode'),
    ('index_mode', 'GetIndexMode'), ('scale_mode', 'GetScaleMode'),
    ('vector_mode', 'GetVectorMode'), ('point_ids_name',
    'GetPointIdsName'), ('range', 'GetRange'), ('scale_factor',
    'GetScaleFactor'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamping', 'debug', 'fill_cell_data',
    'generate_point_ids', 'global_warning_display', 'orient',
    'release_data_flag', 'scaling', 'color_mode', 'index_mode',
    'scale_mode', 'vector_mode', 'point_ids_name', 'progress_text',
    'range', 'scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Glyph3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Glyph3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clamping', 'fill_cell_data', 'generate_point_ids', 'orient',
            'scaling'], ['color_mode', 'index_mode', 'scale_mode', 'vector_mode'],
            ['point_ids_name', 'range', 'scale_factor']),
            title='Edit Glyph3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Glyph3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

