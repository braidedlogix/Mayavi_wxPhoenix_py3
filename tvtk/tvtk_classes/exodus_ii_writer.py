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

from tvtk.tvtk_classes.writer import Writer


class ExodusIIWriter(Writer):
    """
    ExodusIIWriter - Write Exodus II files
    
    Superclass: Writer
    
    This is a Writer that writes it's UnstructuredGrid
        input out to an Exodus II file.  Go to
    http://endo.sandia.gov/SEACAS/
        for more information about the Exodus II format.
    
    
        Exodus files contain much information that is not captured
        in a UnstructuredGrid, such as time steps, information
        lines, node sets, and side sets.  This information can be
        stored in a ModelMetadata object.
    
    
        The ExodusReader and PExodusReader can create
        a ModelMetadata object and embed it in a UnstructuredGrid
        in a series of field arrays.  This writer searches for these
        field arrays and will use the metadata contained in them
        when creating the new Exodus II file.
    
    
        You can also explicitly give the ExodusIIWriter a
        ModelMetadata object to use when writing the file.
    
    
        In the absence of the information provided by ModelMetadata,
        if this writer is not part of a parallel application, we will use
        reasonable defaults for all the values in the output Exodus file.
        If you don't provide a block ID element array, we'll create a
        block for each cell type that appears in the unstructured grid.
    
    
        However if this writer is part of a parallel application (hence
        writing out a distributed Exodus file), then we need at the very
        least a list of all the block IDs that appear in the file.  And
        we need the element array of block IDs for the input unstructured
    grid.
    
    
        In the absence of a ModelMetadata object, you can also provide
        time step information which we will include in the output Exodus
        file.
    
    @warning
        If the input floating point field arrays and point locations are
    all
        floats or all doubles, this class will operate more efficiently.
        Mixing floats and doubles will slow you down, because Exodus II
        requires that we write only floats or only doubles.
    
    @warning
        We use the terms "point" and "node" interchangeably.
        Also, we use the terms "element" and "cell" interchangeably.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkExodusIIWriter, obj, update, **traits)
    
    write_all_time_steps = tvtk_base.false_bool_trait(help=\
        """
        When write_all_time_steps is turned ON, the writer is executed once
        for each timestep available from the reader.
        """
    )

    def _write_all_time_steps_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteAllTimeSteps,
                        self.write_all_time_steps_)

    write_out_block_id_array = tvtk_base.false_bool_trait(help=\
        """
        By default, the integer array containing the global Block Ids of
        the cells is not included when the new Exodus II file is written
        out.  If you do want to include this array, set
        write_out_block_id_array to ON.
        """
    )

    def _write_out_block_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteOutBlockIdArray,
                        self.write_out_block_id_array_)

    write_out_global_element_id_array = tvtk_base.false_bool_trait(help=\
        """
        By default, the integer array containing the global Element Ids
        is not included when the new Exodus II file is written out.  If
        you do want to include this array, set
        write_out_global_element_id_array to ON.
        """
    )

    def _write_out_global_element_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteOutGlobalElementIdArray,
                        self.write_out_global_element_id_array_)

    write_out_global_node_id_array = tvtk_base.false_bool_trait(help=\
        """
        By default, the integer array containing the global Node Ids is
        not included when the new Exodus II file is written out.  If you
        do want to include this array, set write_out_global_node_id_array to
        ON.
        """
    )

    def _write_out_global_node_id_array_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteOutGlobalNodeIdArray,
                        self.write_out_global_node_id_array_)

    block_id_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _block_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlockIdArrayName,
                        self.block_id_array_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Name for the output file.  If writing in parallel, the number of
        processes and the process rank will be appended to the name, so
        each process is writing out a separate file. If not set, this
        class will make up a file name.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    ghost_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        We never write out ghost cells.  This variable is here to satisfy
        the behavior of para_view on invoking a parallel writer.
        """
    )

    def _ghost_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGhostLevel,
                        self.ghost_level)

    def _get_model_metadata(self):
        return wrap_vtk(self._vtk_obj.GetModelMetadata())
    def _set_model_metadata(self, arg):
        old_val = self._get_model_metadata()
        self._wrap_call(self._vtk_obj.SetModelMetadata,
                        deref_vtk(arg))
        self.trait_property_changed('model_metadata', old_val, arg)
    model_metadata = traits.Property(_get_model_metadata, _set_model_metadata, help=\
        """
        
        """
    )

    store_doubles = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        If store_doubles is ON, the floating point fields in the Exodus
        file will be double precision fields.  The default is determined
        by the max precision of the input.  If the field data appears to
        be doubles, then store_doubles will be ON, otherwise store_doubles
        will be OFF.
        """
    )

    def _store_doubles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStoreDoubles,
                        self.store_doubles)

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

    _updateable_traits_ = \
    (('write_all_time_steps', 'GetWriteAllTimeSteps'),
    ('write_out_block_id_array', 'GetWriteOutBlockIdArray'),
    ('write_out_global_element_id_array',
    'GetWriteOutGlobalElementIdArray'), ('write_out_global_node_id_array',
    'GetWriteOutGlobalNodeIdArray'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('block_id_array_name', 'GetBlockIdArrayName'), ('file_name',
    'GetFileName'), ('ghost_level', 'GetGhostLevel'), ('store_doubles',
    'GetStoreDoubles'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_all_time_steps',
    'write_out_block_id_array', 'write_out_global_element_id_array',
    'write_out_global_node_id_array', 'block_id_array_name', 'file_name',
    'ghost_level', 'progress_text', 'store_doubles'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ExodusIIWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ExodusIIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['write_all_time_steps', 'write_out_block_id_array',
            'write_out_global_element_id_array',
            'write_out_global_node_id_array'], [], ['block_id_array_name',
            'file_name', 'ghost_level', 'store_doubles']),
            title='Edit ExodusIIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ExodusIIWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

