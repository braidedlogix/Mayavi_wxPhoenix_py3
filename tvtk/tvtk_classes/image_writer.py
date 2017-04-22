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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageWriter(ImageAlgorithm):
    """
    ImageWriter - Writes images to files.
    
    Superclass: ImageAlgorithm
    
    ImageWriter writes images to files with any data type. The data
    type of the file is the same scalar type as the input.  The
    dimensionality determines whether the data will be written in one or
    multiple files. This class is used as the superclass of most image
    writing classes such as BMPWriter etc. It supports streaming.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageWriter, obj, update, **traits)
    
    file_dimensionality = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        What dimension are the files to be written. Usually this is 2, or
        3. If it is 2 and the input is a volume then the volume will be
        written as a series of 2d slices.
        """
    )

    def _file_dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileDimensionality,
                        self.file_dimensionality)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name for the image file. You should specify either a
        file_name or a file_prefix. Use file_prefix if the data is stored in
        multiple files.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    file_pattern = traits.String('%s.%d', enter_set=True, auto_set=False, help=\
        """
        The sprintf format used to build filename from file_prefix and
        number.
        """
    )

    def _file_pattern_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePattern,
                        self.file_pattern)

    file_prefix = tvtk_base.vtk_file_prefix("", help=\
        """
        Specify file prefix for the image file(s).You should specify
        either a file_name or file_prefix. Use file_prefix if the data is
        stored in multiple files.
        """
    )

    def _file_prefix_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilePrefix,
                        self.file_prefix)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input object from the image pipeline.
        """
    )

    def delete_files(self):
        """
        V.delete_files()
        C++: void DeleteFiles()"""
        ret = self._vtk_obj.DeleteFiles()
        return ret
        

    def write(self):
        """
        V.write()
        C++: virtual void Write()
        The main interface which triggers the writer to start.
        """
        ret = self._vtk_obj.Write()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('file_dimensionality', 'GetFileDimensionality'), ('file_name',
    'GetFileName'), ('file_pattern', 'GetFilePattern'), ('file_prefix',
    'GetFilePrefix'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_dimensionality', 'file_name',
    'file_pattern', 'file_prefix', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['file_dimensionality', 'file_name', 'file_pattern',
            'file_prefix']),
            title='Edit ImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

