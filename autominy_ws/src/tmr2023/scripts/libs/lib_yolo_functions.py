#! /usr/bin/env python

def yolo_roi(C, x0, y0):
	x1, y1, x2, y2, x3, y3, x4, y4 = C
	# Verifica si el punto esta dentro del rectangulo que contiene al cuadrilatero
	x_min = min(x1, x2, x3, x4)
	x_max = max(x1, x2, x3, x4)
	y_min = min(y1, y2, y3, y4)
	y_max = max(y1, y2, y3, y4)
	if x0 < x_min or x0 > x_max or y0 < y_min or y0 > y_max: return False
	"""
	# Ordena los puntos de izquierda a derecha
	points = sorted([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
	x1, y1 = points[0]
	x2, y2 = points[1]
	x3, y3 = points[2]
	x4, y4 = points[3]
	"""
	# Encuentra las ecuaciones de las lineas
	m1 = (y1-y2)/(x1-x2)
	b1 = y1-m1*x1
	m2 = (y4-y3)/(x4-x3)
	b2 = y3-m2*x3
	# Evalua el punto en las ecuaciones de las lineas
	if (y0>=m1*x0+b1) and (y0>=m2*x0+b2): return True
	else: return False


