#!/usr/bin/env bash
flirt -in bet.nii.gz -ref ../../template.nii.gz -dof 12 -out T1toMNI.nii.gz -omat T1toMNI.mat -dof 12 -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -interp trilinear -v
flirt -in corr_in_t1.nii.gz -ref ../../template.nii.gz -applyxfm -init T1toMNI.mat -out corr_in_template -interp trilinear
