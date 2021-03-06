def execute():
	import webnotes
	webnotes.reload_doc("hr", "doctype", "leave_application")
	
	webnotes.conn.sql("""update `tabLeave Application`, `tabEmployee` set
		`tabLeave Application`.company = `tabEmployee`.company where
		`tabLeave Application`.employee = `tabEmployee`.name""")
		
	company = webnotes.conn.get_default("company")
	if company:
		webnotes.conn.sql("""update `tabLeave Application`
			set company = %s where ifnull(company,'')=''""", company)