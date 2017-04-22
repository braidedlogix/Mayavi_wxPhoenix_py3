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


class MCubesReader(PolyDataAlgorithm):
    """
    MCubesReader - read binary marching cubes file
    
    Superclass: PolyDataAlgorithm
    
    MCubesReader is a source object that reads binary marching cubes
    files. (Marching cubes is an isosurfacing technique that generates
    many triangles.) The binary format is supported by W. Lorensen's
    marching cubes program (and the SliceCubes object). The format
    repeats point coordinates, so this object will merge the points with
    a Locator object. You can choose to supply the Locator or use
    the default.
    
    @warning
    Binary files assumed written in sun/hp/sgi (i.e., Big Endian) form.
    
    @warning
    Because points are merged when read, degenerate triangles may be
    removed. Thus the number of triangles read may be fewer than the
    number of triangles actually created.
    
    @warning
    The point merging does not take into account that the same point may
    have different normals. For example, running PolyDataNormals after
    ContourFilter may split triangles because of the feature_angle
    ivar. Subsequent reading with MCubesReader will merge the points
    and use the first point's normal. For the most part, this is
    undesirable.
    
    @warning
    Normals are generated from the gradient of the data scalar values.
    Hence the normals may on occasion point in a direction inconsistent
    with the ordering of the triangle vertices. If this happens, the
    resulting surface may be "black".  Reverse the sense of the
    flip_normals boolean flag to correct this.
    
    @sa
    ContourFilter MarchingCubes SliceCubes Locator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMCubesReader, obj, update, **traits)
    
    flip_normals = tvtk_base.false_bool_trait(help=\
        """
        Specify whether to flip normals in opposite direction. Flipping
        ONLY changes the direction of the normal vector. Contrast this
        with flipping in PolyDataNormals which flips both the normal
        and the cell point order.
        """
    )

    def _flip_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFlipNormals,
                        self.flip_normals_)

    normals = tvtk_base.true_bool_trait(help=\
        """
        Specify whether to read normals.
        """
    )

    def _normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormals,
                        self.normals_)

    swap_bytes = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off byte swapping.
        """
    )

    def _swap_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSwapBytes,
                        self.swap_bytes_)

    data_byte_order = traits.Trait('big_endian',
    tvtk_base.TraitRevPrefixMap({'big_endian': 0, 'little_endian': 1}), help=\
        """
        These methods should be used instead of the swap_bytes methods.
        They indicate the byte ordering of the file you are trying to
        read in. These methods will then either swap or not swap the
        bytes depending on the byte ordering of the machine it is being
        run on. For example, reading in a big_endian file on a big_endian
        machine will result in no swapping. Trying to read the same file
        on a little_endian machine will result in swapping. As a quick
        note most UNIX machines are big_endian while PC's and VAX tend to
        be little_endian. So if the file you are reading in was generated
        on a VAX or PC, set_data_byte_order_to_little_endian otherwise
        set_data_byte_order_to_big_endian.
        """
    )

    def _data_byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataByteOrder,
                        self.data_byte_order_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of marching cubes file.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    header_size = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify a header size if one exists. The header is skipped and
        not used at this time.
        """
    )

    def _header_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeaderSize,
                        self.header_size)

    limits_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set / get the file name of the marching cubes limits file.
        """
    )

    def _limits_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLimitsFileName,
                        self.limits_file_name)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set / get a spatial locator for merging points. By default, an
        instance of MergePoints is used.
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

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('flip_normals', 'GetFlipNormals'), ('normals', 'GetNormals'),
    ('swap_bytes', 'GetSwapBytes'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('data_byte_order', 'GetDataByteOrder'), ('file_name', 'GetFileName'),
    ('header_size', 'GetHeaderSize'), ('limits_file_name',
    'GetLimitsFileName'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'flip_normals', 'global_warning_display',
    'normals', 'release_data_flag', 'swap_bytes', 'data_byte_order',
    'file_name', 'header_size', 'limits_file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MCubesReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MCubesReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['flip_normals', 'normals', 'swap_bytes'], ['data_byte_order'],
            ['file_name', 'header_size', 'limits_file_name']),
            title='Edit MCubesReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MCubesReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

