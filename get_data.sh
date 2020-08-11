#!/bin/bash
#SBATCH --job-name=conn
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

for i in ../[0-9]*/struc_conn/final_dp; do cat $i >> final_dp_all; done
for i in ../[0-9]*/struc_conn/z_dp; do cat $i >> z_dp_all; done
for i in ../[0-9]*/struc_conn/sp; do cat $i >> sp_all; done

for i in ../[0-9]*/struc_conn/c_Si; do cat $i >> c_Si_all; done
for i in ../[0-9]*/struc_conn/c_O; do cat $i >> c_O_all; done

for i in ../[0-9]*/struc_conn/sio; do cat $i >> sio_all; done
for i in ../[0-9]*/struc_conn/siosi; do cat $i >> siosi_all; done
for i in ../[0-9]*/struc_conn/osio; do cat $i >> osio_all; done
for i in ../[0-9]*/struc_conn/ring_stats; do cat $i >> ring_stats_all; done
for i in ../[0-9]*/struc_conn/cn; do cat $i >> cn_all; done

for i in ../[0-9]*/struc_conn/Si_z_3; do cat $i >> Si_z_3_all; done
for i in ../[0-9]*/struc_conn/Si_z_5; do cat $i >> Si_z_5_all; done



python bin.py -i sio_all -m1 0 -m2 3 > sio_density.dat
python bin.py -i siosi_all -m1 0 -m2 180 > siosi_density.dat
python bin.py -i osio_all -m1 0 -m2 180 > osio_density.dat
python bin.py -i cn_all -m1 -40 -m2 40 > cn.dat
python bin.py -i Si_z_3_all -m1 -40 -m2 40 > Si3_z.dat
python bin.py -i Si_z_5_all -m1 -40 -m2 40 > Si5_z.dat
python bin.py -i c_Si_all -m1 -5 -m2 5 > cSi.dat
python bin.py -i c_O_all -m1 -5 -m2 5 > cO.dat
python avg_ring.py > ring.dat
python avg_single.py -i sio_all > sio_avg
python avg_single.py -i siosi_all > siosi_avg
python avg_single.py -i osio_all > osio_avg
python avg_single.py -i Si_z_3_all > si_3_z_avg
python avg_single.py -i Si_z_5_all > si_5_z_avg
python avg_single.py -i c_Si_all > cSi_avg
python avg_single.py -i c_O_all > cO_avg
python avg_cn.py > cn_avg
python avg_dp.py > z_dp.dat
