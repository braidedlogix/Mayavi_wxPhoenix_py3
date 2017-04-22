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

from tvtk.tvtk_classes.streamer_base import StreamerBase


class PolyDataStreamer(StreamerBase):
    """
    PolyDataStreamer - Streamer appends input pieces to the output.
    
    Superclass: StreamerBase
    
    PolyDataStreamer initiates streaming by requesting pieces from its
    single input it appends these pieces to the requested output. Note
    that since PolyDataStreamer uses an append filter, all the
    polygons generated have to be kept in memory before rendering. If
    these do not fit in the memory, it is possible to make the
    PolyDataMapper stream. Since the mapper will render each piece
    separately, all the polygons do not have to stored in
    memory.@attention The output may be slightly different if the
    pipeline does not handle ghost cells properly (i.e. you might see
    seames between the pieces).
    @sa
    AppendFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyDataStreamer, obj, update, **traits)
    
    color_by_piece = tvtk_base.false_bool_trait(help=\
        """
        By default, this option is off.  When it is on, cell scalars are
        generated based on which piece they are in.
        """
    )

    def _color_by_piece_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorByPiece,
                        self.color_by_piece_)

    number_of_stream_divisions = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        Set the number of pieces to divide the problem into.
        """
    )

    def _number_of_stream_divisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfStreamDivisions,
                        self.number_of_stream_divisions)

    _updateable_traits_ = \
    (('color_by_piece', 'GetColorByPiece'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('number_of_stream_divisions',
    'GetNumberOfStreamDivisions'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'color_by_piece', 'debug',
    'global_warning_display', 'release_data_flag',
    'number_of_stream_divisions', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolyDataStreamer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyDataStreamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['color_by_piece'], [], ['number_of_stream_divisions']),
            title='Edit PolyDataStreamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyDataStreamer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

