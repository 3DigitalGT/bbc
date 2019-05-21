import time
import num2words
import datetime
from report import report_sxw
class examw(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context):
		super(examw, self).__init__(cr, uid, name, context)
		self.localcontext.update({
		'time': time,
		'num2words' : num2words,
		'convertir_int' : self.convertir_int,
		'obtener_decimales' : self.obtener_decimales,
		'datetime' : datetime,
		'suma_fechas' : self.suma_fechas,
		})
	def convertir_int(self,monito):
		return num2words.num2words(int(monito),lang='esp')

	def obtener_decimales(self,monito):
		b=float(monito)
		a=float('%.2f' %b)
		#a = int((float('%.2f' %b) - float(int(float('%.2f' %b))) )*  10.0)
		number_dec = str(a-int(a))[2:4]
		return number_dec + "/100"

	def suma_fechas(self,fecha,delay):
		dt_obj = datetime.datetime.strptime(fecha, "%d-%m-%Y")
		try:
			nueva_fecha =  dt_obj +  datetime.timedelta(days=int(delay))
		except:
			nueva_fecha =  dt_obj +  datetime.timedelta(days=int(0))
		finally:
			print nueva_fecha
		#return type(nueva_fecha), "DELAY", delay ,nueva_fecha, nueva_fecha.strftime('%d-%m-%Y')
		return nueva_fecha.strftime('%d-%m-%Y')

report_sxw.report_sxw('report.account.invoice.Fact_Guatemala_Consolidado', 'account.invoice',
			'addons/BBC_Fac/report/OpenERP-Factura_Guatemala_consolidado.rml', parser=examw, header=False)

