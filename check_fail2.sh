#!/bin/bash
#SBATCH --job-name=cf
#SBATCH --partition=sixhour
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --time=00-06:00:00
#SBATCH --output=serial_test_%j.log
#SBATCH --constraint=intel,ib

pwd; hostname; date
echo "$SLURM_ARRAY_TASK_ID"

module purge
#module load compiler/intel/18 intel-mpi/18
module load anaconda
source activate py_run
module list

fold=$SLURM_ARRAY_TASK_ID

cp check_final_slab.py ../$fold
cp complete.py ../$fold

cd ../$fold
zcat bonds.reaxc.gz | tail -n 584  > bond_tail
python check_final_slab.py > check

python complete.py > line

for i in ../[0-9]*/line; do cat $i >> line_all; done
for i in ../[0-9]*/check; do cat $i >> check_all; done
python test2.py
