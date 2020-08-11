#!/bin/bash
#SBATCH --job-name=conn
#SBATCH --partition=sixhour
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --time=00-06:00:00
#SBATCH --output=serial_test_%j.log
#SBATCH --constraint=intel,ib
#SBATCH --array=1-10

pwd; hostname; date
echo "$SLURM_ARRAY_TASK_ID"

module purge
#module load compiler/intel/18 intel-mpi/18
module load anaconda
source activate py_run
module list

fold=$SLURM_ARRAY_TASK_ID

cp over_underCN.py ../$fold

cd ../$fold

tail -n 585 traj_cool.lammpstrj > final.lammpstrj
tail -n 584 bonds_cool.reaxc > bond_tail
python over_underCN.py -i bond_tail -tr final.lammpstrj -t 1 -cn 3 > Si_z_3
python over_underCN.py -i bond_tail -tr final.lammpstrj -t 1 -cn 5 > Si_z_5
