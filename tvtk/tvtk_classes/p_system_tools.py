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


class PSystemTools(Object):
    """
    PSystemTools - System tools for file system introspection
    
    Superclass: Object
    
    A class with only static methods for doing parallel file system
    introspection. It limits doing file stats on process 0 and
    broadcasting the results to other processes. It is built on VTK's
    system_tools class and uses the global controller for communication.
    It uses blocking collective communication operations.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPSystemTools, obj, update, **traits)
    
    def get_current_working_directory(self, *args):
        """
        V.get_current_working_directory(bool) -> string
        C++: static std::string GetCurrentWorkingDirectory(
            bool collapse=true)
        Get current working directory CWD
        """
        ret = self._wrap_call(self._vtk_obj.GetCurrentWorkingDirectory, *args)
        return ret

    def get_program_path(self, *args):
        """
        V.get_program_path(string) -> string
        C++: static std::string GetProgramPath(const std::string &)
        Given the path to a program executable, get the directory part of
        the path with the file stripped off.  If there is no directory
        part, the empty string is returned.
        """
        ret = self._wrap_call(self._vtk_obj.GetProgramPath, *args)
        return ret

    def broadcast_string(self, *args):
        """
        V.broadcast_string(string, int)
        C++: static void BroadcastString(std::string &, int proc)
        Given a string on process proc, broadcast that string to all of
        the other processes. This method does not have a correspondence
        to anything in system_tools.
        """
        ret = self._wrap_call(self._vtk_obj.BroadcastString, *args)
        return ret

    def collapse_full_path(self, *args):
        """
        V.collapse_full_path(string) -> string
        C++: static std::string CollapseFullPath(
            const std::string &in_relative)
        V.collapse_full_path(string, string) -> string
        C++: static std::string CollapseFullPath(
            const std::string &in_relative, const char *in_base)
        Given a path to a file or directory, convert it to a full path.
        This collapses away relative paths relative to the cwd argument
        (which defaults to the current working directory).  The full path
        is returned.
        """
        ret = self._wrap_call(self._vtk_obj.CollapseFullPath, *args)
        return ret

    def file_exists(self, *args):
        """
        V.file_exists(string, bool) -> bool
        C++: static bool FileExists(const std::string &filename,
            bool isFile)
        V.file_exists(string) -> bool
        C++: static bool FileExists(const std::string &filename)
        Return true if a file exists in the current directory. If is_file
        = true, then make sure the file is a file and not a directory. 
        If is_file = false, then return true if it is a file or a
        directory.  Note that the file will also be checked for read
        access.  (Currently, this check for read access is only done on
        POSIX systems.)
        """
        ret = self._wrap_call(self._vtk_obj.FileExists, *args)
        return ret

    def file_is_directory(self, *args):
        """
        V.file_is_directory(string) -> bool
        C++: static bool FileIsDirectory(const std::string &name)
        Return true if the file is a directory
        """
        ret = self._wrap_call(self._vtk_obj.FileIsDirectory, *args)
        return ret

    def find_program_path(self, *args):
        """
        V.find_program_path(string, string, string, string, string, string)
            -> bool
        C++: static bool FindProgramPath(const char *argv0,
            std::string &pathOut, std::string &errorMsg,
            const char *exeName=0, const char *buildDir=0,
            const char *installPrefix=0)
        Given argv[0] for a unix program find the full path to a running
        executable.  argv0 can be null for windows win_main programs in
        this case get_module_file_name will be used to find the path to the
        running executable.  If argv0 is not a full path, then this will
        try to find the full path.  If the path is not found false is
        returned, if found true is returned.  An error message of the
        attempted paths is stored in error_msg. exe_name is the name of the
        executable. build_dir is a possibly null path to the build
        directory. install_prefix is a possibly null pointer to the
        install directory.
        """
        ret = self._wrap_call(self._vtk_obj.FindProgramPath, *args)
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
            return super(PSystemTools, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PSystemTools properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit PSystemTools properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PSystemTools properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

