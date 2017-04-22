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


class QuadratureSchemeDefinition(Object):
    """
    QuadratureSchemeDefinition - An Elemental data type that holds a
    definition of a numerical quadrature scheme.
    
    Superclass: Object
    
    The definition contains the requisite information to interpolate to
    the so called quadrature points of the specific scheme. namely:
    
    1) A matrix of shape function weights(shape functions evaluated at
    parametric coordinates of the quadrature points).
    
    2) The number of quadrature points and cell nodes. These parameters
    size the matrix, and allow for convinent evaluation by users of the
    definition. 
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkQuadratureSchemeDefinition, obj, update, **traits)
    
    def _get_cell_type(self):
        return self._vtk_obj.GetCellType()
    cell_type = traits.Property(_get_cell_type, help=\
        """
        Access the VTK cell type id.
        """
    )

    def _get_number_of_nodes(self):
        return self._vtk_obj.GetNumberOfNodes()
    number_of_nodes = traits.Property(_get_number_of_nodes, help=\
        """
        Get the number of nodes associated with the interpolation.
        """
    )

    def _get_number_of_quadrature_points(self):
        return self._vtk_obj.GetNumberOfQuadraturePoints()
    number_of_quadrature_points = traits.Property(_get_number_of_quadrature_points, help=\
        """
        Get the number of quadrature points associated with the scheme.
        """
    )

    def _get_quadrature_key(self):
        return self._vtk_obj.GetQuadratureKey()
    quadrature_key = traits.Property(_get_quadrature_key, help=\
        """
        Access to an alternative key.
        """
    )

    def _get_quadrature_weights(self):
        return self._vtk_obj.GetQuadratureWeights()
    quadrature_weights = traits.Property(_get_quadrature_weights, help=\
        """
        Access to the quadrature weights.
        """
    )

    def _get_shape_function_weights(self):
        return self._vtk_obj.GetShapeFunctionWeights()
    shape_function_weights = traits.Property(_get_shape_function_weights, help=\
        """
        Get the array of shape function weights. Shape function weights
        are the shape functions evaluated at the quadrature points. There
        are "_number_of_nodes" weights for each quadrature point.
        """
    )

    def clear(self):
        """
        V.clear()
        C++: void Clear()
        Release all allocated resources and set the object to an
        unitialized state.
        """
        ret = self._vtk_obj.Clear()
        return ret
        

    def DICTIONARY(self):
        """
        V.dictionary()
            -> InformationQuadratureSchemeDefinitionVectorKey
        C++: static InformationQuadratureSchemeDefinitionVectorKey *DICTIONARY(
            )"""
        ret = wrap_vtk(self._vtk_obj.DICTIONARY())
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(QuadratureSchemeDefinition) -> int
        C++: int DeepCopy(const QuadratureSchemeDefinition *other)
        Deep copy.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def initialize(self, *args):
        """
        V.initialize(int, int, int, [float, ...])
        C++: void Initialize(int cellType, int numberOfNodes,
            int numberOfQuadraturePoints, double *shapeFunctionWeights)
        V.initialize(int, int, int, [float, ...], [float, ...])
        C++: void Initialize(int cellType, int numberOfNodes,
            int numberOfQuadraturePoints, double *shapeFunctionWeights,
            double *quadratureWeights)
        Initialize the object allocating resources as needed.
        """
        ret = self._wrap_call(self._vtk_obj.Initialize, *args)
        return ret

    def QUADRATURE_OFFSET_ARRAY_NAME(self):
        """
        V.quadrature__offset__array__name() -> InformationStringKey
        C++: static InformationStringKey *QUADRATURE_OFFSET_ARRAY_NAME(
            )"""
        ret = wrap_vtk(self._vtk_obj.QUADRATURE_OFFSET_ARRAY_NAME())
        return ret
        

    def restore_state(self, *args):
        """
        V.restore_state(XMLDataElement) -> int
        C++: int RestoreState(XMLDataElement *e)
        Restore the object from an XML representation.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RestoreState, *my_args)
        return ret

    def save_state(self, *args):
        """
        V.save_state(XMLDataElement) -> int
        C++: int SaveState(XMLDataElement *e)
        Put the object into an XML representation. The element passed in
        is assumed to be empty.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SaveState, *my_args)
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
            return super(QuadratureSchemeDefinition, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit QuadratureSchemeDefinition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit QuadratureSchemeDefinition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit QuadratureSchemeDefinition properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

