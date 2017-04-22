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

from tvtk.tvtk_classes.undirected_graph import UndirectedGraph


class Molecule(UndirectedGraph):
    """
    Molecule - class describing a molecule
    
    Superclass: UndirectedGraph
    
    Molecule and the convenience classes Atom and Bond describe
    the geometry and connectivity of a molecule. The molecule can be
    constructed using the append_atom() and append_bond() methods in one of
    two ways; either by fully specifying the atom/bond in a single call,
    or by incrementally setting the various attributes using the
    convience Atom and Bond classes:
    
    Single call:vtk_molecule *mol = Molecule::New();
    Atom h1 = mol->_append_atom(_1, 0.0, 0.0, -0.5);
    Atom h2 = mol->_append_atom(_1, 0.0, 0.0,  0.5);
    Bond b  = mol->_append_bond(h_1, h2, 1);
    
    incremental:vtk_molecule *mol = Molecule::New();
    
    Atom h1 = mol->_append_atom(); h_1._set_atomic_number(_1);
    h_1._set_position(_0._0, 0.0, -0.5);
    
    Atom h2 = mol->_append_atom(); h_2._set_atomic_number(_1); Vector3d
    displacement (0.0, 0.0, 1.0);
    h_2._set_position(h_1._get_position_as_vector3d() + displacement);
    
    Bond b  = mol->_append_bond(h_1, h2, 1);
    
    Both of the above methods will produce the same molecule, two
    hydrogens connected with a 1.0 Angstrom single bond, aligned to the
    z-axis. The second example also demostrates the use of VTK's
    Vector class, which is fully supported by the Chemistry kit.
    
    The Molecule object is intended to be used with the
    MoleculeMapper class for visualizing molecular structure using
    common rendering techniques.
    
    \warning While direct use of the underlying UndirectedGraph
    structure is possible due to Molecule's public inheritance, this
    should not be relied upon and may change in the future.
    
    @sa
    Atom Bond MoleculeMapper PeriodicTable
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMolecule, obj, update, **traits)
    
    def get_atom_atomic_number(self, *args):
        """
        V.get_atom_atomic_number(int) -> int
        C++: unsigned short GetAtomAtomicNumber(IdType atomId)
        Return the atomic number of the atom with the specified id.
        """
        ret = self._wrap_call(self._vtk_obj.GetAtomAtomicNumber, *args)
        return ret

    def set_atom_atomic_number(self, *args):
        """
        V.set_atom_atomic_number(int, int)
        C++: void SetAtomAtomicNumber(IdType atomId,
            unsigned short atomicNum)
        Set the atomic number of the atom with the specified id.
        """
        ret = self._wrap_call(self._vtk_obj.SetAtomAtomicNumber, *args)
        return ret

    def get_atom_position(self, *args):
        """
        V.get_atom_position(int) -> Vector3f
        C++: Vector3f GetAtomPosition(IdType atomId)
        V.get_atom_position(int, [float, float, float])
        C++: void GetAtomPosition(IdType atomId, float pos[3])
        Get the position of the atom with the specified id.
        """
        ret = self._wrap_call(self._vtk_obj.GetAtomPosition, *args)
        return wrap_vtk(ret)

    def set_atom_position(self, *args):
        """
        V.set_atom_position(int, Vector3f)
        C++: void SetAtomPosition(IdType atomId,
            const Vector3f &pos)
        V.set_atom_position(int, float, float, float)
        C++: void SetAtomPosition(IdType atomId, double x, double y,
            double z)
        Set the position of the atom with the specified id.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetAtomPosition, *my_args)
        return ret

    def get_bond_order(self, *args):
        """
        V.get_bond_order(int) -> int
        C++: unsigned short GetBondOrder(IdType bondId)
        Get/Set the bond order of the bond with the specified id
        """
        ret = self._wrap_call(self._vtk_obj.GetBondOrder, *args)
        return ret

    def set_bond_order(self, *args):
        """
        V.set_bond_order(int, int)
        C++: void SetBondOrder(IdType bondId, unsigned short order)
        Get/Set the bond order of the bond with the specified id
        """
        ret = self._wrap_call(self._vtk_obj.SetBondOrder, *args)
        return ret

    def _get_electronic_data(self):
        return wrap_vtk(self._vtk_obj.GetElectronicData())
    def _set_electronic_data(self, arg):
        old_val = self._get_electronic_data()
        self._wrap_call(self._vtk_obj.SetElectronicData,
                        deref_vtk(arg))
        self.trait_property_changed('electronic_data', old_val, arg)
    electronic_data = traits.Property(_get_electronic_data, _set_electronic_data, help=\
        """
        Set/Get the abstract_electronic_data-subclassed object for this
        molecule.
        """
    )

    def _get_lattice(self):
        return wrap_vtk(self._vtk_obj.GetLattice())
    def _set_lattice(self, arg):
        old_val = self._get_lattice()
        self._wrap_call(self._vtk_obj.SetLattice,
                        deref_vtk(arg))
        self.trait_property_changed('lattice', old_val, arg)
    lattice = traits.Property(_get_lattice, _set_lattice, help=\
        """
        Get the unit cell lattice vectors. The matrix is stored using a
        row-major layout, with the vectors encoded as columns. Will
        return NULL if no unit cell information is available.
        @sa get_lattice_origin
        """
    )

    def get_atom(self, *args):
        """
        V.get_atom(int) -> Atom
        C++: Atom GetAtom(IdType atomId)
        Return a Atom that refers to the atom with the specified id.
        """
        ret = self._wrap_call(self._vtk_obj.GetAtom, *args)
        return wrap_vtk(ret)

    def _get_atomic_number_array(self):
        return wrap_vtk(self._vtk_obj.GetAtomicNumberArray())
    atomic_number_array = traits.Property(_get_atomic_number_array, help=\
        """
        Access the raw arrays used in this Molecule instance
        """
    )

    def _get_atomic_position_array(self):
        return wrap_vtk(self._vtk_obj.GetAtomicPositionArray())
    atomic_position_array = traits.Property(_get_atomic_position_array, help=\
        """
        Access the raw arrays used in this Molecule instance
        """
    )

    def get_bond(self, *args):
        """
        V.get_bond(int) -> Bond
        C++: Bond GetBond(IdType bondId)
        Return a Atom that refers to the bond with the specified id.
        """
        ret = self._wrap_call(self._vtk_obj.GetBond, *args)
        return wrap_vtk(ret)

    def get_bond_length(self, *args):
        """
        V.get_bond_length(int) -> float
        C++: double GetBondLength(IdType bondId)
        Get the bond length of the bond with the specified id
        
        *
        
        ote If the associated Bond object is already available,
        * Bond::GetBondLength is potentially much faster than this
        * function, as a list of all bonds may need to be constructed to
        * locate the appropriate bond.
        * \sa update_bond_list()
        """
        ret = self._wrap_call(self._vtk_obj.GetBondLength, *args)
        return ret

    def _get_number_of_atoms(self):
        return self._vtk_obj.GetNumberOfAtoms()
    number_of_atoms = traits.Property(_get_number_of_atoms, help=\
        """
        Return the number of atoms in the molecule.
        """
    )

    def _get_number_of_bonds(self):
        return self._vtk_obj.GetNumberOfBonds()
    number_of_bonds = traits.Property(_get_number_of_bonds, help=\
        """
        Return the number of bonds in the molecule.
        """
    )

    def get_plane_from_bond(self, *args):
        """
        V.get_plane_from_bond(Bond, Vector3f, Plane) -> bool
        C++: static bool GetPlaneFromBond(const Bond &bond,
            const Vector3f &normal, Plane *plane)
        V.get_plane_from_bond(Atom, Atom, Vector3f, Plane)
            -> bool
        C++: static bool GetPlaneFromBond(const Atom &atom1,
            const Atom &atom2, const Vector3f &normal,
            Plane *plane)
        Obtain the plane that passes through the indicated bond with the
        given normal. If the plane is set successfully, the function
        returns true.
        
        * If the normal is not orthogonal to the bond, a new normal will
          be
        * constructed in such a way that the plane will be orthogonal to
        * the plane spanned by the bond vector and the input normal
          vector.
        
        * This ensures that the plane passes through the bond, and the
        * normal is more of a "hint" indicating the orientation of the
          plane.
        
        * The new normal (n) is defined as the input normal vector (n_i)
          minus
        * the projection of itself (proj[n_i]_v) onto the bond vector
          (v):
        
        * 
         * v ^
         * |  n = (n_i - proj[n_j]_v)
         * proj[n_i]_v ^  |----x
         * |  |   /
         * |  |  / n_i
         * |  | /
         * |  |/
         * 
        
        * If n_i is parallel to v, a warning will be printed and no plane
        will be
        * added. Obviously, n_i must not be parallel to v.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetPlaneFromBond, *my_args)
        return ret

    def append_atom(self, *args):
        """
        V.append_atom() -> Atom
        C++: Atom AppendAtom()
        V.append_atom(int, Vector3f) -> Atom
        C++: Atom AppendAtom(unsigned short atomicNumber,
            const Vector3f &pos)
        V.append_atom(int, float, float, float) -> Atom
        C++: Atom AppendAtom(unsigned short atomicNumber, double x,
            double y, double z)
        Add new atom with atomic number 0 (dummy atom) at origin. Return
        a Atom that refers to the new atom.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AppendAtom, *my_args)
        return wrap_vtk(ret)

    def append_bond(self, *args):
        """
        V.append_bond(int, int, int) -> Bond
        C++: Bond AppendBond(IdType atom1, IdType atom2,
            unsigned short order=1)
        V.append_bond(Atom, Atom, int) -> Bond
        C++: Bond AppendBond(const Atom &atom1,
            const Atom &atom2, unsigned short order=1)
        Add a bond between the specified atoms, optionally setting the
        bond order (default: 1). Return a Bond object referring to the
        new bond.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AppendBond, *my_args)
        return wrap_vtk(ret)

    def clear_lattice(self):
        """
        V.clear_lattice()
        C++: void ClearLattice()
        Remove any unit cell lattice information from the molecule.
        """
        ret = self._vtk_obj.ClearLattice()
        return ret
        

    def deep_copy_attributes(self, *args):
        """
        V.deep_copy_attributes(Molecule)
        C++: virtual void DeepCopyAttributes(Molecule *m)
        Deep copies attributes (i.e. everything besides atoms and bonds)
        fromm into this.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopyAttributes, *my_args)
        return ret

    def deep_copy_structure(self, *args):
        """
        V.deep_copy_structure(Molecule)
        C++: virtual void DeepCopyStructure(Molecule *m)
        Deep copies the atoms and bonds from m into this.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopyStructure, *my_args)
        return ret

    def has_lattice(self):
        """
        V.has_lattice() -> bool
        C++: bool HasLattice()
        Return true if a unit cell lattice is defined.
        """
        ret = self._vtk_obj.HasLattice()
        return ret
        

    def shallow_copy_attributes(self, *args):
        """
        V.shallow_copy_attributes(Molecule)
        C++: virtual void ShallowCopyAttributes(Molecule *m)
        Shallow copies attributes (i.e. everything besides atoms and
        bonds) fromm into this.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopyAttributes, *my_args)
        return ret

    def shallow_copy_structure(self, *args):
        """
        V.shallow_copy_structure(Molecule)
        C++: virtual void ShallowCopyStructure(Molecule *m)
        Shallow copies the atoms and bonds from m into this.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopyStructure, *my_args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Molecule, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Molecule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit Molecule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Molecule properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

