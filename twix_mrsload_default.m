% using FID-A
% initially a script, by may want to be a function


dat_path = '/home/sapje1/data_sapje1/projects/wand/mrs_7t/'
f_met = 'meas_MID38_slaser_SMleft_met_FID106067.dat'
f_wat = 'meas_MID40_slaser_SMleft_ref_FID106069.dat'

path_met = strcat(dat_path, f_met)
path_wat = strcat(dat_path, f_wat)

%met = mapVBVD(path_met);
%wat = mapVBVD(path_wat);

met = io_loadspec_twix(path_wat)

%[met_comb, wat_comb] = op_combineRcvrs(met, wat);

