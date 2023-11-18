#!/usr/bin/env python
import subprocess

build_command_list = ["vmd", "-dispdev", "text", "-e", "build.vmd"]
output = subprocess.check_output(build_command_list, text=True)
vmd_output_file=open("vmd_output",'w')
vmd_output_file.write(output)
vmd_output_file.close()
