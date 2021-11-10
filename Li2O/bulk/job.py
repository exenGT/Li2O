from gpaw import GPAW, PW, FermiDirac
from ase.io import read
from ase.parallel import parprint
from ase.optimize.lbfgs import LBFGS
from ase.constraints import StrainFilter
from gpaw.xc.libvdwxc import vdw_df_cx


atoms = read("Li2O.cif")

# atoms = read("GDY_Li_top_opt.traj")

calc = GPAW(mode=PW(450), kpts=(6,6,6), xc='PBE',
            convergence={'eigenstates': 1.e-8},
            random=True, occupations=FermiDirac(0.01), txt='Li2O_opt.txt')

atoms.calc = calc

sf = StrainFilter(atoms)
relax = LBFGS(sf, logfile='Li2O_cell_opt.log', trajectory='Li2O_cell_opt.traj')
relax.run(fmax=0.02)
