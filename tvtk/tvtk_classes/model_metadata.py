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


class ModelMetadata(Object):
    """
    ModelMetadata - This class encapsulates the metadata
      that appear in mesh-based file formats but do not appear in
      UnstructuredGrid.
    
    Superclass: Object
    
    This class is inspired by the Exodus II file format, but
      because this class does not depend on the Exodus library, it
      should be possible to use it to represent metadata for other
      dataset file formats.  Sandia Labs uses it in their Exodus II
      reader, their Exodus II writer and their en_sight writer.
      DistributedDataFilter looks for metadata attached to
      it's input and redistributes the metadata with the grid.
    
    
      The fields in this class are those described in the document
      "EXODUS II: A Finite Element Data Model", SAND92-2137, November
    1995.
    
    
      Element and node IDs stored in this object must be global IDs,
      in the event that the original dataset was partitioned across
      many files.
    
    
      One way to initialize this object is by using ExodusModel
      (a Sandia class used by the Sandia Exodus reader).
      That class will take an open Exodus II file and a
      UnstructuredGrid drawn from it and will set the required fields.
    
    
      Alternatively, you can use all the Set*
      methods to set the individual fields. This class does not
      copy the data, it simply uses your pointer. This
      class will free the storage associated with your pointer
      when the class is deleted.  Most fields have sensible defaults.
      The only requirement is that if you are using this model_metadata
      to write out an Exodus or en_sight file in parallel, you must
      set_block_ids and set_block_id_array_name.  Your UnstructuredGrid must
      have a cell array giving the block ID for each cell.
    
    @warning
      The Exodus II library supports an optimized element order map
      (section 3.7 in the SAND document).  It contains all the element
      IDs, listed in the order in which a solver should process them.
      We don't include this, and won't unless there is a request.
    
    @warning
      There is an assumption in some classes that the name of the cell
      array containing global element ids is "_global_element_id" and the
      name of the point array containing global node ids is
    "_global_node_id".
      (element == cell) and (node == point).
    
    @sa
      DistributedDataFilter ExtractCells
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkModelMetadata, obj, update, **traits)
    
    all_variables_defined_in_all_blocks = tvtk_base.false_bool_trait(help=\
        """
        Instead of a truth table of all "1"s, you can set this instance
        variable to indicate that all variables are defined in all
        blocks.
        """
    )

    def _all_variables_defined_in_all_blocks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllVariablesDefinedInAllBlocks,
                        self.all_variables_defined_in_all_blocks_)

    def _get_block_attributes(self):
        return self._vtk_obj.GetBlockAttributes()
    def _set_block_attributes(self, arg):
        old_val = self._get_block_attributes()
        self._wrap_call(self._vtk_obj.SetBlockAttributes,
                        arg)
        self.trait_property_changed('block_attributes', old_val, arg)
    block_attributes = traits.Property(_get_block_attributes, _set_block_attributes, help=\
        """
        
        """
    )

    def _get_block_element_id_list(self):
        return self._vtk_obj.GetBlockElementIdList()
    def _set_block_element_id_list(self, arg):
        old_val = self._get_block_element_id_list()
        self._wrap_call(self._vtk_obj.SetBlockElementIdList,
                        arg)
        self.trait_property_changed('block_element_id_list', old_val, arg)
    block_element_id_list = traits.Property(_get_block_element_id_list, _set_block_element_id_list, help=\
        """
        
        """
    )

    def _get_block_ids(self):
        return self._vtk_obj.GetBlockIds()
    def _set_block_ids(self, arg):
        old_val = self._get_block_ids()
        self._wrap_call(self._vtk_obj.SetBlockIds,
                        arg)
        self.trait_property_changed('block_ids', old_val, arg)
    block_ids = traits.Property(_get_block_ids, _set_block_ids, help=\
        """
        
        """
    )

    def _get_block_nodes_per_element(self):
        return self._vtk_obj.GetBlockNodesPerElement()
    def _set_block_nodes_per_element(self, arg):
        old_val = self._get_block_nodes_per_element()
        self._wrap_call(self._vtk_obj.SetBlockNodesPerElement,
                        arg)
        self.trait_property_changed('block_nodes_per_element', old_val, arg)
    block_nodes_per_element = traits.Property(_get_block_nodes_per_element, _set_block_nodes_per_element, help=\
        """
        
        """
    )

    def _get_block_number_of_attributes_per_element(self):
        return self._vtk_obj.GetBlockNumberOfAttributesPerElement()
    def _set_block_number_of_attributes_per_element(self, arg):
        old_val = self._get_block_number_of_attributes_per_element()
        self._wrap_call(self._vtk_obj.SetBlockNumberOfAttributesPerElement,
                        arg)
        self.trait_property_changed('block_number_of_attributes_per_element', old_val, arg)
    block_number_of_attributes_per_element = traits.Property(_get_block_number_of_attributes_per_element, _set_block_number_of_attributes_per_element, help=\
        """
        
        """
    )

    def _get_block_number_of_elements(self):
        return self._vtk_obj.GetBlockNumberOfElements()
    def _set_block_number_of_elements(self, arg):
        old_val = self._get_block_number_of_elements()
        self._wrap_call(self._vtk_obj.SetBlockNumberOfElements,
                        arg)
        self.trait_property_changed('block_number_of_elements', old_val, arg)
    block_number_of_elements = traits.Property(_get_block_number_of_elements, _set_block_number_of_elements, help=\
        """
        
        """
    )

    def _get_block_property_value(self):
        return self._vtk_obj.GetBlockPropertyValue()
    def _set_block_property_value(self, arg):
        old_val = self._get_block_property_value()
        self._wrap_call(self._vtk_obj.SetBlockPropertyValue,
                        arg)
        self.trait_property_changed('block_property_value', old_val, arg)
    block_property_value = traits.Property(_get_block_property_value, _set_block_property_value, help=\
        """
        
        """
    )

    def _get_element_variable_truth_table(self):
        return self._vtk_obj.GetElementVariableTruthTable()
    def _set_element_variable_truth_table(self, arg):
        old_val = self._get_element_variable_truth_table()
        self._wrap_call(self._vtk_obj.SetElementVariableTruthTable,
                        arg)
        self.trait_property_changed('element_variable_truth_table', old_val, arg)
    element_variable_truth_table = traits.Property(_get_element_variable_truth_table, _set_element_variable_truth_table, help=\
        """
        
        """
    )

    def _get_global_variable_value(self):
        return self._vtk_obj.GetGlobalVariableValue()
    def _set_global_variable_value(self, arg):
        old_val = self._get_global_variable_value()
        self._wrap_call(self._vtk_obj.SetGlobalVariableValue,
                        arg)
        self.trait_property_changed('global_variable_value', old_val, arg)
    global_variable_value = traits.Property(_get_global_variable_value, _set_global_variable_value, help=\
        """
        
        """
    )

    def _get_node_set_distribution_factors(self):
        return self._vtk_obj.GetNodeSetDistributionFactors()
    def _set_node_set_distribution_factors(self, arg):
        old_val = self._get_node_set_distribution_factors()
        self._wrap_call(self._vtk_obj.SetNodeSetDistributionFactors,
                        arg)
        self.trait_property_changed('node_set_distribution_factors', old_val, arg)
    node_set_distribution_factors = traits.Property(_get_node_set_distribution_factors, _set_node_set_distribution_factors, help=\
        """
        
        """
    )

    def _get_node_set_ids(self):
        return self._vtk_obj.GetNodeSetIds()
    def _set_node_set_ids(self, arg):
        old_val = self._get_node_set_ids()
        self._wrap_call(self._vtk_obj.SetNodeSetIds,
                        arg)
        self.trait_property_changed('node_set_ids', old_val, arg)
    node_set_ids = traits.Property(_get_node_set_ids, _set_node_set_ids, help=\
        """
        
        """
    )

    def _get_node_set_names(self):
        return wrap_vtk(self._vtk_obj.GetNodeSetNames())
    def _set_node_set_names(self, arg):
        old_val = self._get_node_set_names()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetNodeSetNames,
                        my_arg[0])
        self.trait_property_changed('node_set_names', old_val, arg)
    node_set_names = traits.Property(_get_node_set_names, _set_node_set_names, help=\
        """
        
        """
    )

    def _get_node_set_node_id_list(self):
        return self._vtk_obj.GetNodeSetNodeIdList()
    def _set_node_set_node_id_list(self, arg):
        old_val = self._get_node_set_node_id_list()
        self._wrap_call(self._vtk_obj.SetNodeSetNodeIdList,
                        arg)
        self.trait_property_changed('node_set_node_id_list', old_val, arg)
    node_set_node_id_list = traits.Property(_get_node_set_node_id_list, _set_node_set_node_id_list, help=\
        """
        
        """
    )

    def _get_node_set_number_of_distribution_factors(self):
        return self._vtk_obj.GetNodeSetNumberOfDistributionFactors()
    def _set_node_set_number_of_distribution_factors(self, arg):
        old_val = self._get_node_set_number_of_distribution_factors()
        self._wrap_call(self._vtk_obj.SetNodeSetNumberOfDistributionFactors,
                        arg)
        self.trait_property_changed('node_set_number_of_distribution_factors', old_val, arg)
    node_set_number_of_distribution_factors = traits.Property(_get_node_set_number_of_distribution_factors, _set_node_set_number_of_distribution_factors, help=\
        """
        
        """
    )

    def _get_node_set_property_value(self):
        return self._vtk_obj.GetNodeSetPropertyValue()
    def _set_node_set_property_value(self, arg):
        old_val = self._get_node_set_property_value()
        self._wrap_call(self._vtk_obj.SetNodeSetPropertyValue,
                        arg)
        self.trait_property_changed('node_set_property_value', old_val, arg)
    node_set_property_value = traits.Property(_get_node_set_property_value, _set_node_set_property_value, help=\
        """
        
        """
    )

    def _get_node_set_size(self):
        return self._vtk_obj.GetNodeSetSize()
    def _set_node_set_size(self, arg):
        old_val = self._get_node_set_size()
        self._wrap_call(self._vtk_obj.SetNodeSetSize,
                        arg)
        self.trait_property_changed('node_set_size', old_val, arg)
    node_set_size = traits.Property(_get_node_set_size, _set_node_set_size, help=\
        """
        
        """
    )

    number_of_blocks = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The number of blocks in the file.  Set this before setting any of
        the block arrays.
        """
    )

    def _number_of_blocks_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfBlocks,
                        self.number_of_blocks)

    number_of_node_sets = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The number of node sets in the file.  Set this value before
        setting the various node set arrays.
        """
    )

    def _number_of_node_sets_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfNodeSets,
                        self.number_of_node_sets)

    number_of_side_sets = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set or get the number of side sets.  Set this value before
        setting any of the other side set arrays.
        """
    )

    def _number_of_side_sets_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSideSets,
                        self.number_of_side_sets)

    def _get_side_set_distribution_factors(self):
        return self._vtk_obj.GetSideSetDistributionFactors()
    def _set_side_set_distribution_factors(self, arg):
        old_val = self._get_side_set_distribution_factors()
        self._wrap_call(self._vtk_obj.SetSideSetDistributionFactors,
                        arg)
        self.trait_property_changed('side_set_distribution_factors', old_val, arg)
    side_set_distribution_factors = traits.Property(_get_side_set_distribution_factors, _set_side_set_distribution_factors, help=\
        """
        
        """
    )

    def _get_side_set_element_list(self):
        return self._vtk_obj.GetSideSetElementList()
    def _set_side_set_element_list(self, arg):
        old_val = self._get_side_set_element_list()
        self._wrap_call(self._vtk_obj.SetSideSetElementList,
                        arg)
        self.trait_property_changed('side_set_element_list', old_val, arg)
    side_set_element_list = traits.Property(_get_side_set_element_list, _set_side_set_element_list, help=\
        """
        
        """
    )

    def _get_side_set_ids(self):
        return self._vtk_obj.GetSideSetIds()
    def _set_side_set_ids(self, arg):
        old_val = self._get_side_set_ids()
        self._wrap_call(self._vtk_obj.SetSideSetIds,
                        arg)
        self.trait_property_changed('side_set_ids', old_val, arg)
    side_set_ids = traits.Property(_get_side_set_ids, _set_side_set_ids, help=\
        """
        
        """
    )

    def _get_side_set_names(self):
        return wrap_vtk(self._vtk_obj.GetSideSetNames())
    def _set_side_set_names(self, arg):
        old_val = self._get_side_set_names()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetSideSetNames,
                        my_arg[0])
        self.trait_property_changed('side_set_names', old_val, arg)
    side_set_names = traits.Property(_get_side_set_names, _set_side_set_names, help=\
        """
        
        """
    )

    def _get_side_set_num_df_per_side(self):
        return self._vtk_obj.GetSideSetNumDFPerSide()
    def _set_side_set_num_df_per_side(self, arg):
        old_val = self._get_side_set_num_df_per_side()
        self._wrap_call(self._vtk_obj.SetSideSetNumDFPerSide,
                        arg)
        self.trait_property_changed('side_set_num_df_per_side', old_val, arg)
    side_set_num_df_per_side = traits.Property(_get_side_set_num_df_per_side, _set_side_set_num_df_per_side, help=\
        """
        
        """
    )

    def _get_side_set_number_of_distribution_factors(self):
        return self._vtk_obj.GetSideSetNumberOfDistributionFactors()
    def _set_side_set_number_of_distribution_factors(self, arg):
        old_val = self._get_side_set_number_of_distribution_factors()
        self._wrap_call(self._vtk_obj.SetSideSetNumberOfDistributionFactors,
                        arg)
        self.trait_property_changed('side_set_number_of_distribution_factors', old_val, arg)
    side_set_number_of_distribution_factors = traits.Property(_get_side_set_number_of_distribution_factors, _set_side_set_number_of_distribution_factors, help=\
        """
        
        """
    )

    def _get_side_set_property_value(self):
        return self._vtk_obj.GetSideSetPropertyValue()
    def _set_side_set_property_value(self, arg):
        old_val = self._get_side_set_property_value()
        self._wrap_call(self._vtk_obj.SetSideSetPropertyValue,
                        arg)
        self.trait_property_changed('side_set_property_value', old_val, arg)
    side_set_property_value = traits.Property(_get_side_set_property_value, _set_side_set_property_value, help=\
        """
        
        """
    )

    def _get_side_set_side_list(self):
        return self._vtk_obj.GetSideSetSideList()
    def _set_side_set_side_list(self, arg):
        old_val = self._get_side_set_side_list()
        self._wrap_call(self._vtk_obj.SetSideSetSideList,
                        arg)
        self.trait_property_changed('side_set_side_list', old_val, arg)
    side_set_side_list = traits.Property(_get_side_set_side_list, _set_side_set_side_list, help=\
        """
        
        """
    )

    def _get_side_set_size(self):
        return self._vtk_obj.GetSideSetSize()
    def _set_side_set_size(self, arg):
        old_val = self._get_side_set_size()
        self._wrap_call(self._vtk_obj.SetSideSetSize,
                        arg)
        self.trait_property_changed('side_set_size', old_val, arg)
    side_set_size = traits.Property(_get_side_set_size, _set_side_set_size, help=\
        """
        
        """
    )

    sum_nodes_per_node_set = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the total number of nodes in all node sets
        """
    )

    def _sum_nodes_per_node_set_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSumNodesPerNodeSet,
                        self.sum_nodes_per_node_set)

    sum_sides_per_side_set = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get the total number of sides in all side sets
        """
    )

    def _sum_sides_per_side_set_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSumSidesPerSideSet,
                        self.sum_sides_per_side_set)

    time_step_index = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Set the index of the time step represented by the results data in
        the file attached to this model_metadata object.  Time step
        indices start at 0 in this file, they start at 1 in an Exodus
        file.
        """
    )

    def _time_step_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStepIndex,
                        self.time_step_index)

    title = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The title of the dataset.
        """
    )

    def _title_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTitle,
                        self.title)

    def _get_block_attributes_index(self):
        return self._vtk_obj.GetBlockAttributesIndex()
    block_attributes_index = traits.Property(_get_block_attributes_index, help=\
        """
        Get a list of the index into the block_attributes of the start of
        each block's element attribute list.
        """
    )

    def _get_block_element_id_list_index(self):
        return self._vtk_obj.GetBlockElementIdListIndex()
    block_element_id_list_index = traits.Property(_get_block_element_id_list_index, help=\
        """
        Get a list of the index into the block_element_id_list of the start
        of each block's elements.
        """
    )

    def _get_dimension(self):
        return self._vtk_obj.GetDimension()
    dimension = traits.Property(_get_dimension, help=\
        """
        Get the dimension of the model.  This is also the number of
        coordinate names.
        """
    )

    def _get_element_variable_number_of_components(self):
        return self._vtk_obj.GetElementVariableNumberOfComponents()
    element_variable_number_of_components = traits.Property(_get_element_variable_number_of_components, help=\
        """
        
        """
    )

    def _get_map_to_original_element_variable_names(self):
        return self._vtk_obj.GetMapToOriginalElementVariableNames()
    map_to_original_element_variable_names = traits.Property(_get_map_to_original_element_variable_names, help=\
        """
        
        """
    )

    def _get_map_to_original_node_variable_names(self):
        return self._vtk_obj.GetMapToOriginalNodeVariableNames()
    map_to_original_node_variable_names = traits.Property(_get_map_to_original_node_variable_names, help=\
        """
        
        """
    )

    def _get_node_set_distribution_factor_index(self):
        return self._vtk_obj.GetNodeSetDistributionFactorIndex()
    node_set_distribution_factor_index = traits.Property(_get_node_set_distribution_factor_index, help=\
        """
        Get a list of the index of the starting entry for each node set
        in the list of node set distribution factors.
        """
    )

    def _get_node_set_node_id_list_index(self):
        return self._vtk_obj.GetNodeSetNodeIdListIndex()
    node_set_node_id_list_index = traits.Property(_get_node_set_node_id_list_index, help=\
        """
        Get a list of the index of the starting entry for each node set
        in the list of node set node IDs.
        """
    )

    def _get_node_variable_number_of_components(self):
        return self._vtk_obj.GetNodeVariableNumberOfComponents()
    node_variable_number_of_components = traits.Property(_get_node_variable_number_of_components, help=\
        """
        
        """
    )

    def _get_number_of_block_properties(self):
        return self._vtk_obj.GetNumberOfBlockProperties()
    number_of_block_properties = traits.Property(_get_number_of_block_properties, help=\
        """
        The number of block properties (global variables)
        """
    )

    def _get_number_of_element_variables(self):
        return self._vtk_obj.GetNumberOfElementVariables()
    number_of_element_variables = traits.Property(_get_number_of_element_variables, help=\
        """
        
        """
    )

    def _get_number_of_global_variables(self):
        return self._vtk_obj.GetNumberOfGlobalVariables()
    number_of_global_variables = traits.Property(_get_number_of_global_variables, help=\
        """
        Get the number of global variables per time step
        """
    )

    def _get_number_of_information_lines(self):
        return self._vtk_obj.GetNumberOfInformationLines()
    number_of_information_lines = traits.Property(_get_number_of_information_lines, help=\
        """
        Get the number of information lines.
        """
    )

    def _get_number_of_node_set_properties(self):
        return self._vtk_obj.GetNumberOfNodeSetProperties()
    number_of_node_set_properties = traits.Property(_get_number_of_node_set_properties, help=\
        """
        The number of node set properties (global variables)
        """
    )

    def _get_number_of_node_variables(self):
        return self._vtk_obj.GetNumberOfNodeVariables()
    number_of_node_variables = traits.Property(_get_number_of_node_variables, help=\
        """
        
        """
    )

    def _get_number_of_side_set_properties(self):
        return self._vtk_obj.GetNumberOfSideSetProperties()
    number_of_side_set_properties = traits.Property(_get_number_of_side_set_properties, help=\
        """
        The number of side set properties (global variables)
        """
    )

    def _get_number_of_time_steps(self):
        return self._vtk_obj.GetNumberOfTimeSteps()
    number_of_time_steps = traits.Property(_get_number_of_time_steps, help=\
        """
        
        """
    )

    def _get_original_number_of_element_variables(self):
        return self._vtk_obj.GetOriginalNumberOfElementVariables()
    original_number_of_element_variables = traits.Property(_get_original_number_of_element_variables, help=\
        """
        The model_metadata object may contain these lists: o  the
        variables in the original data file o  the variables created in
        the u grid from those original variables o  a mapping from the
        grid variable names to the original names o  a list of the number
        of components each grid variable has
        
        * (Example: Variables in Exodus II files are all scalars.  Some
          are
        * combined by the exodus_reader into vector variables in the
          grid.)
        
        * These methods return names of the original variables, the names
        * of the grid variables, a list of the number of components in
        * each grid variable, and a list of the index into the list of
        * original variable names where the original name of the first
        * component of a grid variable may be found.  The names of
          subsequent
        * components would immediately follow the name of the the first
        * component.
        """
    )

    def _get_original_number_of_node_variables(self):
        return self._vtk_obj.GetOriginalNumberOfNodeVariables()
    original_number_of_node_variables = traits.Property(_get_original_number_of_node_variables, help=\
        """
        
        """
    )

    def _get_side_set_distribution_factor_index(self):
        return self._vtk_obj.GetSideSetDistributionFactorIndex()
    side_set_distribution_factor_index = traits.Property(_get_side_set_distribution_factor_index, help=\
        """
        Get a list of the index of the starting entry for each side set
        in the list of side set distribution factors.
        """
    )

    def _get_side_set_list_index(self):
        return self._vtk_obj.GetSideSetListIndex()
    side_set_list_index = traits.Property(_get_side_set_list_index, help=\
        """
        Get a list of the index of the starting entry for each side set
        in the list of side set side IDs.
        """
    )

    def _get_size_block_attribute_array(self):
        return self._vtk_obj.GetSizeBlockAttributeArray()
    size_block_attribute_array = traits.Property(_get_size_block_attribute_array, help=\
        """
        Get the length of the list of floating point block attributes.
        """
    )

    def _get_sum_dist_fact_per_node_set(self):
        return self._vtk_obj.GetSumDistFactPerNodeSet()
    sum_dist_fact_per_node_set = traits.Property(_get_sum_dist_fact_per_node_set, help=\
        """
        Get the total number of distribution factors stored for all node
        sets
        """
    )

    def _get_sum_dist_fact_per_side_set(self):
        return self._vtk_obj.GetSumDistFactPerSideSet()
    sum_dist_fact_per_side_set = traits.Property(_get_sum_dist_fact_per_side_set, help=\
        """
        Get the total number of distribution factors stored for all side
        sets
        """
    )

    def _get_sum_elements_per_block(self):
        return self._vtk_obj.GetSumElementsPerBlock()
    sum_elements_per_block = traits.Property(_get_sum_elements_per_block, help=\
        """
        Get the length of the list of elements in every block.
        """
    )

    def _get_time_step_values(self):
        return self._vtk_obj.GetTimeStepValues()
    time_step_values = traits.Property(_get_time_step_values, help=\
        """
        Get the time step values
        """
    )

    def free_all_global_data(self):
        """
        V.free_all_global_data()
        C++: void FreeAllGlobalData()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeAllGlobalData()
        return ret
        

    def free_all_local_data(self):
        """
        V.free_all_local_data()
        C++: void FreeAllLocalData()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeAllLocalData()
        return ret
        

    def free_block_dependent_data(self):
        """
        V.free_block_dependent_data()
        C++: void FreeBlockDependentData()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeBlockDependentData()
        return ret
        

    def free_original_element_variable_names(self):
        """
        V.free_original_element_variable_names()
        C++: void FreeOriginalElementVariableNames()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeOriginalElementVariableNames()
        return ret
        

    def free_original_node_variable_names(self):
        """
        V.free_original_node_variable_names()
        C++: void FreeOriginalNodeVariableNames()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeOriginalNodeVariableNames()
        return ret
        

    def free_used_element_variable_names(self):
        """
        V.free_used_element_variable_names()
        C++: void FreeUsedElementVariableNames()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeUsedElementVariableNames()
        return ret
        

    def free_used_element_variables(self):
        """
        V.free_used_element_variables()
        C++: void FreeUsedElementVariables()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeUsedElementVariables()
        return ret
        

    def free_used_node_variable_names(self):
        """
        V.free_used_node_variable_names()
        C++: void FreeUsedNodeVariableNames()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeUsedNodeVariableNames()
        return ret
        

    def free_used_node_variables(self):
        """
        V.free_used_node_variables()
        C++: void FreeUsedNodeVariables()
        Free selected portions of the metadata when updating values in
        the ModelMetadata object.  Resetting a particular field, (i.e.
        set_node_set_ids) frees the previous setting, but if you are not
        setting every field, you may want to do a wholesale "Free" first.
        
        * free_all_global_data frees all the fields which don't depend on
        * which time step, which blocks, or which variables are in the
          input.
        * free_all_local_data frees all the fields which do depend on which
        * time step, blocks or variables are in the input.
        * free_block_dependent_data frees all metadata fields which depend
          on
        * which blocks were read in.
        """
        ret = self._vtk_obj.FreeUsedNodeVariables()
        return ret
        

    def print_global_information(self):
        """
        V.print_global_information()
        C++: virtual void PrintGlobalInformation()
        The global fields are those which pertain to the whole file. 
        Examples are the title, information lines, and list of block IDs.
         This method prints out all the global information.
        """
        ret = self._vtk_obj.PrintGlobalInformation()
        return ret
        

    def print_local_information(self):
        """
        V.print_local_information()
        C++: virtual void PrintLocalInformation()
        The local fields are those which depend on exactly which blocks,
        which time step, and which variables you read in from the file. 
        Examples are the number of cells in each block, and the list of
        nodes in a node set, or the value of the global variables at a
        time step.  If VERBOSE_TESTING is defined in your execution
        environment, this method will print more than mere counts, and
        actually print a few of the IDs, distribution factors and so on. 
        If VERY_VERBOSE_TESTING is defined, it will print out all ID
        lists, distribution factor lists, and so on.
        """
        ret = self._vtk_obj.PrintLocalInformation()
        return ret
        

    def reset(self):
        """
        V.reset()
        C++: void Reset()
        Set the object back to it's initial state
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def set_time_steps(self, *args):
        """
        V.set_time_steps(int, [float, ...])
        C++: void SetTimeSteps(int numberOfTimeSteps,
            float *timeStepValues)
        Set the total number of time steps in the file, and the value at
        each time step.  We use your time step value array and delete it
        when we're done.
        """
        ret = self._wrap_call(self._vtk_obj.SetTimeSteps, *args)
        return ret

    _updateable_traits_ = \
    (('all_variables_defined_in_all_blocks',
    'GetAllVariablesDefinedInAllBlocks'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_blocks', 'GetNumberOfBlocks'), ('number_of_node_sets',
    'GetNumberOfNodeSets'), ('number_of_side_sets',
    'GetNumberOfSideSets'), ('sum_nodes_per_node_set',
    'GetSumNodesPerNodeSet'), ('sum_sides_per_side_set',
    'GetSumSidesPerSideSet'), ('time_step_index', 'GetTimeStepIndex'),
    ('title', 'GetTitle'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['all_variables_defined_in_all_blocks', 'debug',
    'global_warning_display', 'number_of_blocks', 'number_of_node_sets',
    'number_of_side_sets', 'sum_nodes_per_node_set',
    'sum_sides_per_side_set', 'time_step_index', 'title'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ModelMetadata, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ModelMetadata properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['all_variables_defined_in_all_blocks'], [],
            ['number_of_blocks', 'number_of_node_sets', 'number_of_side_sets',
            'sum_nodes_per_node_set', 'sum_sides_per_side_set', 'time_step_index',
            'title']),
            title='Edit ModelMetadata properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ModelMetadata properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

