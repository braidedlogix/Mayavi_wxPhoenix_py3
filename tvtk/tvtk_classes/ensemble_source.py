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

from tvtk.tvtk_classes.algorithm import Algorithm


class EnsembleSource(Algorithm):
    """
    EnsembleSource - source that manages dataset ensembles
    
    Superclass: Algorithm
    
    EnsembleSource manages a collection of data sources in order to
    represent a dataset ensemble. It has the ability to provide meta-data
    about the ensemble in the form of a table, using the META_DATA key as
    well as accept a pipeline request using the UPDATE_MEMBER key. Note
    that it is expected that all ensemble members produce data of the
    same type.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkEnsembleSource, obj, update, **traits)
    
    current_member = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the current ensemble member to process. Note that this
        data member will not be used if the UPDATE_MEMBER key is present
        in the pipeline. Also, this data member may be removed in the
        future. Unless it is absolutely necessary to use this data
        member, use the UPDATE_MEMBER key instead.
        """
    )

    def _current_member_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCurrentMember,
                        self.current_member)

    def _get_number_of_members(self):
        return self._vtk_obj.GetNumberOfMembers()
    number_of_members = traits.Property(_get_number_of_members, help=\
        """
        Returns the number of ensemble members.
        """
    )

    def add_member(self, *args):
        """
        V.add_member(Algorithm)
        C++: void AddMember(Algorithm *)
        Add an algorithm (source) that will produce the next ensemble
        member. This algorithm will be passed the REQUEST_INFORMATION,
        REQUEST_UPDATE_EXTENT and REQUEST_DATA pipeline passes for
        execution.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddMember, *my_args)
        return ret

    def META_DATA(self):
        """
        V.meta__data() -> InformationDataObjectMetaDataKey
        C++: static InformationDataObjectMetaDataKey *META_DATA()
        Meta-data for the ensemble. This is set with set_meta_data.
        """
        ret = wrap_vtk(self._vtk_obj.META_DATA())
        return ret
        

    def remove_all_members(self):
        """
        V.remove_all_members()
        C++: void RemoveAllMembers()
        Removes all ensemble members.
        """
        ret = self._vtk_obj.RemoveAllMembers()
        return ret
        

    def set_meta_data(self, *args):
        """
        V.set_meta_data(Table)
        C++: void SetMetaData(Table *)
        Set the meta-data that will be propagated downstream. Make sure
        that this table has as many rows as the ensemble members and the
        meta-data for each row matches the corresponding ensemble source.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMetaData, *my_args)
        return ret

    def UPDATE_MEMBER(self):
        """
        V.update__member() -> InformationIntegerRequestKey
        C++: static InformationIntegerRequestKey *UPDATE_MEMBER()
        Key used to request a particular ensemble member.
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_MEMBER())
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('current_member', 'GetCurrentMember'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'current_member', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(EnsembleSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit EnsembleSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['current_member']),
            title='Edit EnsembleSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit EnsembleSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

