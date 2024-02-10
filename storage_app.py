import sys
import os
import data as dt
import shutil
from zipfile import ZipFile
try:
	import pynotepad as PyN1
except ImportError:
	print('pynotepad plugin doesnt exist, but you can continue use PyFiles, for install it. You have to write first !eval(for write PyCode), and then write dowland("plugin") use the strings.')
print("Welcome to PyFiles. Write !help for help.")
def s_app():
	
	def dowland(plugin):
		try:
			if plugin == "pynotepad":
				print('Not added yet')
			else:
				print('plugin doesnt exists or internet.')
		except:
			print('An Error occurred, for internet or more.')
	s_user = input("- ")
	
	if s_user == "!help":
		print("commands:\n!info, !see.dir, !kill.storage(will delete the pyfiles app for updates), !delete.file, !delete.dir, !check.zip, !delete.dir_content !see.file, !see.files, !extract.zip, !add.file, !add.dir, !change.dir, !compress.zip, !write.file(it needs PyNote plugin), !exit, !rename")
		s_app()
	elif s_user == "!kill.storage":
		print("Deleting Storage..")
		os.remove("storage_app.py")
		quit()
	elif s_user == '!exit':
		sys.exit()
	elif s_user == '!see.dir':
		path = os.getcwd()
		print(path)
		s_app()
	elif s_user == '!see.files':
		for file in os.listdir():
			print(file)
		s_app()
	elif s_user == '!change.dir':
		chdir_inp = input('change.dir- ')
		try:
			os.chdir(chdir_inp)
			s_app()
		except Exception as e:
			print(e)
			s_app()
	elif s_user == '!see.file':
		file_ins = input('see.file- ')
		try:
			file_inp = open(file_ins, 'r')
			file_txt = file_inp.read()
			print(str(file_txt))
			s_app()
		except Exception as e:
			print(e)
			s_app()
	elif s_user == '!delete.file':
		del_file = input('delete.file- ')
		try:
			os.remove(del_file)
			s_app()
		except Exception as e:
			print(e)
			s_app()
	elif s_user == '!delete.dir':
		try:
			del_dir = input('delete.dir- ')
			os.rmdir(del_dir)
			s_app()
		except Exception as e:
			print(e)
			s_app()
	elif s_user == '!info':
		print('Name: PyFiles,\nVer: 1.0,\nCredits: Python, CrystalStudios,')
		s_app()
	
	elif s_user == '!add.file':
		file_name = input('add.file_name- ')
		try:
			mkfile = open(str(file_name), 'w')
			mkfile.close()
			print('File created without errors.')
			s_app()
		except Exception as e:
			print('PyError: ' + e)
			s_app()
			
	elif s_user == '!add.dir':
			try:
				add_dirname = input('add.dir_name- ')
				os.mkdir(add_dirname)
				s_app()
			except:
				print("A error occurred.")
				s_app()		
	elif s_user == '!extract.zip':
		try:
			zip_inp = input("extract.zip- ")
			print('Your folder name when extracted.')
			zip_inp_nm = input("extract.zip_name- ")
			shutil.unpack_archive(str(zip_inp), str(zip_inp_nm))
			s_app()
		except Exception as e:
			print("PyError:" + e)
			s_app()
	elif s_user == '!delete.dir_content':
		try:
			fold_cont_inp = input('delete.dir_content- ')
			shutil.rmtree(fold_cont_inp, ignore_errors=True)
			s_app()
		except Exception as e:
			print(e)
	elif s_user == '!eval':
		try:
			eval(input('eval- '))
			s_app()
		except Exception as e:
			print(e)
			s_app()
	elif s_user == '!check.zip':
		try:
			z_file_ch = input('check.zip- ')
			z_file_cont = ZipFile(z_file_ch, 'r')
			print(z_file_cont.namelist())
			s_app()
		except:
			print('File isnt here or coding system error.')
	elif s_user == '!compress.zip':
		try:
			z_file_compr = input('compress.zip- ')
			print('Name the zip that you want compress.')
			z_file_compr_nm = input('compress.zip_name- ')
			shutil.make_archive(z_file_compr_nm, 'zip', z_file_compr)
			s_app()
		except Exception as e:
			print(e)
			s_app()
	elif s_user == '!rename':
		try:
			rn_file_i = input('remame- ')
			print('Now put the new file name.')
			rn_file_n = input('rename.file_rename- ')
			os.rename(rn_file_i, rn_file_n)
			s_app()
		except Exception as e:
			print(e)
			s_app()
	elif s_user == '!write.file':
		PyN1.open_file()
		
		
	else:
		try:
			print(s_user + ' is not a command.')
			s_app()
		except Exception as e:
			print(e)
			s_app()
s_app()	
