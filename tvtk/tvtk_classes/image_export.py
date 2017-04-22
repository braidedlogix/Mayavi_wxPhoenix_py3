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


class ImageExport(ImageAlgorithm):
    """
    ImageExport - Export VTK images to third-party systems.
    
    Superclass: ImageAlgorithm
    
    ImageExport provides a way of exporting image data at the end of a
    pipeline to a third-party system or to a simple C array. Applications
    can use this to get direct access to the image data in memory.  A
    callback interface is provided to allow connection of the VTK
    pipeline to a third-party pipeline.  This interface conforms to the
    interface of ImageImport. In Python it is possible to use this
    class to write the image data into a python string that has been
    pre-allocated to be the correct size.
    @sa
    ImageImport
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageExport, obj, update, **traits)
    
    image_lower_left = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether the data goes to the exported memory starting in
        the lower left corner or upper left corner.  Default: On. When
        this flag is Off, the image will be flipped vertically before it
        is exported. WARNING: this flag is used only with the Export()
        method, it is ignored by get_pointer_to_data().
        """
    )

    def _image_lower_left_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageLowerLeft,
                        self.image_lower_left_)

    def _get_export_void_pointer(self):
        return self._vtk_obj.GetExportVoidPointer()
    def _set_export_void_pointer(self, arg):
        old_val = self._get_export_void_pointer()
        self._wrap_call(self._vtk_obj.SetExportVoidPointer,
                        arg)
        self.trait_property_changed('export_void_pointer', old_val, arg)
    export_void_pointer = traits.Property(_get_export_void_pointer, _set_export_void_pointer, help=\
        """
        Set the void pointer of the C array to export the data to. From
        python, you can specify a pointer to a string that is large
        enough to hold the data.
        """
    )

    def _get_callback_user_data(self):
        return self._vtk_obj.GetCallbackUserData()
    callback_user_data = traits.Property(_get_callback_user_data, help=\
        """
        Get the user data that should be passed to the callback
        functions.
        """
    )

    def _get_data_dimensions(self):
        return self._vtk_obj.GetDataDimensions()
    data_dimensions = traits.Property(_get_data_dimensions, help=\
        """
        Get the (x,y,z) index dimensions of the data.  Please note that C
        arrays are indexed in decreasing order, i.e. array[z][y][x].
        """
    )

    def _get_data_extent(self):
        return self._vtk_obj.GetDataExtent()
    data_extent = traits.Property(_get_data_extent, help=\
        """
        Get miscellaneous additional information about the data.
        """
    )

    def _get_data_memory_size(self):
        return self._vtk_obj.GetDataMemorySize()
    data_memory_size = traits.Property(_get_data_memory_size, help=\
        """
        Get the number of bytes required for the output C array.
        """
    )

    def _get_data_number_of_scalar_components(self):
        return self._vtk_obj.GetDataNumberOfScalarComponents()
    data_number_of_scalar_components = traits.Property(_get_data_number_of_scalar_components, help=\
        """
        Get the number of scalar components of the data.  Please note
        that when you index into a C array, the scalar component index
        comes last, i.e. array[z][y][x][c].
        """
    )

    def _get_data_origin(self):
        return self._vtk_obj.GetDataOrigin()
    data_origin = traits.Property(_get_data_origin, help=\
        """
        Get miscellaneous additional information about the data.
        """
    )

    def _get_data_scalar_type(self):
        return self._vtk_obj.GetDataScalarType()
    data_scalar_type = traits.Property(_get_data_scalar_type, help=\
        """
        Get the scalar type of the data.  The scalar type of the C array
        must match the scalar type of the data.
        """
    )

    def _get_data_scalar_type_as_string(self):
        return self._vtk_obj.GetDataScalarTypeAsString()
    data_scalar_type_as_string = traits.Property(_get_data_scalar_type_as_string, help=\
        """
        
        """
    )

    def _get_data_spacing(self):
        return self._vtk_obj.GetDataSpacing()
    data_spacing = traits.Property(_get_data_spacing, help=\
        """
        Get miscellaneous additional information about the data.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input object from the image pipeline.
        """
    )

    def _get_pointer_to_data(self):
        return self._vtk_obj.GetPointerToData()
    pointer_to_data = traits.Property(_get_pointer_to_data, help=\
        """
        An alternative to Export(): Use with caution.   Update the
        pipeline and return a pointer to the image memory.  The pointer
        is only valid until the next time that the pipeline is updated.
        WARNING: This method ignores the image_lower_left flag.
        """
    )

    def export(self, *args):
        """
        V.export()
        C++: void Export()
        V.export(void)
        C++: virtual void Export(void *)
        The main interface: update the pipeline and export the image to
        the memory pointed to by set_export_void_pointer().  You can also
        specify a void pointer when you call Export().
        """
        ret = self._wrap_call(self._vtk_obj.Export, *args)
        return ret

    _updateable_traits_ = \
    (('image_lower_left', 'GetImageLowerLeft'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'image_lower_left', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageExport, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageExport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['image_lower_left'], [], []),
            title='Edit ImageExport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageExport properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

