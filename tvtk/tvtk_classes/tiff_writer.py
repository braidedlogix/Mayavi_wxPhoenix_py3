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

from tvtk.tvtk_classes.image_writer import ImageWriter


class TIFFWriter(ImageWriter):
    """
    TIFFWriter - write out image data as a TIFF file
    
    Superclass: ImageWriter
    
    TIFFWriter writes image data as a TIFF data file. Data can be
    written uncompressed or compressed. Several forms of compression are
    supported including packed bits, JPEG, deflation, and LZW. (Note: LZW
    compression is currently under patent in the US and is disabled until
    the patent expires. However, the mechanism for supporting this
    compression is available for those with a valid license or to whom
    the patent does not apply.)
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTIFFWriter, obj, update, **traits)
    
    compression = traits.Trait('pack_bits',
    tvtk_base.TraitRevPrefixMap({'pack_bits': 1, 'deflate': 3, 'jpeg': 2, 'lzw': 4, 'no_compression': 0}), help=\
        """
        Set compression type. Sinze LZW compression is patented outside
        US, the additional work steps have to be taken in order to use
        that compression.
        """
    )

    def _compression_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompression,
                        self.compression_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input object from the image pipeline.
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('compression',
    'GetCompression'), ('file_dimensionality', 'GetFileDimensionality'),
    ('file_name', 'GetFileName'), ('file_pattern', 'GetFilePattern'),
    ('file_prefix', 'GetFilePrefix'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'compression', 'file_dimensionality',
    'file_name', 'file_pattern', 'file_prefix', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TIFFWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TIFFWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['compression'], ['file_dimensionality', 'file_name',
            'file_pattern', 'file_prefix']),
            title='Edit TIFFWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TIFFWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

