#!/bin/bash
#SBATCH --job-name=dp
#SBATCH --partition=sixhour
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --time=00-06:00:00
#SBATCH --output=serial_test_%j.log
#SBATCH --constraint=intel
#SBATCH --array=1-100

pwd; hostname; date
echo "$SLURM_ARRAY_TASK_ID"

module purge
#module load compiler/intel/18 intel-mpi/18
module load anaconda
source activate py_run
module list

fold=$SLURM_ARRAY_TASK_ID
cp bin_dp.py ../$fold


cd ../$fold
tail -n 84 density.profile.gz > final_dp
#zcat density.profile.gz | tail -n 84 > final_dp
python bin_dp.py > z_dp


