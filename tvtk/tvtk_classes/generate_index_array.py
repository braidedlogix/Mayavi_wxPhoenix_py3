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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class GenerateIndexArray(DataObjectAlgorithm):
    """
    GenerateIndexArray - Generates a new IdTypeArray containing
    zero-base indices.
    
    Superclass: DataObjectAlgorithm
    
    GenerateIndexArray operates in one of two distinct "modes". By
    default, it simply generates an index array containing
    monotonically-increasing integers in the range [0, N), where N is
    appropriately sized for the field type that will store the results. 
    This mode is useful for generating a unique ID field for datasets
    that have none.
    
    The second "mode" uses an existing array from the input data object
    as a "reference".  Distinct values from the reference array are
    sorted in ascending order, and an integer index in the range [0, N)
    is assigned to each.  The resulting map is used to populate the
    output index array, mapping each value in the reference array to its
    corresponding index and storing the result in the output array.  This
    mode is especially useful when generating tensors, since it allows us
    to "map" from an array with arbitrary contents to an index that can
    be used as tensor coordinates.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGenerateIndexArray, obj, update, **traits)
    
    array_name = traits.String('index', enter_set=True, auto_set=False, help=\
        """
        Control the output index array name.  Default: "index".
        """
    )

    def _array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayName,
                        self.array_name)

    field_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Control the location where the index array will be stored.
        """
    )

    def _field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldType,
                        self.field_type)

    pedigree_id = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specifies whether the index array should be marked as pedigree
        ids.  Default: false.
        """
    )

    def _pedigree_id_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPedigreeID,
                        self.pedigree_id)

    reference_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specifies an optional reference array for index-generation.
        """
    )

    def _reference_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReferenceArrayName,
                        self.reference_array_name)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('array_name',
    'GetArrayName'), ('field_type', 'GetFieldType'), ('pedigree_id',
    'GetPedigreeID'), ('reference_array_name', 'GetReferenceArrayName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'array_name', 'field_type', 'pedigree_id',
    'progress_text', 'reference_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GenerateIndexArray, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GenerateIndexArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['array_name', 'field_type', 'pedigree_id',
            'reference_array_name']),
            title='Edit GenerateIndexArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GenerateIndexArray properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

