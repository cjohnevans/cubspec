function [spectro] = cubspec_fida_proc( spectro_file_list , water_file_list, legend_info, write_jmrui, ...
    write_dir)
%  basic preprocessing for semi-laser 7T data using FID-A
%    spectro_file_list: cell array of files to load
%    legend_info:       cell array of text labels for plot
%    write_jmrui:       write jmrui file (for tarquin).  true/false
%    write_dir:         specify the write directory

n_files = length(spectro_file_list);

% offset value for plotting
offset_val = 2 * 10 .^ (-7);


for file = 1:n_files
    if water_file_list{1}
        disp(strcat('io_loadspec_twix ', spectro_file_list{file}, ' ', water_file_list{file}))
        spectro{file} = io_loadspec_twix(spectro_file_list{file});
        water{file} = io_loadspec_twix(water_file_list{file});
        spectro{file}, water{file} = op_combineRcvrs(spectro{file}, water{file})
        spectro{file} = op_addrcvrs(spectro{file}, 1, 'w')
        disp('op_combineRcvrs')
    else
        disp(strcat('io_loadspec_twix ', spectro_file_list{file}, ' '))
        spectro{file} = io_loadspec_twix(spectro_file_list{file});
        spectro{file} = op_addrcvrs(spectro{file}, 1, 'w');
        disp('op_addrcvrs')
    end
    
    spectro{file} = op_alignAverages(spectro{file});
    spectro{file} = op_averaging(spectro{file});
    %spectro_ph = op_addphase(spectro, -55, -0.00032, 2,0) % phase relative to naa, wand
    spectro{file} = op_addphase(spectro{file}, -55, -0.00020, 2,1); % phase relative to naa, thal
    %spectro_ph = op_addphase(spectro, 0, -0.00000, 2,1) % phase relative to naa, thal
    
    offset = repmat(([1:n_files ] * offset_val), [length(spectro{file}.specs), 1]); 
    disp('Length of spec')
    disp(length(spectro{file}.specs))
    spec_plot(:,file) = spectro{file}.specs + offset(:, file);
    if write_jmrui
        out_file = strcat(write_dir, legend_info{file}, '.jmrui')
        io_writejmrui(spectro{file}, out_file);
    end
        
end
    
figure(4)
plot(-spectro{1}.ppm, real(spec_plot))
axis([-5 0 min(min(real(spec_plot))) max(max(real(spec_plot))) ] )
legend(legend_info)

