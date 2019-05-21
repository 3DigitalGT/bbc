import time
from report import report_sxw
class examnn(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context):
		super(examnn, self).__init__(cr, uid, name, context)
		self.localcontext.update({
		'time': time,
		})
report_sxw.report_sxw('report.sale.order.Carta_de_Endoso', 'sale.order',
			'addons/BBCV/report/Carta_de_Endoso.rml', parser=examnn, header=False)
report_sxw.report_sxw('report.sale.order.Carta_de_Trazabilidad', 'sale.order',
			'addons/BBCV/report/Carta_de_Trazabilidad.rml', parser=examnn, header=False)
report_sxw.report_sxw('report.sale.order.Carta_de_Liberacion', 'sale.order',
			'addons/BBCV/report/Carta_de_Liberacion.rml', parser=examnn, header=False)

