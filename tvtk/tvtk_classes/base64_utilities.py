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


class Base64Utilities(Object):
    """
    Base64Utilities - base64 encode and decode utilities.
    
    Superclass: Object
    
    Base64Utilities implements base64 encoding and decoding.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBase64Utilities, obj, update, **traits)
    
    def decode(self, *args):
        """
        V.decode((int, ...), int, [int, ...], int) -> int
        C++: static unsigned long Decode(const unsigned char *input,
            unsigned long length, unsigned char *output,
            unsigned long max_input_length=0)
        Decode bytes from the input buffer and store the decoded stream
        into the output buffer until 'length' bytes have been decoded.
        Return the real length of the decoded stream (which should be
        equal to 'length'). Note that the output buffer must be allocated
        by the caller. If 'max_input_length' is not 0, then it specifies
        the number of encoded bytes that should be at most read from the
        input buffer. In that case the 'length' parameter is ignored.
        This enables the caller to decode a stream without actually
        knowing how much decoded data to expect (of course, the buffer
        must be large enough).\deprecated: This method can easily overrun
        its buffers, use decode_safely.
        """
        ret = self._wrap_call(self._vtk_obj.Decode, *args)
        return ret

    def decode_safely(self, *args):
        """
        V.decode_safely((int, ...), int, [int, ...], int) -> int
        C++: static size_t DecodeSafely(const unsigned char *input,
            size_t inputLen, unsigned char *output, size_t outputLen)
        Decode 4 bytes at a time from the input buffer and store the
        decoded stream into the output buffer. The required output buffer
        size must be determined and allocated by the caller. The needed
        output space is always less than the input buffer size, so a good
        first order approximation is to allocate the same size. Base64
        encoding is about 4/3 overhead, so a tighter bound is possible.
        Return the number of bytes atually placed into the output buffer.
        """
        ret = self._wrap_call(self._vtk_obj.DecodeSafely, *args)
        return ret

    def decode_triplet(self, *args):
        """
        V.decode_triplet(int, int, int, int, [int, ...], [int, ...], [int,
            ...]) -> int
        C++: static int DecodeTriplet(unsigned char i0, unsigned char i1,
            unsigned char i2, unsigned char i3, unsigned char *o0,
            unsigned char *o1, unsigned char *o2)
        Decode 4 bytes into 3 bytes. Return the number of bytes actually
        decoded (0 to 3, inclusive).
        """
        ret = self._wrap_call(self._vtk_obj.DecodeTriplet, *args)
        return ret

    def encode(self, *args):
        """
        V.encode((int, ...), int, [int, ...], int) -> int
        C++: static unsigned long Encode(const unsigned char *input,
            unsigned long length, unsigned char *output, int mark_end=0)
        Encode 'length' bytes from the input buffer and store the encoded
        stream into the output buffer. Return the length of the encoded
        stream. Note that the output buffer must be allocated by the
        caller (length * 1.5 should be a safe estimate). If 'mark_end' is
        true then an extra set of 4 bytes is added to the end of the
        stream if the input is a multiple of 3 bytes. These bytes are
        invalid chars and therefore they will stop the decoder thus
        enabling the caller to decode a stream without actually knowing
        how much data to expect (if the input is not a multiple of 3
        bytes then the extra padding needed to complete the encode 4
        bytes will stop the decoding anyway).
        """
        ret = self._wrap_call(self._vtk_obj.Encode, *args)
        return ret

    def encode_pair(self, *args):
        """
        V.encode_pair(int, int, [int, ...], [int, ...], [int, ...], [int,
            ...])
        C++: static void EncodePair(unsigned char i0, unsigned char i1,
            unsigned char *o0, unsigned char *o1, unsigned char *o2,
            unsigned char *o3)
        Encode 2 bytes into 4 bytes
        """
        ret = self._wrap_call(self._vtk_obj.EncodePair, *args)
        return ret

    def encode_single(self, *args):
        """
        V.encode_single(int, [int, ...], [int, ...], [int, ...], [int,
            ...])
        C++: static void EncodeSingle(unsigned char i0, unsigned char *o0,
             unsigned char *o1, unsigned char *o2, unsigned char *o3)
        Encode 1 byte into 4 bytes
        """
        ret = self._wrap_call(self._vtk_obj.EncodeSingle, *args)
        return ret

    def encode_triplet(self, *args):
        """
        V.encode_triplet(int, int, int, [int, ...], [int, ...], [int, ...],
             [int, ...])
        C++: static void EncodeTriplet(unsigned char i0, unsigned char i1,
             unsigned char i2, unsigned char *o0, unsigned char *o1,
            unsigned char *o2, unsigned char *o3)
        Encode 3 bytes into 4 bytes
        """
        ret = self._wrap_call(self._vtk_obj.EncodeTriplet, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Base64Utilities, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Base64Utilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Base64Utilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Base64Utilities properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

