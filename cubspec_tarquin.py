# cubspec_tarquin.py
#  analyse sLASER, STEAM, data with Tarqui
#  process a directory of jmrui files, created by FID-A
# example usage in IDLE3:
#  >>> import cubspec_tarquin as tq
#  >>> bbb  = tq.CubspecTarquin('/home/sapje1/data_sapje1/projects/476_bbbcov/proc/', 'jmrui')
#       ['CAU002N004.jmrui', 'oxford018.jmrui', 'oxford017.jmrui', '220315_pilot.jmrui', 'CAU002N001.jmrui', '220401_pilot.jmrui', 'CAU002N002.jmrui']
#  >>> bbb.write_para()
#       Writing tarquin.para
#  >>> bbb.run_tarquin()


import os
#input_dir = '/home/sapje1/data_sapje1/projects/476_bbbcov/proc/'
# input_type = 'jmrui'

class CubspecTarquin(object):
    '''
    Class of Tarquin helper functions.  Operates on a directory of valid
      Tarquin input files (e.g. Siemens DICOM, jmrui from FID-A)
    Requires input files to be located in a single directory, for example
    as an output from cubspec.fida_proc.m matlab script
    '''
    def __init__(self, input_dir, input_type):
        self.input_dir = input_dir
        self.input_type = input_type
        temp_file_list = os.listdir(input_dir)
        self.file_list = []
        for file in temp_file_list:
            if '.jmrui' in file:
                self.file_list.append(file)
        print(self.file_list)

    def write_para(self):
        '''
        write tarquin parameter file
        '''
        para_file = os.path.join(self.input_dir, 'tarquin.para')
        print('Writing tarquin.para\n')
        f = open(para_file, 'w') #overwrite existing
        f.write('#  tarquin parameter file - generated by CubspecTarquin\n')
        f.write('#  for use when FID-A has been used for pre-processing and data written out in\n')
        f.write('#  jmrui file.  Specify this file with --para_file parameter.\n')
        f.write('format jmrui_txt\n')
        f.write('pul_seq slaser\n')
        f.write('fs 4000.000000\n')
        f.write('ft 123253382.000000\n')
        f.write('echo 0.026000\n')
        f.write('lipid_filter true\n')
        f.write('auto_phase true\n')
        f.write('auto_ref true\n')
        f.write('ref_signals 1h_naa_cr_cho\n')
        f.write('dref_signals 1h_cr\n')
        f.write('int_basis 1h_brain_glth\n')
        f.write('water_eddy true\n')
        f.write('w_conc 1\n')
        f.write('w_att 1\n')
        f.write('ext_pdf true\n')
        f.write('# need so specify the following at the command line\n')
        f.write('#  --input\n')
        f.write('#  --input_w (if water referencing)\n')
        f.write('#  --output_pdf FILENAME.PDF --ext_pdf (for extended pdf output)\n')
        f.write('#  --output_txt (for text output)\n')
        f.close()

    def run_tarquin(self):
        '''
        run_tarquin()
        use input file list defined in __init__ and para_file defined by write_para fo
        run tarquin analysis
        '''
        for ff in self.file_list:
            file_root = ff.split('.')[0]  # filename, without extension
            tarquin_cmd = 'tarquin --para_file ' \
                           + self.input_dir + 'tarquin.para ' \
                           + ' --input ' \
                           + self.input_dir + ff \
                           + ' --output_pdf ' \
                           + self.input_dir + file_root + '.pdf' \
                           + ' --output_csv ' \
                           + self.input_dir + file_root + '.csv' \
                           + ' --output_txt ' \
                           + self.input_dir + file_root + '.txt'
            print('Running tarquin on ' + ff)
            os.system(tarquin_cmd)    





