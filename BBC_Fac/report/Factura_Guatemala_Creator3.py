import time
from report import report_sxw
class examz(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context):
		super(examz, self).__init__(cr, uid, name, context)
		self.localcontext.update({
		'time': time,
		})
report_sxw.report_sxw('report.account.invoice.Invoice_Panama', 'account.invoice',
			'addons/BBC_Fac/report/Invoice_Guatemala_Panama.rml', parser=examz, header=False)

