#!/bin/bash
#SBATCH --job-name=conn
#SBATCH --partition=sixhour
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --time=00-06:00:00
#SBATCH --output=serial_test_%j.log
#SBATCH --constraint=intel,ib
#SBATCH --array=1-100

pwd; hostname; date
echo "$SLURM_ARRAY_TASK_ID"

module purge
#module load compiler/intel/18 intel-mpi/18
module load anaconda
source activate py_run
module list

fold=$SLURM_ARRAY_TASK_ID

cp -r struc_conn ../$fold


cd ../$fold
#zcat bonds.reaxc.gz | tail -n 584  > bond_tail
zcat traj.lammpstrj.gz | tail -n 585 > final.lammpstrj
tail -n 84 density.profile.gz > final_dp

zcat stress_profile.gz | tail -n 585 > final_stress


zcat dump_charge.gz | tail -n 585 > final_charge


#mv bond_tail struc_conn
mv final* struc_conn

cd struc_conn

python map_conn100.py -tr final.lammpstrj -f 585 -c 2.4 -t slab > bond_tail

python sio_conn100.py -i bond_tail -tr final.lammpstrj -f1 584 -f2 585 -t slab > sio
python siosi_conn100.py -i bond_tail -tr final.lammpstrj -f1 584 -f2 585 -t slab > siosi
python osio_conn100.py -i bond_tail -tr final.lammpstrj -f1 584 -f2 585 -t slab > osio

python conn100.py -i bond_tail -tr final.lammpstrj -f1 584 -f2 585 -t slab > ring_stats

python CN_conn100.py -i bond_tail -f 584 > cn
python over_underCN.py -i bond_tail -tr final.lammpstrj -t 1 -cn 3 > Si_z_3
python over_underCN.py -i bond_tail -tr final.lammpstrj -t 1 -cn 5 > Si_z_5


python bin_dp.py > z_dp
python sp.py > sp
python charge.py -i final_charge -t 1 > c_Si
python charge.py -i final_charge -t 2 > c_O

