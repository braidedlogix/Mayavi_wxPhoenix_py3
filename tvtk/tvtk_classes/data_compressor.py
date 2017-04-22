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


class DataCompressor(Object):
    """
    DataCompressor - Abstract interface for data compression classes.
    
    Superclass: Object
    
    DataCompressor provides a universal interface for data
    compression.  Subclasses provide one compression method and one
    decompression method.  The public interface to all compressors
    remains the same, and is defined by this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataCompressor, obj, update, **traits)
    
    def get_maximum_compression_space(self, *args):
        """
        V.get_maximum_compression_space(int) -> int
        C++: virtual size_t GetMaximumCompressionSpace(size_t size)
        Get the maximum space that may be needed to store data of the
        given uncompressed size after compression.  This is the minimum
        size of the output buffer that can be passed to the four-argument
        Compress method.
        """
        ret = self._wrap_call(self._vtk_obj.GetMaximumCompressionSpace, *args)
        return ret

    def compress(self, *args):
        """
        V.compress((int, ...), int, [int, ...], int) -> int
        C++: size_t Compress(unsigned char const *uncompressedData,
            size_t uncompressedSize, unsigned char *compressedData,
            size_t compressionSpace)
        V.compress((int, ...), int) -> UnsignedCharArray
        C++: UnsignedCharArray *Compress(
            unsigned char const *uncompressedData,
            size_t uncompressedSize)
        Compress the given input data buffer into the given output
        buffer.  The size of the output buffer must be at least as large
        as the value given by get_maximum_compression_space for the given
        input size.
        """
        ret = self._wrap_call(self._vtk_obj.Compress, *args)
        return wrap_vtk(ret)

    def uncompress(self, *args):
        """
        V.uncompress((int, ...), int, [int, ...], int) -> int
        C++: size_t Uncompress(unsigned char const *compressedData,
            size_t compressedSize, unsigned char *uncompressedData,
            size_t uncompressedSize)
        V.uncompress((int, ...), int, int) -> UnsignedCharArray
        C++: UnsignedCharArray *Uncompress(
            unsigned char const *compressedData, size_t compressedSize,
            size_t uncompressedSize)
        Uncompress the given input data into the given output buffer. The
        size of the uncompressed data must be known by the caller. It
        should be transmitted from the compressor by a means outside of
        this class.
        """
        ret = self._wrap_call(self._vtk_obj.Uncompress, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataCompressor, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataCompressor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit DataCompressor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataCompressor properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

