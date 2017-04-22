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


class PolynomialSolversUnivariate(Object):
    """
    PolynomialSolversUnivariate - polynomial solvers
    
    Superclass: Object
    
    PolynomialSolversUnivariate provides solvers for univariate
    polynomial equations with real coefficients. The Tartaglia-Cardan and
    Ferrari solvers work on polynomials of fixed degree 3 and 4,
    respectively. The Lin-Bairstow and Sturm solvers work on polynomials
    of arbitrary degree. The Sturm solver is the most robust solver but
    only reports roots within an interval and does not report
    multiplicities. The Lin-Bairstow solver reports multiplicities.
    
    For difficult polynomials, you may wish to use filter_roots to
    eliminate some of the roots reported by the Sturm solver. filter_roots
    evaluates the derivatives near each root to eliminate cases where a
    local minimum or maximum is close to zero.
    
    @par Thanks: Thanks to Philippe Pebay, Korben Rusek, David Thompson,
    and Maurice Rojas for implementing these solvers.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolynomialSolversUnivariate, obj, update, **traits)
    
    division_tolerance = traits.Float(1e-08, enter_set=True, auto_set=False, help=\
        """
        Set/get the tolerance used when performing polynomial Euclidean
        division to find polynomial roots. This tolerance is used to
        decide whether the coefficient(s) of a polynomial remainder are
        close enough to zero to be neglected.
        """
    )

    def _division_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDivisionTolerance,
                        self.division_tolerance)

    def ferrari_solve(self, *args):
        """
        V.ferrari_solve([float, ...], [float, ...], [int, ...], float)
            -> int
        C++: static int FerrariSolve(double *c, double *r, int *m,
            double tol)
        Algebraically extracts REAL roots of the quartic polynomial with
        REAL coefficients X^4 + c[0] X^3 + c[1] X^2 + c[2] X + c[3] and
        stores them (when they exist) and their respective multiplicities
        in the r and m arrays, based on Ferrari's method. Some numerical
        noise can be filtered by the use of a tolerance tol instead of
        equality with 0 (one can use, e.g., VTK_DBL_EPSILON). Returns the
        number of roots. Warning: it is the user's responsibility to pass
        a non-negative tol.
        """
        ret = self._wrap_call(self._vtk_obj.FerrariSolve, *args)
        return ret

    def filter_roots(self, *args):
        """
        V.filter_roots([float, ...], int, [float, ...], int, float) -> int
        C++: static int FilterRoots(double *P, int d, double *upperBnds,
            int rootcount, double diameter)
        This uses the derivative sequence to filter possible roots of a
        polynomial. First it sorts the roots and removes any duplicates.
        If the number of sign changes of the derivative sequence at a
        root at upper_bnds[i] == that at upper_bnds[i]  - diameter then the
        i^th value is removed from upper_bnds. It returns the new number
        of roots.
        """
        ret = self._wrap_call(self._vtk_obj.FilterRoots, *args)
        return ret

    def habicht_bisection_solve(self, *args):
        """
        V.habicht_bisection_solve([float, ...], int, [float, ...], [float,
            ...], float) -> int
        C++: static int HabichtBisectionSolve(double *P, int d, double *a,
             double *upperBnds, double tol)
        V.habicht_bisection_solve([float, ...], int, [float, ...], [float,
            ...], float, int) -> int
        C++: static int HabichtBisectionSolve(double *P, int d, double *a,
             double *upperBnds, double tol, int intervalType)
        V.habicht_bisection_solve([float, ...], int, [float, ...], [float,
            ...], float, int, bool) -> int
        C++: static int HabichtBisectionSolve(double *P, int d, double *a,
             double *upperBnds, double tol, int intervalType,
            bool divideGCD)
        Finds all REAL roots (within tolerance tol) of the d -th degree
        polynomial\[ P[0] X^d + ... + P[d-1] X + P[d]\] in ] a[0] ; a[1]]
        using the Habicht sequence (polynomial coefficients are REAL) and
        returns the count nr. All roots are bracketed in the
        
        r first ] upper_bnds[i] - tol ; upper_bnds[i]] intervals. Returns
        -1 if anything went wrong (such as: polynomial does not have
        degree d, the interval provided by the other is absurd, etc.).
        
        * interval_type specifies the search interval as follows:
        * 0 = 00 = ]a,b[
        * 1 = 10 = [a,b[
        * 2 = 01 = ]a,b]
        * 3 = 11 = [a,b]
        * This defaults to 0.
        
        * The last non-zero item in the Habicht sequence is the gcd of P
          and P'. The
        * parameter divide_gcd specifies whether the program should
          attempt to divide
        * by the gcd and run again. It works better with polynomials
          known to have
        * high multiplicities. When divide_gcd != 0 then it attempts to
          divide by the
        * GCD, if applicable. This defaults to 0.
        
        * Compared to the Sturm solver the Habicht solver is slower,
        * although both are O(d^2). The Habicht solver has the added
          benefit
        * that it has a built in mechanism to keep the leading
          coefficients of the
        * result from polynomial division bounded above and below in
          absolute value.
        * This will tend to keep the coefficients of the polynomials in
          the sequence
        * from zeroi ...
         [Truncated]
        """
        ret = self._wrap_call(self._vtk_obj.HabichtBisectionSolve, *args)
        return ret

    def lin_bairstow_solve(self, *args):
        """
        V.lin_bairstow_solve([float, ...], int, [float, ...], float) -> int
        C++: static int LinBairstowSolve(double *c, int d, double *r,
            double &tolerance)
        Seeks all REAL roots of the d -th degree polynomial c[0] X^d +
        ... + c[d-1] X + c[d] = 0 equation Lin-Bairstow's method (
        polynomial coefficients are REAL ) and stores the nr roots found
        ( multiple roots are multiply stored ) in r.tolerance is the
        user-defined solver tolerance; this variable may be relaxed by
        the iterative solver if needed. Returns nr. Warning: it is the
        user's responsibility to make sure the r array is large enough to
        contain the maximal number of expected roots.
        """
        ret = self._wrap_call(self._vtk_obj.LinBairstowSolve, *args)
        return ret

    def solve_cubic(self, *args):
        """
        V.solve_cubic(float, float, float, float) -> (float, ...)
        C++: static double *SolveCubic(double c0, double c1, double c2,
            double c3)
        V.solve_cubic(float, float, float, float, [float, ...], [float,
            ...], [float, ...], [int, ...]) -> int
        C++: static int SolveCubic(double c0, double c1, double c2,
            double c3, double *r1, double *r2, double *r3, int *num_roots)
        Solves a cubic equation c0*t^3 + c1*t^2 + c2*t + c3 = 0 when c0,
        c1, c2, and c3 are REAL.  Solution is motivated by Numerical
        Recipes In C 2nd Ed.  Return array contains number of (real)
        roots (counting multiple roots as one) followed by roots
        themselves. The value in roots[4] is a integer giving further
        information about the roots (see return codes for int
        solve_cubic() ).
        """
        ret = self._wrap_call(self._vtk_obj.SolveCubic, *args)
        return ret

    def solve_linear(self, *args):
        """
        V.solve_linear(float, float) -> (float, ...)
        C++: static double *SolveLinear(double c0, double c1)
        V.solve_linear(float, float, [float, ...], [int, ...]) -> int
        C++: static int SolveLinear(double c0, double c1, double *r1,
            int *num_roots)
        Solves a linear equation c2*t  + c3 = 0 when c2 and c3 are REAL.
        Solution is motivated by Numerical Recipes In C 2nd Ed. Return
        array contains number of roots followed by roots themselves.
        """
        ret = self._wrap_call(self._vtk_obj.SolveLinear, *args)
        return ret

    def solve_quadratic(self, *args):
        """
        V.solve_quadratic(float, float, float) -> (float, ...)
        C++: static double *SolveQuadratic(double c0, double c1,
            double c2)
        V.solve_quadratic(float, float, float, [float, ...], [float, ...],
            [int, ...]) -> int
        C++: static int SolveQuadratic(double c0, double c1, double c2,
            double *r1, double *r2, int *num_roots)
        V.solve_quadratic([float, ...], [float, ...], [int, ...]) -> int
        C++: static int SolveQuadratic(double *c, double *r, int *m)
        Solves a quadratic equation c1*t^2 + c2*t + c3 = 0 when c1, c2,
        and c3 are REAL.  Solution is motivated by Numerical Recipes In C
        2nd Ed. Return array contains number of (real) roots (counting
        multiple roots as one) followed by roots themselves. Note that
        roots[3] contains a return code further describing solution - see
        documentation for solve_cubic() for meaning of return codes.
        """
        ret = self._wrap_call(self._vtk_obj.SolveQuadratic, *args)
        return ret

    def sturm_bisection_solve(self, *args):
        """
        V.sturm_bisection_solve([float, ...], int, [float, ...], [float,
            ...], float) -> int
        C++: static int SturmBisectionSolve(double *P, int d, double *a,
            double *upperBnds, double tol)
        V.sturm_bisection_solve([float, ...], int, [float, ...], [float,
            ...], float, int) -> int
        C++: static int SturmBisectionSolve(double *P, int d, double *a,
            double *upperBnds, double tol, int intervalType)
        V.sturm_bisection_solve([float, ...], int, [float, ...], [float,
            ...], float, int, bool) -> int
        C++: static int SturmBisectionSolve(double *P, int d, double *a,
            double *upperBnds, double tol, int intervalType,
            bool divideGCD)
        Finds all REAL roots (within tolerance tol) of the d -th degree
        polynomial P[0] X^d + ... + P[d-1] X + P[d] in ] a[0] ; a[1]]
        using Sturm's theorem ( polynomial coefficients are REAL ) and
        returns the count nr. All roots are bracketed in the
        
        r first ] upper_bnds[i] - tol ; upper_bnds[i]] intervals. Returns
        -1 if anything went wrong (such as: polynomial does not have
        degree d, the interval provided by the other is absurd, etc.).
        
        * interval_type specifies the search interval as follows:
        * 0 = 00 = ]a,b[
        * 1 = 10 = [a,b[
        * 2 = 01 = ]a,b]
        * 3 = 11 = [a,b]
        * This defaults to 0.
        
        * The last non-zero item in the Sturm sequence is the gcd of P
          and P'. The
        * parameter divide_gcd specifies whether the program should
          attempt to divide
        * by the gcd and run again. It works better with polynomials
          known to have
        * high multiplicities. When divide_gcd != 0 then it attempts to
          divide by the
        * GCD, if applicable. This defaults to 0.
        
        * Constructing the Sturm sequence is O(d^2) in both time and
          space.
        
        * Warning: it is the user's responsibility to make sure the
          upper_bnds
        * array is large enough to contain the maximal number of expected
        roots.
        * Note that nr is smaller or equal to the actual number of roots
          in
        * ] a[0] ; a[1]] since roots within \tol are lumped in the same
          bracket.
        * array is large enough to contain the ma ...
         [Truncated]
        """
        ret = self._wrap_call(self._vtk_obj.SturmBisectionSolve, *args)
        return ret

    def tartaglia_cardan_solve(self, *args):
        """
        V.tartaglia_cardan_solve([float, ...], [float, ...], [int, ...],
            float) -> int
        C++: static int TartagliaCardanSolve(double *c, double *r, int *m,
             double tol)
        Algebraically extracts REAL roots of the cubic polynomial with
        REAL coefficients X^3 + c[0] X^2 + c[1] X + c[2] and stores them
        (when they exist) and their respective multiplicities in the r
        and m arrays. Some numerical noise can be filtered by the use of
        a tolerance tol instead of equality with 0 (one can use, e.g.,
        VTK_DBL_EPSILON). The main differences with solve_cubic are that
        (1) the polynomial must have unit leading coefficient, (2)
        complex roots are discarded upfront, (3) non-simple roots are
        stored only once, along with their respective multiplicities, and
        (4) some numerical noise is filtered by the use of relative
        tolerance instead of equality with 0. Returns the number of
        roots. In memoriam Niccolo Tartaglia (1500 - 1559), unfairly
        forgotten.
        """
        ret = self._wrap_call(self._vtk_obj.TartagliaCardanSolve, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('division_tolerance',
    'GetDivisionTolerance'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'division_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolynomialSolversUnivariate, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolynomialSolversUnivariate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['division_tolerance']),
            title='Edit PolynomialSolversUnivariate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolynomialSolversUnivariate properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

