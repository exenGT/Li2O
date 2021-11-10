from gpaw import GPAW, PW, FermiDirac
from ase.io import read
from ase.parallel import parprint
from ase.optimize.lbfgs import LBFGS
from ase.constraints import StrainFilter
from gpaw.xc.libvdwxc import vdw_df_cx


atoms = read("Li_atom.cif")

# atoms = read("GDY_Li_top_opt.traj")

calc = GPAW(mode=PW(450), kpts=(1,1,1), xc='PBE',
            convergence={'eigenstates': 1.e-8},
            random=True, occupations=FermiDirac(0.01), txt='Li_atom.txt')

atoms.calc = calc

