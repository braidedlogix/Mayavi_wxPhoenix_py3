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

from tvtk.tvtk_classes.sql_database import SQLDatabase


class SQLiteDatabase(SQLDatabase):
    """
    SQLiteDatabase - maintain a connection to an SQLite database
    
    Superclass: SQLDatabase
    
    SQLite (http://www.sqlite.org) is a public-domain SQL database
    written in C++.  It's small, fast, and can be easily embedded inside
    other applications.  Its databases are stored in files.
    
    This class provides a VTK interface to SQLite.  You do not need to
    download any external libraries: we include a copy of SQLite 3.3.16
    in VTK/Utilities/vtksqlite.
    
    If you want to open a database that stays in memory and never gets
    written to disk, pass in the URL 'sqlite://:memory:'; otherwise,
    specifiy the file path by passing the URL 'sqlite://<file_path>'.
    
    @par Thanks: Thanks to Andrew Wilson and Philippe Pebay from Sandia
    National Laboratories for implementing this class.
    
    @sa
    SQLiteQuery
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSQLiteDatabase, obj, update, **traits)
    
    database_file_name = tvtk_base.vtk_file_name("", help=\
        """
        String representing the database filename.
        """
    )

    def _database_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDatabaseFileName,
                        self.database_file_name)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('database_file_name',
    'GetDatabaseFileName'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'database_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SQLiteDatabase, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SQLiteDatabase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['database_file_name']),
            title='Edit SQLiteDatabase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SQLiteDatabase properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

