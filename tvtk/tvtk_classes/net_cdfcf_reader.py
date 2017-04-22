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

from tvtk.tvtk_classes.net_cdf_reader import NetCDFReader


class NetCDFCFReader(NetCDFReader):
    """
    NetCDFCFReader - Reads net_cdf files that follow the CF convention.
    
    Superclass: NetCDFReader
    
    Details on this convention can be found at
    <http://cf-pcmdi.llnl.gov/>.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNetCDFCFReader, obj, update, **traits)
    
    spherical_coordinates = tvtk_base.true_bool_trait(help=\
        """
        If on (the default), then 3d data with latitude/longitude
        dimensions will be read in as curvilinear data shaped like
        spherical coordinates. If false, then the data will always be
        read in Cartesian coordinates.
        """
    )

    def _spherical_coordinates_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSphericalCoordinates,
                        self.spherical_coordinates_)

    output_type = traits.Trait('automatic',
    tvtk_base.TraitRevPrefixMap({'automatic': -1, 'image': 6, 'rectilinear': 3, 'structured': 2, 'unstructured': 4}), help=\
        """
        Set/get the data type of the output.  The index used is taken
        from the list of VTK data types in Type.h.  Valid types are
        VTK_IMAGE_DATA, VTK_RECTILINEAR_GRID, VTK_STRUCTURED_GRID, and
        VTK_UNSTRUCTURED_GRID.  In addition you can set the type to -1
        (the default), and this reader will pick the data type best
        suited for the dimensions being read.
        """
    )

    def _output_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputType,
                        self.output_type_)

    vertical_bias = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        The scale and bias of the vertical component of spherical
        coordinates.  It is common to write the vertical component with
        respect to something other than the center of the sphere (for
        example, the surface).  In this case, it might be necessary to
        scale and/or bias the vertical height.  The height will become
        height*scale + bias.  Keep in mind that if the positive attribute
        of the vertical dimension is down, then the height is negated. By
        default the scale is 1 and the bias is 0 (that is, no change). 
        The scaling will be adjusted if it results in invalid (negative)
        vertical values.
        """
    )

    def _vertical_bias_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalBias,
                        self.vertical_bias)

    vertical_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        The scale and bias of the vertical component of spherical
        coordinates.  It is common to write the vertical component with
        respect to something other than the center of the sphere (for
        example, the surface).  In this case, it might be necessary to
        scale and/or bias the vertical height.  The height will become
        height*scale + bias.  Keep in mind that if the positive attribute
        of the vertical dimension is down, then the height is negated. By
        default the scale is 1 and the bias is 0 (that is, no change). 
        The scaling will be adjusted if it results in invalid (negative)
        vertical values.
        """
    )

    def _vertical_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVerticalScale,
                        self.vertical_scale)

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

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: static int CanReadFile(const char *filename)
        Returns true if the given file can be read.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    _updateable_traits_ = \
    (('spherical_coordinates', 'GetSphericalCoordinates'),
    ('replace_fill_value_with_nan', 'GetReplaceFillValueWithNan'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('output_type',
    'GetOutputType'), ('vertical_bias', 'GetVerticalBias'),
    ('vertical_scale', 'GetVerticalScale'), ('file_name', 'GetFileName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'replace_fill_value_with_nan',
    'spherical_coordinates', 'output_type', 'file_name', 'progress_text',
    'vertical_bias', 'vertical_scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NetCDFCFReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit NetCDFCFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['replace_fill_value_with_nan', 'spherical_coordinates'],
            ['output_type'], ['file_name', 'vertical_bias', 'vertical_scale']),
            title='Edit NetCDFCFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NetCDFCFReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

