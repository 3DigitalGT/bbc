import time
import datetime
from report import report_sxw
class examqw(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context):
		super(examqw, self).__init__(cr, uid, name, context)
		self.localcontext.update({
		'time': time,
		'datetime' : datetime,
		'get__value_sel' : self._get_value_from_selection_field,
		'_do_nothing' : self._do_nothing,
		'prueba' : self.prueba,
		'_do_whatever' : self._do_whatever,

		'_do_anything' : self._do_anything,
		})


	def prueba(self, cr,uid,field,arg,context=None):
		return str('sucker')

	def _get_value_from_selection_field(self, model, field, value):
		selection = self.pool.get(model)
		res = ''
		return str(selection.name)

	def _do_nothing(list):
		return "fucker nothing"
	def _do_whatever(object):
		return "fucker whatever"

	def _do_anything(object):
		return "fucker1 anything"
report_sxw.report_sxw('report.sale.order.HBL_Report', 'sale.order',
			'addons/BBC_Fac/report/HBL_REPORT.rml', parser=examqw, header=False)
report_sxw.report_sxw('report.sale.order.MBL_Report', 'sale.order',
			'addons/BBC_Fac/report/MBL_REPORT.rml', parser=examqw, header=False)
report_sxw.report_sxw('report.sale.order.Not_Zarpe', 'sale.order',
			'addons/BBC_Fac/report/Not_Zarpe.rml', parser=examqw, header=False)
report_sxw.report_sxw('report.sale.order.Not_Arribo', 'sale.order',
			'addons/BBC_Fac/report/Not_Arribo.rml', parser=examqw, header=False)
report_sxw.report_sxw('report.sale.order.Routing_order_info', 'sale.order',
			'addons/BBC_Fac/report/Routing_order_info.rml', parser=examqw, header=False)
report_sxw.report_sxw('report.sale.order.Not_pre_Zarpe', 'sale.order',
			'addons/BBC_Fac/report/Not_pre_Zarpe.rml', parser=examqw, header=False)
report_sxw.report_sxw('report.sale.order.Not_pre_Arribo', 'sale.order',
			'addons/BBC_Fac/report/Not_pre_Arribo.rml', parser=examqw, header=False)

