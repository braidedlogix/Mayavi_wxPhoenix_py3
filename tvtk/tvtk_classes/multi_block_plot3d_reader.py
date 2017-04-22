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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class MultiBlockPLOT3DReader(MultiBlockDataSetAlgorithm):
    """
    MultiBlockPLOT3DReader - read plot3d data files
    
    Superclass: MultiBlockDataSetAlgorithm
    
    MultiBlockPLOT3DReader is a reader object that reads plot3d
    formatted files and generates structured grid(s) on output. plot3d is
    a computer graphics program designed to visualize the grids and
    solutions of computational fluid dynamics. This reader also supports
    the variant of the plot3d format used by NASA's OVERFLOW CFD
    software, including full support for all Q variables. Please see the "_plot3d User's
    Manual" available from NASA Ames Research Center, Moffett Field CA.
    
    plot3d files consist of a grid file (also known as XYZ file), an
    optional solution file (also known as a Q file), and an optional
    function file that contains user created data (currently
    unsupported). The Q file contains solution  information as follows:
    the four parameters free stream mach number (Fsmach), angle of attack
    (Alpha), Reynolds number (Re), and total integration time (Time).
    This information is stored in an array called Properties in the
    field_data of each output (tuple 0: fsmach, tuple 1: alpha, tuple 2:
    re, tuple 3: time). In addition, the solution file contains the flow
    density (scalar), flow momentum (vector), and flow energy (scalar).
    
    Note that this reader does not support time series data which is
    usually stored as a series of Q and optionally XYZ files. If you want
    to read such a file series, use Plot3DMetaReader.
    
    The reader can generate additional scalars and vectors (or
    "functions") from this information. To use MultiBlockPLOT3DReader,
    you must specify the particular function number for the scalar and
    vector you want to visualize. This implementation of the reader
    provides the following functions. The scalar functions are:
    -1  - don't read or compute any scalars 100 - density 110 - pressure
       111 - pressure coefficient (requires Overflow file with Gamma) 112
    - mach number (requires Overflow file with Gamma) 113 - sounds speed
       (requires Overflow file with Gamma) 120 - temperature 130 -
       enthalpy 140 - internal energy 144 - kinetic energy 153 - velocity
    magnitude 163 - stagnation energy 170 - entropy 184 - swirl 211 -
       vorticity magnitude
    
    The vector functions are:
    -1  - don't read or compute any vectors 200 - velocity 201 -
       vorticity 202 - momentum 210 - pressure gradient. 212 - strain
       rate
    
    (Other functions are described in the plot3d spec, but only those
    listed are implemented here.) Note that by default, this reader
    creates the density scalar (100), stagnation energy (163) and
    momentum vector (202) as output. (These are just read in from the
    solution file.) Please note that the validity of computation is a
    function of this class's gas constants (R, Gamma) and the equations
    used. They may not be suitable for your computational domain.
    
    Additionally, you can read other data and associate it as a
    DataArray into the output's point attribute data. Use the method
    add_function() to list all the functions that you'd like to read.
    add_function() accepts an integer parameter that defines the function
    number.
    
    @sa
    MultiBlockDataSet StructuredGrid Plot3DMetaReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMultiBlockPLOT3DReader, obj, update, **traits)
    
    auto_detect_format = tvtk_base.false_bool_trait(help=\
        """
        When this option is turned on, the reader will try to figure out
        the values of various options such as byte order, byte count etc.
        automatically. This options works only for binary files. When it
        is turned on, the reader should be able to read most plot3d files
        automatically. The default is OFF for backwards compatibility
        reasons. For binary files, it is strongly recommended that you
        turn on auto_detect_format and leave the other file format related
        options untouched.
        """
    )

    def _auto_detect_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoDetectFormat,
                        self.auto_detect_format_)

    binary_file = tvtk_base.true_bool_trait(help=\
        """
        Is the file to be read written in binary format (as opposed to
        ascii).
        """
    )

    def _binary_file_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinaryFile,
                        self.binary_file_)

    double_precision = tvtk_base.false_bool_trait(help=\
        """
        Is this file in double precision or single precision. This only
        matters for binary files. Default is single.
        """
    )

    def _double_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDoublePrecision,
                        self.double_precision_)

    force_read = tvtk_base.false_bool_trait(help=\
        """
        Try to read a binary file even if the file length seems to be
        inconsistent with the header information. Use this with caution,
        if the file length is not the same as calculated from the header.
        either the file is corrupt or the settings are wrong.
        """
    )

    def _force_read_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForceRead,
                        self.force_read_)

    has_byte_count = tvtk_base.false_bool_trait(help=\
        """
        Were the arrays written with leading and trailing byte counts ?
        Usually, files written by a fortran program will contain these
        byte counts whereas the ones written by C/C++ won't.
        """
    )

    def _has_byte_count_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHasByteCount,
                        self.has_byte_count_)

    i_blanking = tvtk_base.false_bool_trait(help=\
        """
        Is there iblanking (point visibility) information in the file. If
        there is iblanking arrays, these will be read and assigned to the
        point_visibility array of the output.
        """
    )

    def _i_blanking_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIBlanking,
                        self.i_blanking_)

    multi_grid = tvtk_base.false_bool_trait(help=\
        """
        Does the file to be read contain information about number of
        grids. In some plot3d files, the first value contains the number
        of grids (even if there is only 1). If reading such a file, set
        this to true.
        """
    )

    def _multi_grid_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMultiGrid,
                        self.multi_grid_)

    two_dimensional_geometry = tvtk_base.false_bool_trait(help=\
        """
        If only two-dimensional data was written to the file, turn this
        on.
        """
    )

    def _two_dimensional_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTwoDimensionalGeometry,
                        self.two_dimensional_geometry_)

    byte_order = traits.Trait('big_endian',
    tvtk_base.TraitRevPrefixMap({'big_endian': 0, 'little_endian': 1}), help=\
        """
        Set the byte order of the file (remember, more Unix workstations
        write big endian whereas PCs write little endian). Default is big
        endian (since most older plot3d files were written by
        workstations).
        """
    )

    def _byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetByteOrder,
                        self.byte_order_)

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set/Get the communicator object (we'll use global World
        controller if you don't set a different one).
        """
    )

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the plot3d geometry filename.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    function_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the plot3d function filename.
        """
    )

    def _function_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFunctionFileName,
                        self.function_file_name)

    gamma = traits.Float(1.4, enter_set=True, auto_set=False, help=\
        """
        Set/Get the ratio of specific heats. Default is 1.4.
        """
    )

    def _gamma_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGamma,
                        self.gamma)

    q_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the plot3d solution filename.
        """
    )

    def _q_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQFileName,
                        self.q_file_name)

    r = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the gas constant. Default is 1.0.
        """
    )

    def _r_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetR,
                        self.r)

    scalar_function_number = traits.Int(100, enter_set=True, auto_set=False, help=\
        """
        Specify the scalar function to extract. If ==(-1), then no scalar
        function is extracted.
        """
    )

    def _scalar_function_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarFunctionNumber,
                        self.scalar_function_number)

    vector_function_number = traits.Int(202, enter_set=True, auto_set=False, help=\
        """
        Specify the vector function to extract. If ==(-1), then no vector
        function is extracted.
        """
    )

    def _vector_function_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorFunctionNumber,
                        self.vector_function_number)

    xyz_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the plot3d geometry filename.
        """
    )

    def _xyz_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXYZFileName,
                        self.xyz_file_name)

    def add_function(self, *args):
        """
        V.add_function(int)
        C++: void AddFunction(int functionNumber)
        Specify additional functions to read. These are placed into the
        point data as data arrays. Later on they can be used by labeling
        them as scalars, etc.
        """
        ret = self._wrap_call(self._vtk_obj.AddFunction, *args)
        return ret

    def can_read_binary_file(self, *args):
        """
        V.can_read_binary_file(string) -> int
        C++: virtual int CanReadBinaryFile(const char *fname)
        Return 1 if the reader can read the given file name. Only
        meaningful for binary files.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadBinaryFile, *args)
        return ret

    def remove_all_functions(self):
        """
        V.remove_all_functions()
        C++: void RemoveAllFunctions()
        Specify additional functions to read. These are placed into the
        point data as data arrays. Later on they can be used by labeling
        them as scalars, etc.
        """
        ret = self._vtk_obj.RemoveAllFunctions()
        return ret
        

    def remove_function(self, *args):
        """
        V.remove_function(int)
        C++: void RemoveFunction(int)
        Specify additional functions to read. These are placed into the
        point data as data arrays. Later on they can be used by labeling
        them as scalars, etc.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveFunction, *args)
        return ret

    _updateable_traits_ = \
    (('auto_detect_format', 'GetAutoDetectFormat'), ('binary_file',
    'GetBinaryFile'), ('double_precision', 'GetDoublePrecision'),
    ('force_read', 'GetForceRead'), ('has_byte_count', 'GetHasByteCount'),
    ('i_blanking', 'GetIBlanking'), ('multi_grid', 'GetMultiGrid'),
    ('two_dimensional_geometry', 'GetTwoDimensionalGeometry'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('byte_order',
    'GetByteOrder'), ('file_name', 'GetFileName'), ('function_file_name',
    'GetFunctionFileName'), ('gamma', 'GetGamma'), ('q_file_name',
    'GetQFileName'), ('r', 'GetR'), ('scalar_function_number',
    'GetScalarFunctionNumber'), ('vector_function_number',
    'GetVectorFunctionNumber'), ('xyz_file_name', 'GetXYZFileName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_detect_format', 'binary_file', 'debug',
    'double_precision', 'force_read', 'global_warning_display',
    'has_byte_count', 'i_blanking', 'multi_grid', 'release_data_flag',
    'two_dimensional_geometry', 'byte_order', 'file_name',
    'function_file_name', 'gamma', 'progress_text', 'q_file_name', 'r',
    'scalar_function_number', 'vector_function_number', 'xyz_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MultiBlockPLOT3DReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MultiBlockPLOT3DReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_detect_format', 'binary_file', 'double_precision',
            'force_read', 'has_byte_count', 'i_blanking', 'multi_grid',
            'two_dimensional_geometry'], ['byte_order'], ['file_name',
            'function_file_name', 'gamma', 'q_file_name', 'r',
            'scalar_function_number', 'vector_function_number', 'xyz_file_name']),
            title='Edit MultiBlockPLOT3DReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MultiBlockPLOT3DReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

