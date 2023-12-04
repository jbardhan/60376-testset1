#!/bin/bash

#SBATCH --job-name=0_0/model_compound
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --output=/home/bard415/repos/60376-testset1/testing-writing-subdirs/0_0/model_compound/foo.output
#SBATCH --error=/home/bard415/repos/60376-testset1/testing-writing-subdirs/0_0/model_compound/foo.error
#SBATCH --account=emsla60376

cd /home/bard415/repos/60376-testset1/testing-writing-subdirs/0_0/model_compound
singularity exec --bind /run/user /tahoma/emsla60376/containers/apbs/apbs_singularity_ubuntu.sif /usr/local/bin/apbs apbs.in

