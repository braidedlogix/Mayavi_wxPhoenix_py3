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

from tvtk.tvtk_classes.geo_tree_node import GeoTreeNode


class GeoImageNode(GeoTreeNode):
    """
    GeoImageNode - A node in a multi-resolution image tree.
    
    Superclass: GeoTreeNode
    
    GeoImageNode contains an image tile in a multi-resolution image
    tree, along with metadata about that image's extents.
    
    @sa
    GeoTreeNode GeoTerrainNode
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoImageNode, obj, update, **traits)
    
    def get_child(self, *args):
        """
        V.get_child(int) -> GeoImageNode
        C++: GeoImageNode *GetChild(int idx)
        Every subclass implements these methods returning the specific
        type. This is easier than templating.
        """
        ret = self._wrap_call(self._vtk_obj.GetChild, *args)
        return wrap_vtk(ret)

    def set_child(self, *args):
        """
        V.set_child(GeoTreeNode, int)
        C++: void SetChild(GeoTreeNode *node, int idx)
        Get a child of this node. If one is set, then they all should
        set.  No not mix subclasses.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetChild, *my_args)
        return ret

    def _get_image(self):
        return wrap_vtk(self._vtk_obj.GetImage())
    def _set_image(self, arg):
        old_val = self._get_image()
        self._wrap_call(self._vtk_obj.SetImage,
                        deref_vtk(arg))
        self.trait_property_changed('image', old_val, arg)
    image = traits.Property(_get_image, _set_image, help=\
        """
        Get the image tile.
        """
    )

    def _get_parent(self):
        return wrap_vtk(self._vtk_obj.GetParent())
    def _set_parent(self, arg):
        old_val = self._get_parent()
        self._wrap_call(self._vtk_obj.SetParent,
                        deref_vtk(arg))
        self.trait_property_changed('parent', old_val, arg)
    parent = traits.Property(_get_parent, _set_parent, help=\
        """
        Every subclass implements these methods returning the specific
        type. This is easier than templating.
        """
    )

    def _get_texture(self):
        return wrap_vtk(self._vtk_obj.GetTexture())
    def _set_texture(self, arg):
        old_val = self._get_texture()
        self._wrap_call(self._vtk_obj.SetTexture,
                        deref_vtk(arg))
        self.trait_property_changed('texture', old_val, arg)
    texture = traits.Property(_get_texture, _set_texture, help=\
        """
        Get the image tile.
        """
    )

    def crop_image_for_tile(self, *args):
        """
        V.crop_image_for_tile(ImageData, [float, ...], string)
        C++: void CropImageForTile(ImageData *image,
            double *imageLonLatExt, const char *prefix=0)
        This crops the image as small as possible while still covering
        the patch.  The Longitude Latitude range may get bigger to
        reflect the actual size of the image. If prefix is specified,
        writes the tile to that location.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CropImageForTile, *my_args)
        return ret

    def load_an_image(self, *args):
        """
        V.load_an_image(string)
        C++: void LoadAnImage(const char *prefix)
        This loads the image from a tile database at the specified
        location.
        """
        ret = self._wrap_call(self._vtk_obj.LoadAnImage, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('id', 'GetId'), ('latitude_range',
    'GetLatitudeRange'), ('level', 'GetLevel'), ('longitude_range',
    'GetLongitudeRange'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'id', 'latitude_range', 'level',
    'longitude_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoImageNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoImageNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['id', 'latitude_range', 'level', 'longitude_range']),
            title='Edit GeoImageNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoImageNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

