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


class PDirectory(Object):
    """
    PDirectory - PDirectory provides a portable way of finding the
    names of the files in a system directory where process 0 finds the
    information and broadcasts it to other processes.
    
    Superclass: Object
    
    It tries to replicate the API for both Directory and Directory
    though there are slight mismatches between the two. This is a
    blocking collective operation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPDirectory, obj, update, **traits)
    
    def get_file(self, *args):
        """
        V.get_file(int) -> string
        C++: const char *GetFile(IdType index)
        Return the file at the given index, the indexing is 0 based
        """
        ret = self._wrap_call(self._vtk_obj.GetFile, *args)
        return ret

    def _get_files(self):
        return wrap_vtk(self._vtk_obj.GetFiles())
    files = traits.Property(_get_files, help=\
        """
        Get an array that contains all the file names.
        """
    )

    def _get_number_of_files(self):
        return self._vtk_obj.GetNumberOfFiles()
    number_of_files = traits.Property(_get_number_of_files, help=\
        """
        Return the number of files in the current directory.
        """
    )

    def _get_path(self):
        return self._vtk_obj.GetPath()
    path = traits.Property(_get_path, help=\
        """
        Return the path to Open'ed directory
        """
    )

    def clear(self):
        """
        V.clear()
        C++: void Clear()
        Clear the internal structure. Used internally at beginning of
        Load(...) to clear the cache.
        """
        ret = self._vtk_obj.Clear()
        return ret
        

    def file_is_directory(self, *args):
        """
        V.file_is_directory(string) -> int
        C++: int FileIsDirectory(const char *name)
        Return true if the file is a directory.  If the file is not an
        absolute path, it is assumed to be relative to the opened
        directory. If no directory has been opened, it is assumed to be
        relative to the current working directory.
        """
        ret = self._wrap_call(self._vtk_obj.FileIsDirectory, *args)
        return ret

    def load(self, *args):
        """
        V.load(string) -> bool
        C++: bool Load(const std::string &)
        Open/Load the specified directory and load the names of the files
        in that directory. false/0 is returned if the directory can not
        be opened, true/1 if it is opened. The reason that there are two
        versions of this is that Directory uses Load() and Directory
        uses Open() for this functionality.
        """
        ret = self._wrap_call(self._vtk_obj.Load, *args)
        return ret

    def open(self, *args):
        """
        V.open(string) -> int
        C++: int Open(const char *dir)
        Open/Load the specified directory and load the names of the files
        in that directory. false/0 is returned if the directory can not
        be opened, true/1 if it is opened. The reason that there are two
        versions of this is that Directory uses Load() and Directory
        uses Open() for this functionality.
        """
        ret = self._wrap_call(self._vtk_obj.Open, *args)
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
            return super(PDirectory, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PDirectory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit PDirectory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PDirectory properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

