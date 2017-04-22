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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class PCAAnalysisFilter(MultiBlockDataSetAlgorithm):
    """
    PCAAnalysisFilter - Performs principal component analysis of a set
    of aligned pointsets
    
    Superclass: MultiBlockDataSetAlgorithm
    
    PCAAnalysisFilter is a filter that takes as input a set of aligned
    pointsets (any object derived from PointSet) and performs a
    principal component analysis of the coordinates. This can be used to
    visualise the major or minor modes of variation seen in a set of
    similar biological objects with corresponding landmarks.
    PCAAnalysisFilter is designed to work with the output from the
    ProcrustesAnalysisFilter PCAAnalysisFilter requires a
    MultiBlock input consisting of PointSets as first level
    children.
    
    PCAAnalysisFilter is an implementation of (for example):
    
    T. Cootes et al. : Active Shape Models - their training and
    application. Computer Vision and Image Understanding, 61(1):38-59,
    1995.
    
    The material can also be found in Tim Cootes' ever-changing online
    report published at his website: http://www.isbe.man.ac.uk/~bim/
    
    @warning
    All of the input pointsets must have the same number of points.
    
    @par Thanks: Rasmus Paulsen and Tim Hutton who developed and
    contributed this class
    
    @sa
    ProcrustesAlignmentFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPCAAnalysisFilter, obj, update, **traits)
    
    def _get_evals(self):
        return wrap_vtk(self._vtk_obj.GetEvals())
    evals = traits.Property(_get_evals, help=\
        """
        Get the vector of eigenvalues sorted in descending order
        """
    )

    def get_modes_required_for(self, *args):
        """
        V.get_modes_required_for(float) -> int
        C++: int GetModesRequiredFor(double proportion)
        Retrieve how many modes are necessary to model the given
        proportion of the variation. proportion should be between 0 and 1
        """
        ret = self._wrap_call(self._vtk_obj.GetModesRequiredFor, *args)
        return ret

    def get_parameterised_shape(self, *args):
        """
        V.get_parameterised_shape(FloatArray, PointSet)
        C++: void GetParameterisedShape(FloatArray *b,
            PointSet *shape)
        Fills the shape with:
        
        * mean + b[0] * sqrt(eigenvalue[0]) * eigenvector[0]
        * + b[1] * sqrt(eigenvalue[1]) * eigenvector[1]
        * ...
        * + b[sizeb-1] * sqrt(eigenvalue[bsize-1]) * eigenvector[bsize-1]
        
        * here b are the parameters expressed in standard deviations
        * bsize is the number of parameters in the b vector
        * This function assumes that shape is already allocated
        * with the right size, it just moves the points.
        """
        my_args = deref_array(args, [('vtkFloatArray', 'vtkPointSet')])
        ret = self._wrap_call(self._vtk_obj.GetParameterisedShape, *my_args)
        return ret

    def get_shape_parameters(self, *args):
        """
        V.get_shape_parameters(PointSet, FloatArray, int)
        C++: void GetShapeParameters(PointSet *shape, FloatArray *b,
             int bsize)
        Return the bsize parameters b that best model the given shape (in
        standard deviations). That is that the given shape will be
        approximated by:
        
        * shape ~ mean + b[0] * sqrt(eigenvalue[0]) * eigenvector[0]
        * + b[1] * sqrt(eigenvalue[1]) * eigenvector[1]
        * ...
        * + b[bsize-1] * sqrt(eigenvalue[bsize-1]) * eigenvector[bsize-1]
        """
        my_args = deref_array(args, [('vtkPointSet', 'vtkFloatArray', 'int')])
        ret = self._wrap_call(self._vtk_obj.GetShapeParameters, *my_args)
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
            return super(PCAAnalysisFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PCAAnalysisFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit PCAAnalysisFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PCAAnalysisFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

