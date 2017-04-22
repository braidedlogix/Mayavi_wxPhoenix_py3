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


class Plot3DMetaReader(MultiBlockDataSetAlgorithm):
    """
    Plot3DMetaReader - reads meta-files points to plot3d files
    
    Superclass: MultiBlockDataSetAlgorithm
    
    The main goal of this reader is to make it easy to read plot3d files,
    specifically time series of plot3d files. plot3d files can take many
    different forms based on their content. Unfortunately, it is not a
    self-describing format therefore the user needs to pass information
    about the contents of the file to the reader. Normally, this is done
    by setting a number of member variables. The goal of this reader is
    to provide a simple format that enable the writer of the plot3d file
    to describe its settings as well as group a number of files as a time
    series. Note that for binary files, the auto-detect-format option,
    which is on by default negates the need to specify most other option.
    However, this reader is still very useful when trying to read file
    series even for binary files. The format for this meta-file is very
    simple and is based on JSON (there is no need to know anything about
    JSON to understand this format). Below is an example with comments
    (followed by //) that describe the format. Note that the plot3d file
    names are relative to the location of the meta-file unless they start
    with a leading /.
    
    
     {
     "auto-detect-format" : true // Tells the reader to try to figure out the format automatically. Only works
                                 // with binary file. This is on by default, negating the need for most other
                                 // options for binary files (format, byte-order, precision, multi-grid,
                                 // blanking, 2d).
     "format" : "binary",  // Is this a binary or ascii file, values : binary, ascii
     "byte-order" : "big", // Byte order for binary files, values : little, big (denoting little or big endian)
     "precision" : 32,     // Precision of floating point values, can be 32 or 64 (bits)
     "multi-grid" : false, // Is this a multi-grid file, values: true, false
     "language" : "C",     // Which language was this file written in, values : C, fortran. This is
                           // used to determine if an binary plot3d file contains byte counts, used by
                           // Fortran IO routines.
     "blanking" : false,   // Does this file have blanking information (iblanks), values : true, false
     "_2d" : false,         // Is this a 2d dataset, values : true, false
     "R" : 8.314,          // The value of the gas constant, default is 1.0. Set this according to the dimensions you use
     "gamma" : 1.4,        // Ratio of specific heats. Default is 1.4.
     "functions": [ 110, 200, 201 ],  // Additional derived values to calculate. This is an array of integers formatted
                                      // as [ value, value, value, ...]
     "filenames" : [     // List of xyz (geometry) and q (value) file names along with the time values.
                         // This is an array which contains items in the format:
                         // {"time" : values, "xyz" : "xyz file name", "q" : "q file name", "function" : "function file name"}
                         // Note that q and function are optional. Also, you can repeat the same file name for xyz or q
                         // if they don't change over time. The reader will not read files unnecessarily.
      { "time" : 3.5, "xyz" : "combxyz.bin", "q" : "combq.1.bin", "function" : "combf.1.bin" },
      { "time" : 4.5, "xyz" : "combxyz.bin", "q" : "combq.2.bin", "function" : "combf.2.bin" }
     ]
     }
     
    
    This reader leverages MultiBlockPLOT3DReader to do the actual
    reading so you may want to refer to the documenation of
    MultiBlockPLOT3DReader about the details of some of these
    parameters including the function numbers for derived value
    calculation.
    
    @sa
    MultiBlockPLOT3DReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlot3DMetaReader, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the meta plot3d filename. See the class documentation for
        format details.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Plot3DMetaReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Plot3DMetaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['file_name']),
            title='Edit Plot3DMetaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Plot3DMetaReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

