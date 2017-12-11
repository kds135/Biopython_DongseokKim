# Need Mfannot tbl file
# before use this script, you should change the blank '			' to @
# and erase the first line of tbl file, such as ex) >Feature C_0 Table1, and no empty space.
# for example command : mfannot_vi.py example.tbl
# After finishing this script, you can get a changed_gb_file.gb,
# and need to add the information about original format of gb file.
# CONTACT email adress : dongseokkim6662@gmail.com

import sys

input = str(sys.argv[1])

MFannot_file = open(input, 'r')
lines = MFannot_file.readlines()
result = open('changed_gb_file.gb','w')

for line in lines:
	line.strip()
	if line.find("\tgene") != -1:		
		start_1 = line.split()[0]
		end_1 = line.split()[1]
		if int(start_1) > int(end_1):
			result.write(" "*5+"gene"+" "*12+"complement"+"("+str(end_1)+".."+str(start_1)+")\n")
		else:
			result.write(" "*5+"gene"+" "*12+str(start_1)+".."+str(end_1)+"\n")		
		result.write(" "*21+"/created_by="+'"User"\n')
		result.write(" "*21+"/modified_by="+'"User"\n')
		
	elif line.find("\ttRNA") != -1:
		start_2 = line.split()[0]
		end_2 = line.split()[1]
		if int(start_2) > int(end_2):
			result.write(" "*5+"tRNA"+" "*12+"complement"+"("+str(end_2)+".."+str(start_2)+")\n")
		else:
			result.write(" "*5+"tRNA"+" "*12+str(start_2)+".."+str(end_2)+"\n")
		result.write(" "*21+"/created_by="+'"User"\n')
		result.write(" "*21+"/modified_by="+'"User"\n')
		result.write(" "*21+"/label="+'"'+str(gene_name)+'"\n')
		
	elif line.find("\tCDS") != -1:
		start_3 = line.split()[0]
		end_3 = line.split()[1]
		if int(start_3) > int(end_3):
			result.write(" "*5+"CDS"+" "*12+"complement"+"("+str(end_3)+".."+str(start_3)+")\n")
		else:
			result.write(" "*5+"CDS"+" "*12+str(start_3)+".."+str(end_3)+"\n")
		result.write(" "*21+"/created_by="+'"User"\n')
		result.write(" "*21+"/modified_by="+'"User"\n')	
		result.write(" "*21+"/label="+'"'+str(gene_name)+'"\n')
		
	elif line.find("\trRNA") != -1:	
		start_4 = line.split()[0]
		end_4 = line.split()[1]
		if int(start_4) > int(end_4):
			result.write(" "*5+"rRNA"+" "*12+"complement"+"("+str(end_4)+".."+str(start_4)+")\n")
		else:
			result.write(" "*5+"rRNA"+" "*12+str(start_4)+".."+str(end_4)+"\n")
		result.write(" "*21+"/created_by="+'"User"\n')
		result.write(" "*21+"/modified_by="+'"User"\n')		
		result.write(" "*21+"/label="+'"'+str(gene_name)+'"\n')
		
	elif line.find("@gene") != -1:
		gene_name = line.split()[1]
		result.write(" "*21+"/label="+'"'+str(gene_name)+'"\n')
	
result.close()
	
	
	
	
			