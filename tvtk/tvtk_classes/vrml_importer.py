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

from tvtk.tvtk_classes.importer import Importer


class VRMLImporter(Importer):
    """
    VRMLImporter - imports VRML 2.0 files.
    
    Superclass: Importer
    
    VRMLImporter imports VRML 2.0 files into VTK.
    
    @warning
    These nodes are currently supported:
         Appearance                              indexed_face_set
         Box                                     indexed_line_set
         Color                                   Material
         Cone                                    Shape
         Coordinate                              Sphere
         Cylinder                                Transform
         directional_light
    
    @warning
    As you can see this implementation focuses on getting the geometry
    translated.  The routes and scripting nodes are ignored since they
    deal with directly accessing a nodes internal structure based on the
    VRML spec. Since this is a translation the internal data structures
    differ greatly from the VRML spec and the External Authoring
    Interface (see the VRML spec). The DEF/USE mechanism does allow the
    VTK user to extract objects from the scene and directly manipulate
    them using the native language (Tcl, Python, Java, or whatever
    language VTK is wrapped in). This, in a way, removes the need for the
    route and script mechanism (not completely though). Texture
    coordinates are attached to the mesh is available but image textures
    are not loaded. Viewpoints (camera presets) are not imported.
    
    @par Thanks:
     Thanks to Russ Coucher of Areva for numerous bug fixes and a new
    test.
    
    @sa
    Importer
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkVRMLImporter, obj, update, **traits)
    
    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the file to read.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    shape_resolution = traits.Int(12, enter_set=True, auto_set=False, help=\
        """
        Specify the resolution for Sphere, Cone and Cylinder shape
        sources. Default is 12.
        """
    )

    def _shape_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShapeResolution,
                        self.shape_resolution)

    def get_vrmldef_object(self, *args):
        """
        V.get_vrmldef_object(string) -> Object
        C++: Object *GetVRMLDEFObject(const char *name)
        In the VRML spec you can DEF and USE nodes (name them), This
        routine will return the associated VTK object which was created
        as a result of the DEF mechanism Send in the name from the VRML
        file, get the VTK object. You will have to check and correctly
        cast the object since this only returns Objects.
        """
        ret = self._wrap_call(self._vtk_obj.GetVRMLDEFObject, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'),
    ('shape_resolution', 'GetShapeResolution'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'file_name', 'shape_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(VRMLImporter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit VRMLImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['file_name', 'shape_resolution']),
            title='Edit VRMLImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit VRMLImporter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

