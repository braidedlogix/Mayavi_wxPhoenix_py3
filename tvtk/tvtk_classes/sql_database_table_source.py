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


class SQLDatabaseTableSource(TableAlgorithm):
    """
    SQLDatabaseTableSource - Generates a Table based on an SQL
    query.
    
    Superclass: TableAlgorithm
    
    This class combines SQLDatabase, SQLQuery, and QueryToTable
    to provide a convenience class for generating tables from databases.
    Also this class can be easily wrapped and used within para_view /
    over_view.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSQLDatabaseTableSource, obj, update, **traits)
    
    generate_pedigree_ids = tvtk_base.true_bool_trait(help=\
        """
        If on (default), generates pedigree ids automatically. If off,
        assign one of the arrays to be the pedigree id.
        """
    )

    def _generate_pedigree_ids_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeneratePedigreeIds,
                        self.generate_pedigree_ids_)

    pedigree_id_array_name = traits.String('id', enter_set=True, auto_set=False, help=\
        """
        The name of the array for generating or assigning pedigree ids
        (default "id").
        """
    )

    def _pedigree_id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPedigreeIdArrayName,
                        self.pedigree_id_array_name)

    query = traits.String('', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _query_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQuery,
                        self.query)

    url = traits.String('', enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _url_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetURL,
                        self.url)

    def set_password(self, *args):
        """
        V.set_password(string)
        C++: void SetPassword(const StdString &password)"""
        ret = self._wrap_call(self._vtk_obj.SetPassword, *args)
        return ret

    _updateable_traits_ = \
    (('generate_pedigree_ids', 'GetGeneratePedigreeIds'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('pedigree_id_array_name', 'GetPedigreeIdArrayName'), ('query',
    'GetQuery'), ('url', 'GetURL'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_pedigree_ids',
    'global_warning_display', 'release_data_flag',
    'pedigree_id_array_name', 'progress_text', 'query', 'url'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SQLDatabaseTableSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SQLDatabaseTableSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_pedigree_ids'], [], ['pedigree_id_array_name',
            'query', 'url']),
            title='Edit SQLDatabaseTableSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SQLDatabaseTableSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

