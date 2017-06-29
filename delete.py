import os, shutil, time

def deleteFiles(path, deleteAll):
	if os.path.isdir(path):
		print("**Cleaning up old files in %s**\n" % path)
	else:
		print("WARNING: Directory %s does not exist\n" % path)
		return

	current_time = time.time()

	for f in sorted(os.listdir(path)):
		file_path = path + f
		created_time = os.path.getctime(file_path)
		storage_time = (current_time - created_time) // 86400

		if storage_time >= 2:
			if os.path.isfile(file_path):
				if deleteAll:
					print("Removing %s (File maturity: %d days)" % (f, storage_time))
					try:
						os.remove(file_path)
					except OSError as e:
						print ("Error: %s - %s." % (e.filename,e.strerror))
				
				elif f.endswith(".log") and f != "install.log":
					print("Removing %s (File maturity: %d days)" % (f, storage_time))
					try:
						os.remove(file_path)
					except OSError as e:
						print ("Error: %s - %s." % (e.filename,e.strerror))

			elif os.path.isdir(file_path) and deleteAll and len(os.listdir(path)) > 10:
				print("Removing %s (File maturity: %d days)" % (f, storage_time))
				try:
					shutil.rmtree(file_path)
				except OSError as e:
					print ("Error: %s - %s." % (e.filename,e.strerror))
if "LAWDIR" in os.environ:
	installer_path = os.environ['LAWDIR'] + "/system/backup/"	
	log_path = os.environ['LAWDIR'] + "/system/"

	deleteFiles(installer_path, True)
	deleteFiles(log_path, False)
else:
	print("ERROR: LAWDIR is not set. Please set LAWDIR before running this script.")