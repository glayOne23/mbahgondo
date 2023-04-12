from django import template
import datetime

bulan = {1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'}
bulan_type2 = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

register = template.Library()
@register.filter
def tanggalsp(value):
    if value:
        d = value.day
        m = bulan[value.month]
        y = value.year
        return '%d %s %d'%(d,m,y)
    else:
        return value

def waktutanggal(value):
    # datetime_obj = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
    # datetime_obj =value
    # return datetime_obj
    if value:
        value = value.split('T')
        value = value[0].split('-')
        return F"{value[2]} {bulan_type2[value[1]]} {value[0]}"
    else:
        return None

def tanggal(value):
    if value:
        if len(value) > 10:
            value = value.split('T')
            value = value[0].split('-')
            return F"{value[2]} {bulan_type2[value[1]]} {value[0]}"
        else:
            value = value.split('-')
            return F"{value[2]} {bulan_type2[value[1]]} {value[0]}"
    else:
        return None

register.filter('waktutanggal', waktutanggal)
register.filter('tanggal', tanggal)