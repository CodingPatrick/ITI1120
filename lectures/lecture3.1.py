import math

def area_or_triangle(base, heigt):
	area=base*heigt/2
	return area

def area_or_triangle_v2(base, heigt):
	return base*heigt/2

def area_of_circle(radius):
    area=radius**2*math.pi
    return area

def s_to_ms(s):
    m = s // 60
    #s=s-m*60 is the same as:
    s = s % 60
    return (m,s)
    
def s_to_hms(s):
    h = s // 3600
    #s=s-h*3600 is the same as:
    s = s % 3600
    m = s // 60
    s = s % 60
    return (h,m,s)




        
