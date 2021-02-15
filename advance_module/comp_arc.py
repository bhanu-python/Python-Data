#if we have to do complete dir to zip file

import shutil

#archive the dir using shutil

dir_to_arch='d:\Learning data\Python-Data\/advance_module\extract_cont'
op_name='test_two'
shutil.make_archive(op_name,'zip',dir_to_arch)

#unzip the file

shutil.unpack_archive('test_two.zip','shutil_extract','zip')
