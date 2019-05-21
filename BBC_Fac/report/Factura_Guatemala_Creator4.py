import time
from report import report_sxw
class examy(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context):
		super(examy, self).__init__(cr, uid, name, context)
		self.localcontext.update({
		'time': time,
		})
report_sxw.report_sxw('report.account.invoice.Invoice_Panama_consolidado', 'account.invoice',
			'addons/BBC_Fac/report/Invoice_Guatemala_Panama_Consolidado.rml', parser=examy, header=False)
report_sxw.report_sxw('report.account.invoice.Nota_Cobro_Panama_consolidado', 'account.invoice',
			'addons/BBC_Fac/report/Invoice_Guatemala_Panama_Consolidado_es.rml', parser=examy, header=False)
report_sxw.report_sxw('report.account.invoice.Nota_Cobro_Panama', 'account.invoice',
			'addons/BBC_Fac/report/Invoice_Guatemala_Panama_es.rml', parser=examy, header=False)

