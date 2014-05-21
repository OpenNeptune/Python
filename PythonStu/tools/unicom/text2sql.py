import fileinput

for line in fileinput.input("c:\\2.txt"):
	lists = line.replace('  ',' ').split(' ')
	sql = "update tbl_main_sheet t set t.assign_complete_time='" +lists[1]+" "+lists[2]+"' where t.main_sheet_flow_no='"+lists[0]+"';"
	print sql