from gpaw import GPAW, PW, FermiDirac
from ase.io import read
from ase.parallel import parprint
from ase.optimize.lbfgs import LBFGS
from ase.constraints import StrainFilter
from gpaw.xc.libvdwxc import vdw_df_cx


#atoms = read("Li.cif")

atoms = read("Li_cell_opt.traj")

calc = GPAW(mode=PW(500), kpts=(11,11,11), xc='PBE',
            convergence={'eigenstates': 1.e-8},
            random=True, occupations=FermiDirac(0.03), txt='Li_opt_2.txt')

atoms.calc = calc

sf = StrainFilter(atoms)
relax = LBFGS(sf, logfile='Li_cell_opt_2.log', trajectory='Li_cell_opt_2.traj')
relax.run(fmax=0.02)
