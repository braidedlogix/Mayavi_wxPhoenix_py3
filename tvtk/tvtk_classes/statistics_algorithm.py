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

from tvtk.tvtk_classes.table_algorithm import TableAlgorithm


class StatisticsAlgorithm(TableAlgorithm):
    """
    StatisticsAlgorithm - Base class for statistics algorithms
    
    Superclass: TableAlgorithm
    
    All statistics algorithms can conceptually be operated with several
    operations:
    * Learn: given an input data set, calculate a minimal statistical
      model (e.g., sums, raw moments, joint probabilities).
    * Derive: given an input minimal statistical model, derive the full
      model (e.g., descriptive statistics, quantiles, correlations,
      conditional probabilities). NB: It may be, or not be, a problem
      that a full model was not derived. For instance, when doing
      parallel calculations, one only wants to derive the full model
      after all partial calculations have completed. On the other hand,
      one can also directly provide a full model, that was previously
      calculated or guessed, and not derive a new one.
    * Assess: given an input data set, input statistics, and some form of
      threshold, assess a subset of the data set.
    * Test: perform at least one statistical test. Therefore, a
      StatisticsAlgorithm has the following ports
    * 3 optional input ports:
    * Data (vtk_table)
    * Parameters to the learn operation (vtk_table)
    * Input model (vtk_multi_block_data_set)
    * 3 output ports:
    * Data (input annotated with assessments when the Assess operation is
    ON).
    * Output model (identical to the the input model when Learn operation
    is OFF).
    * Output of statistical tests. Some engines do not offer such tests
      yet, in which case this output will always be empty even when the
      Test operation is ON.
    
    @par Thanks: Thanks to Philippe Pebay and David Thompson from Sandia
    National Laboratories for implementing this class. Updated by
    Philippe Pebay, Kitware SAS 2012
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStatisticsAlgorithm, obj, update, **traits)
    
    def _get_assess_names(self):
        return wrap_vtk(self._vtk_obj.GetAssessNames())
    def _set_assess_names(self, arg):
        old_val = self._get_assess_names()
        my_arg = deref_array([arg], [['vtkStringArray']])
        self._wrap_call(self._vtk_obj.SetAssessNames,
                        my_arg[0])
        self.trait_property_changed('assess_names', old_val, arg)
    assess_names = traits.Property(_get_assess_names, _set_assess_names, help=\
        """
        Set/get assessment names.
        """
    )

    assess_option = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Assess operation.
        """
    )

    def _assess_option_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAssessOption,
                        self.assess_option)

    derive_option = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Derive operation.
        """
    )

    def _derive_option_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDeriveOption,
                        self.derive_option)

    learn_option = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Learn operation.
        """
    )

    def _learn_option_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLearnOption,
                        self.learn_option)

    number_of_primary_tables = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of tables in the primary model.
        """
    )

    def _number_of_primary_tables_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPrimaryTables,
                        self.number_of_primary_tables)

    test_option = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Test operation.
        """
    )

    def _test_option_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTestOption,
                        self.test_option)

    def get_column_for_request(self, *args):
        """
        V.get_column_for_request(int, int) -> string
        C++: virtual const char *GetColumnForRequest(IdType r,
            IdType c)
        V.get_column_for_request(int, int, string) -> int
        C++: virtual int GetColumnForRequest(IdType r, IdType c,
            StdString &columnName)
        Provide the name of the c-th column for the r-th request.
        
        * For the version of this routine that returns an integer,
        * if the request or column does not exist because r or c is out
          of bounds,
        * this routine returns 0 and the value of column_name is
          unspecified.
        * Otherwise, it returns 1 and the value of column_name is set.
        
        * For the version of this routine that returns const char*,
        * if the request or column does not exist because r or c is out
          of bounds,
        * the routine returns NULL. Otherwise it returns the column name.
        * This version is not thread-safe.
        """
        ret = self._wrap_call(self._vtk_obj.GetColumnForRequest, *args)
        return ret

    def get_number_of_columns_for_request(self, *args):
        """
        V.get_number_of_columns_for_request(int) -> int
        C++: virtual IdType GetNumberOfColumnsForRequest(
            IdType request)
        Return the number of columns for a given request.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfColumnsForRequest, *args)
        return ret

    def _get_number_of_requests(self):
        return self._vtk_obj.GetNumberOfRequests()
    number_of_requests = traits.Property(_get_number_of_requests, help=\
        """
        Return the number of requests. This does not include any request
        that is in the column-status buffer but for which
        request_selected_columns() has not yet been called (even though it
        is possible this request will be honored when the filter is run
        -- see set_column_status() for more information).
        """
    )

    def add_column(self, *args):
        """
        V.add_column(string)
        C++: void AddColumn(const char *namCol)
        Convenience method to create a request with a single column name
        nam_col in a single call; this is the preferred method to select
        columns, ensuring selection consistency (a single column per
        request). Warning: no name checking is performed on nam_col; it is
        the user's responsibility to use valid column names.
        """
        ret = self._wrap_call(self._vtk_obj.AddColumn, *args)
        return ret

    def add_column_pair(self, *args):
        """
        V.add_column_pair(string, string)
        C++: void AddColumnPair(const char *namColX, const char *namColY)
        Convenience method to create a request with a single column name
        pair ( nam_col_x, nam_col_y) in a single call; this is the preferred
        method to select columns pairs, ensuring selection consistency (a
        pair of columns per request).
        
        * Unlike set_column_status(), you need not call
          request_selected_columns() after add_column_pair().
        
        * Warning: nam_col_x and nam_col_y are only checked for their
          validity as strings;
        * no check is made that either are valid column names.
        """
        ret = self._wrap_call(self._vtk_obj.AddColumnPair, *args)
        return ret

    def aggregate(self, *args):
        """
        V.aggregate(DataObjectCollection, MultiBlockDataSet)
        C++: virtual void Aggregate(DataObjectCollection *,
            MultiBlockDataSet *)
        Given a collection of models, calculate aggregate model
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Aggregate, *my_args)
        return ret

    def request_selected_columns(self):
        """
        V.request_selected_columns() -> int
        C++: virtual int RequestSelectedColumns()
        Use the current column status values to produce a new request for
        statistics to be produced when request_data() is called. See
        set_column_status() for more information.
        """
        ret = self._vtk_obj.RequestSelectedColumns()
        return ret
        

    def reset_all_column_states(self):
        """
        V.reset_all_column_states()
        C++: virtual void ResetAllColumnStates()
        Set the the status of each and every column in the current
        request to OFF (0).
        """
        ret = self._vtk_obj.ResetAllColumnStates()
        return ret
        

    def reset_requests(self):
        """
        V.reset_requests()
        C++: virtual void ResetRequests()
        Empty the list of current requests.
        """
        ret = self._vtk_obj.ResetRequests()
        return ret
        

    def set_column_status(self, *args):
        """
        V.set_column_status(string, int)
        C++: virtual void SetColumnStatus(const char *namCol, int status)
        Add or remove a column from the current analysis request. Once
        all the column status values are set, call
        request_selected_columns() before selecting another set of columns
        for a different analysis request. The way that columns selections
        are used varies from algorithm to algorithm.
        
        * Note: the set of selected columns is maintained in
          StatisticsAlgorithmPrivate::Buffer
        * until request_selected_columns() is called, at which point the
          set is appended
        * to StatisticsAlgorithmPrivate::Requests.
        * If there are any columns in
          StatisticsAlgorithmPrivate::Buffer at the time
        * request_data() is called, request_selected_columns() will be
          called and the
        * selection added to the list of requests.
        """
        ret = self._wrap_call(self._vtk_obj.SetColumnStatus, *args)
        return ret

    def set_input_model(self, *args):
        """
        V.set_input_model(DataObject)
        C++: virtual void SetInputModel(DataObject *model)
        A convenience method for setting the input model (if one is
        expected or allowed). It is equivalent to calling set_input_data(
        2, model );
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputModel, *my_args)
        return ret

    def set_input_model_connection(self, *args):
        """
        V.set_input_model_connection(AlgorithmOutput)
        C++: virtual void SetInputModelConnection(
            AlgorithmOutput *model)
        A convenience method for setting the input model connection (if
        one is expected or allowed). It is equivalent to calling
        set_input_connection( 2, model );
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputModelConnection, *my_args)
        return ret

    def set_learn_option_parameter_connection(self, *args):
        """
        V.set_learn_option_parameter_connection(AlgorithmOutput)
        C++: virtual void SetLearnOptionParameterConnection(
            AlgorithmOutput *params)
        A convenience method for setting learn input parameters (if one
        is expected or allowed). It is equivalent to calling
        set_input_connection( 1, params );
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLearnOptionParameterConnection, *my_args)
        return ret

    def set_learn_option_parameters(self, *args):
        """
        V.set_learn_option_parameters(DataObject)
        C++: virtual void SetLearnOptionParameters(DataObject *params)
        A convenience method for setting learn input parameters (if one
        is expected or allowed). It is equivalent to calling
        set_input_data( 1, params );
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetLearnOptionParameters, *my_args)
        return ret

    def set_parameter(self, *args):
        """
        V.set_parameter(string, int, Variant) -> bool
        C++: virtual bool SetParameter(const char *parameter, int index,
            Variant value)
        A convenience method (in particular for access from other
        applications) to set parameter values of Learn mode. Return true
        if setting of requested parameter name was excuted, false
        otherwise. NB: default method (which is sufficient for most
        statistics algorithms) does not have any Learn parameters to set
        and always returns false.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetParameter, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('assess_option', 'GetAssessOption'), ('derive_option',
    'GetDeriveOption'), ('learn_option', 'GetLearnOption'),
    ('number_of_primary_tables', 'GetNumberOfPrimaryTables'),
    ('test_option', 'GetTestOption'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'assess_option', 'derive_option', 'learn_option',
    'number_of_primary_tables', 'progress_text', 'test_option'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(StatisticsAlgorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StatisticsAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['assess_option', 'derive_option', 'learn_option',
            'number_of_primary_tables', 'test_option']),
            title='Edit StatisticsAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StatisticsAlgorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

