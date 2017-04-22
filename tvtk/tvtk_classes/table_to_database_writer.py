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


class TableToDatabaseWriter(Writer):
    """
    TableToDatabaseWriter - in a SQL database.
    
    Superclass: Writer
    
    TableToDatabaseWriter abstract parent class that reads a Table
    and inserts it into an SQL database.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTableToDatabaseWriter, obj, update, **traits)
    
    def _get_database(self):
        return wrap_vtk(self._vtk_obj.GetDatabase())
    def _set_database(self, arg):
        old_val = self._get_database()
        self._wrap_call(self._vtk_obj.SetDatabase,
                        deref_vtk(arg))
        self.trait_property_changed('database', old_val, arg)
    database = traits.Property(_get_database, _set_database, help=\
        """
        
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> Table
        C++: Table *GetInput()
        V.get_input(int) -> Table
        C++: Table *GetInput(int port)
        Get the input to this writer.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_table_name(self, *args):
        """
        V.set_table_name(string) -> bool
        C++: bool SetTableName(const char *name)
        Set the name of the new SQL table that you'd this writer to
        create. Returns false if the specified table already exists in
        the database.
        """
        ret = self._wrap_call(self._vtk_obj.SetTableName, *args)
        return ret

    def table_name_is_new(self):
        """
        V.table_name_is_new() -> bool
        C++: bool TableNameIsNew()
        Check if the currently specified table name exists in the
        database.
        """
        ret = self._vtk_obj.TableNameIsNew()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TableToDatabaseWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TableToDatabaseWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit TableToDatabaseWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TableToDatabaseWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

