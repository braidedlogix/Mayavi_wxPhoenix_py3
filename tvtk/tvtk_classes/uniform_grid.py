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

from tvtk.tvtk_classes.image_data import ImageData


class UniformGrid(ImageData):
    """
    UniformGrid - image data with blanking
    
    Superclass: ImageData
    
    UniformGrid is a subclass of ImageData. In addition to all the
    image data functionality, it supports blanking.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUniformGrid, obj, update, **traits)
    
    def _get_grid_description(self):
        return self._vtk_obj.GetGridDescription()
    grid_description = traits.Property(_get_grid_description, help=\
        """
        Returns the data description of this uniform grid instance.
        """
    )

    def blank_cell(self, *args):
        """
        V.blank_cell(int)
        C++: virtual void BlankCell(IdType ptId)
        V.blank_cell(int, int, int)
        C++: virtual void BlankCell(const int i, const int j, const int k)
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid. These methods should be called
        only after the dimensions of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.BlankCell, *args)
        return ret

    def blank_point(self, *args):
        """
        V.blank_point(int)
        C++: virtual void BlankPoint(IdType ptId)
        V.blank_point(int, int, int)
        C++: virtual void BlankPoint(const int i, const int j,
            const int k)
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.BlankPoint, *args)
        return ret

    def is_cell_visible(self, *args):
        """
        V.is_cell_visible(int) -> int
        C++: virtual unsigned char IsCellVisible(IdType cellId)
        Return non-zero value if specified cell is visible. These methods
        should be called only after the dimensions of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.IsCellVisible, *args)
        return ret

    def is_point_visible(self, *args):
        """
        V.is_point_visible(int) -> int
        C++: virtual unsigned char IsPointVisible(IdType ptId)
        Return non-zero value if specified point is visible. These
        methods should be called only after the dimensions of the grid
        are set.
        """
        ret = self._wrap_call(self._vtk_obj.IsPointVisible, *args)
        return ret

    def new_image_data_copy(self):
        """
        V.new_image_data_copy() -> ImageData
        C++: virtual ImageData *NewImageDataCopy()"""
        ret = wrap_vtk(self._vtk_obj.NewImageDataCopy())
        return ret
        

    def un_blank_cell(self, *args):
        """
        V.un_blank_cell(int)
        C++: virtual void UnBlankCell(IdType ptId)
        V.un_blank_cell(int, int, int)
        C++: virtual void UnBlankCell(const int i, const int j,
            const int k)
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid. These methods should be called
        only after the dimensions of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlankCell, *args)
        return ret

    def un_blank_point(self, *args):
        """
        V.un_blank_point(int)
        C++: virtual void UnBlankPoint(IdType ptId)
        V.un_blank_point(int, int, int)
        C++: virtual void UnBlankPoint(const int i, const int j,
            const int k)
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ret = self._wrap_call(self._vtk_obj.UnBlankPoint, *args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('dimensions', 'GetDimensions'), ('extent', 'GetExtent'),
    ('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('origin', 'GetOrigin'), ('spacing', 'GetSpacing'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'dimensions', 'extent', 'number_of_scalar_components', 'origin',
    'spacing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UniformGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UniformGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['dimensions', 'extent',
            'number_of_scalar_components', 'origin', 'spacing']),
            title='Edit UniformGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UniformGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

