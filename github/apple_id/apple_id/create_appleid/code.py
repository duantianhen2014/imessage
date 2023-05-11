# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 验证码相关 
#

import os
import sys
import subprocess

try:
    import urllib2 as wdf_urllib
    from cookielib import CookieJar
except ImportError:
    import urllib.request as wdf_urllib
    from http.cookiejar import CookieJar

QRImagePath = os.path.join(os.getcwd(), 'qrcode.jpg')

def getRequest(url, data=None):
    try:
        data = data.encode('utf-8')
    except:
        pass
    finally:
        return wdf_urllib.Request(url=url, data=data)

def showQRImage(url):

    request = getRequest(url=url)
    response = wdf_urllib.urlopen(request)

    f = open(QRImagePath, 'wb')
    f.write(response.read())
    f.close()

    if sys.platform.find('darwin') >= 0:
        subprocess.call(['open', QRImagePath])
    elif sys.platform.find('linux') >= 0:
        subprocess.call(['xdg-open', QRImagePath])
    else:
        os.startfile(QRImagePath)

    print('请输入')


showQRImage('data:image/jpeg;base64,/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABGAKADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD1/wCzafyv9gXQI58oRrtX/aGG25+nPJ7Zo8jT+D/Yt4c8BinMn+y2Wzjt8/GPapRODGHHiSIxE4V8RZLemeh78AA8dag1G6mt9PvZY9fhM8MDyMgSP5cKSCB1Bxg5OR3xjigB32fT/wDoB3ny9fk/1f8Au/N3/wBj0Ge1H2fTzx/YV2d3IUoMS+7ZbGe/z4OfesaaW/stMs7tfF8sss81sixOkBBDyIr5+XJwGzwRjFb5mIDk+IogqnEpxF8jZxgenPGDk9s55oAh8jTvvf2PfADjzQjbk9hht2O/HHJ75o+zafyv9gXQI58oRrtX/aGG25+nPJ7ZqwJJDIqjX4DKRlU2R4ZfUjOTznkED2qhc63YWkixTeK4V3LvT5Y2Y9uSBjHXsDx1oAn8jT+D/Yt4c8BinMn+y2Wzjt8/GPaj7Pp//QDvPl6/J/q/935u/wDsegz2otNRhvo3lt/E0EgTIl2pGAgA5IB5Bxzk5HfGOKm804T/AIqKH5v9X8sXz+ufXt0x178YAIfs+nnj+wrs7uQpQYl92y2M9/nwc+9Hkad97+x74AceaEbcnsMNux3445PfNTGYgOT4iiCqcSnEXyNnGB6c8YOT2znmnCSQyKo1+AykZVNkeGX1Izk855BA9qAK/wBm0/lf7AugRz5QjXav+0MNtz9OeT2zR5Gn8H+xbw54DFOZP9lstnHb5+Me1Si4QqCviWIxk4Vv3WSewJ6EdeAAfenGVgzg+IYQyjMi7Y/kXGcgdRxzk5HfGOKAIPs+n/8AQDvPl6/J/q/935u/+x6DPaj7Pp54/sK7O7kKUGJfdstjPf58HPvU3mnCf8VFD83+r+WL5/XPr26Y69+MBmIDk+IogqnEpxF8jZxgenPGDk9s55oAh8jTvvf2PfADjzQjbk9hht2O/HHJ75o+zafyv9gXQI58oRrtX/aGG25+nPJ7ZqwJJDIqjX4DKRlU2R4ZfUjOTznkED2pgnBjDjxJEYicK+IslvTPQ9+AAeOtAEXkafwf7FvDngMU5k/2Wy2cdvn4x7UfZ9P/AOgHefL1+T/V/wC783f/AGPQZ7VOZWDOD4hhDKMyLtj+RcZyB1HHOTkd8Y4pPNOE/wCKih+b/V/LF8/rn17dMde/GACH7Pp54/sK7O7kKUGJfdstjPf58HPvR5Gnfe/se+AHHmhG3J7DDbsd+OOT3zUxmIDk+IogqnEpxF8jZxgenPGDk9s55pwkkMiqNfgMpGVTZHhl9SM5POeQQPagB5+1mRnOjWxlIwz+eMMvpnbk9uCAOOtZXiPzY/Cups2iQpFHZzMmHQtGdrHdjGBzzwSfx4q15mm8r/aGpgDnyi025f8AaORux25459cVl+I5bA+G9RCanfO8luyAszFZcjGBkbT6fLzn3zQBNrUc6WNnEdHgXde2wkIlU+ZtcEAcc9D1x1781sAXIZCNEtgyjER85fkGMYPy8ccYGR2zjmsHWZbAtpqrqN8R9tTIZn/dABjzkdeP4s9DjvWp5umnj+0tRO7kqGlzL/tLgZx3+TjHtQBYKTeUytoNuYicunmJlm9QMYPGOSQeOlcvHrn9ng63d6RHK2sXawxOsqkLAOAc4zt+UuTjHzduBV7XLuzXThBb6tffaLqRbZJWdwsYb72eNuVXc3PzdO2KpJa6NqOp3dvJPfDT7O2+xww5lypYfvDjG4KF2Lzx19qANIpLp/iKJho1ukN+oWOMyL8k8eWDHjAyuTxk4QHGeKs3mpSWdylt/wAI8Jri4Uu0cLK29VIGc4xgFv4ivXjPOMLzYdQ8MAtqF5Jq1m3HzyBZZozgBcDA3AY+XnDetXms/DesrFfzXl/OskKhQ8kjLGpyw3DGOc/xZzjjoaALX9qagmX/AOENlHk/LGVngYqvTorEjjPAB9Krya8lxALbT9Dt57qZmAtXIVlcAbmkQqNqgFeWwTwMcjOL4gtPDOi6a0+ledBqr/JZi2jMbyyHgEEKPlyQTtIUjgdQKgtI3bxFdpFrF1mWGJb/AFMM6rG43FokyMAhSgGenJPPUA2LCz068a/S40aw1XULST/TbyYq26TGSFYpkYGMKBgDjORzoeGoriLwto6f2PA6paxGNmlXIbaDuPHHPOQSe+M8VhwjStP0zxL9mnvYIomfybdPMBAW3T5mGN2N24HdxyM84rfsjp0NhbRHU7/KxKhKs+2TAxtXAxnt8nOfegDQ23Pz/wDEjtvmx5n71fn9MfLz36469+cKBchkI0S2DKMRHzl+QYxg/LxxxgZHbOOaq+bpv/QT1H5enzSfu/8Ae47/AO36HHejzdNPH9paid3JUNLmX/aXAzjv8nGPagCwUmMbIdBgMROXTzEyzeoGMHtySDx0p5+1mRnOjWxlIwz+eMMvpnbk9uCAOOtVPO07739r34I480u21f8AZOV257888+mKPM03lf7Q1MAc+UWm3L/tHI3Y7c8c+uKALIWcLGBoduFU5jHmplGznJGMDnnIye+M8Ubbn5/+JHbfNjzP3q/P6Y+Xnv1x1784redp3B/tTUDu4LBnxJ/srgYz2+TnPvR5um/9BPUfl6fNJ+7/AN7jv/t+hx3oAtAXIZCNEtgyjER85fkGMYPy8ccYGR2zjmmlJjGyHQYDETl08xMs3qBjB7ckg8dKr+bpp4/tLUTu5Khpcy/7S4Gcd/k4x7Uedp33v7XvwRx5pdtq/wCycrtz35559MUAaG3WPu+bYnHO/wAtxn227uPrk/T0yfEo1U6BcCRrPZIUQqobK5dR1z83XpgenvU32bT+V/sC6BHPlCNdq/7Qw23P055PbNV77TNL1Cze3k0fUAkmMSIuHcgggEls9Rj5uMD05oAXXV1xW02eO2guhbXfmMkCncR5cgzgsMAEjuevtyn9vauOH0ydM85+xO2z2wrHd6ZyPXHaqJ8O22AEOvpt9FiPl/7uVPX/AGc9BntTG0AqCY5tdckZCPb2pEvu3yAZ7/Pzn3oAj/4SG4u9bu7x44wNGtS3kSQyIzu/UjcOGwFAHP3z61GNL1RWlZPD18hlkaZ2j1AoGZjlvkFzgZJJzn8PTN0fw7OLiCbUdL1YbpFe8eVIxhl3Ptj8ti5G9lOcAYTFdn9m0/lf7AugRz5QjXav+0MNtz9OeT2zQBmaM9/puofYxpbWD35aQPdTmcM6qoPzeaxJ2gHGF4UjPGazmfxTp+rXGj2PmfZ7YG4Q2kcJ3LKxIGJWyApDgbd3GPatTWbKzksllt9IuVuIpUkheVceawOPLYls4YEp82BhvTFVJbdZ9bsrqHwrqkCQlorjzfL2+WwyCgWQnIZV+6OhPqKAOUnuNWPia4uLqS7luYkRRI9hI1xboy/ejUKIgMlhuPJwSBW3prwafYxrp3i0WtucuFcACQnkuWkiPJz3B+vpp3X9mHxFDs0efy7W2kkuiyDBVtpXeS2Mnaz/AD4PyjvipfD9vZjRIJJdHvRvLyCQIwaNWcsqjB3YCsOgx175oAdDplzdeFr+3i1yxura/Epk1EqCG3fKeFIUY6ZzxjGPS5o9/rt5cX0EtxpU/wBmkWPzYY3Ayyhs/eOcBhxx9e9cvGNMufBtui6bJI89zFuVQCmHuFzgbtucNt455PbNdTBYaRbptg8P3MaMeCkW3zD6N82cdvn4x7UAamNY/v2PH+y/z/r8v69e2OTGsdN9iN3OdjnZ7Yz83pn5fXHas/7Pp/8A0A7z5evyf6v/AHfm7/7HoM9qPs+nnj+wrs7uQpQYl92y2M9/nwc+9AGh/wATj72bE442Ycbvfd2+mD9fQ26x93zbE453+W4z7bd3H1yfp6Z/kad97+x74AceaEbcnsMNux3445PfNH2bT+V/sC6BHPlCNdq/7Qw23P055PbNAGhjWOu6xGeMbXOz3zn5vXGB6Z70Y1j+/Y8f7L/P+vy/r17Y5z/I0/g/2LeHPAYpzJ/stls47fPxj2o+z6f/ANAO8+Xr8n+r/wB35u/+x6DPagDQxrHTfYjdznY52e2M/N6Z+X1x2o/4nH3s2Jxxsw43e+7t9MH6+mf9n088f2FdndyFKDEvu2Wxnv8APg596PI07739j3wA480I25PYYbdjvxxye+aAJRODGHHiSIxE4V8RZLemeh78AA8dacZWDOD4hhDKMyLtj+RcZyB1HHOTkd8Y4qQ/azIznRrYykYZ/PGGX0ztye3BAHHWmhZwsYGh24VTmMeamUbOckYwOecjJ74zxQAzzThP+Kih+b/V/LF8/rn17dMde/GAzEByfEUQVTiU4i+Rs4wPTnjBye2c80/bc/P/AMSO2+bHmfvV+f0x8vPfrjr35woFyGQjRLYMoxEfOX5BjGD8vHHGBkds45oAaJJDIqjX4DKRlU2R4ZfUjOTznkED2pgnBjDjxJEYicK+IslvTPQ9+AAeOtPKTGNkOgwGInLp5iZZvUDGD25JB46U8/azIznRrYykYZ/PGGX0ztye3BAHHWgDH1+xl1Wwa1/tyxlKOss0FwieWVX5hkckdjzuHtjisSOx1K2RYor1okfiJbbWAY29cbgDjkfdC4rsQs4WMDQ7cKpzGPNTKNnOSMYHPORk98Z4o23Pz/8AEjtvmx5n71fn9MfLz36469+cAHN2ujvNZyW99rdnaWIk3XFtbyJIXfP/AC0kYAkZxkEEnoWNdEJJN6ouvwGUjKJsjwy+uM5PfkED2p4FyGQjRLYMoxEfOX5BjGD8vHHGBkds45ppSYxsh0GAxE5dPMTLN6gYwe3JIPHSgDN/snRjJHdi/wBMJWQNFcfZrfeH6j5sY9TwAeOtaJlYM4PiGEMozIu2P5FxnIHUcc5OR3xjipD9rMjOdGtjKRhn88YZfTO3J7cEAcdaaFnCxgaHbhVOYx5qZRs5yRjA55yMnvjPFADPNOE/4qKH5v8AV/LF8/rn17dMde/GAzEByfEUQVTiU4i+Rs4wPTnjBye2c80/bc/P/wASO2+bHmfvV+f0x8vPfrjr35woFyGQjRLYMoxEfOX5BjGD8vHHGBkds45oAaJJDIqjX4DKRlU2R4ZfUjOTznkED2pgnBjDjxJEYicK+IslvTPQ9+AAeOtPKTGNkOgwGInLp5iZZvUDGD25JB46U8/azIznRrYykYZ/PGGX0ztye3BAHHWgCMysGcHxDCGUZkXbH8i4zkDqOOcnI74xxSeacJ/xUUPzf6v5Yvn9c+vbpjr34w8LOFjA0O3CqcxjzUyjZzkjGBzzkZPfGeKNtz8//Ejtvmx5n71fn9MfLz36469+cADDMQHJ8RRBVOJTiL5GzjA9OeMHJ7ZzzThJIZFUa/AZSMqmyPDL6kZyec8gge1OAuQyEaJbBlGIj5y/IMYwfl444wMjtnHNNKTGNkOgwGInLp5iZZvUDGD25JB46UAWP7JToLy+Cdl+0twfXPU/QnHtR/ZQ6m+viT94+efmHpjoOOMrg9855oooAP7JX/n9vuPu/wCkH5f8f+BZ/nR/ZK972+IP3h9ob5j6+o55wuB2xjiiigA/sruL++Djo3ndB6Yxg/Ugn3o/slOgvL4J2X7S3B9c9T9Cce1FFAB/ZQ6m+viT94+efmHpjoOOMrg9855o/slf+f2+4+7/AKQfl/x/4Fn+dFFAB/ZK972+IP3h9ob5j6+o55wuB2xjij+yu4v74OOjed0HpjGD9SCfeiigA/slOgvL4J2X7S3B9c9T9Cce1H9lDqb6+JP3j55+YemOg44yuD3znmiigA/slf8An9vuPu/6Qfl/x/4Fn+dH9kr3vb4g/eH2hvmPr6jnnC4HbGOKKKAD+yu4v74OOjed0HpjGD9SCfej+yU6C8vgnZftLcH1z1P0Jx7UUUAH9lDqb6+JP3j55+YemOg44yuD3znmj+yV/wCf2+4+7/pB+X/H/gWf50UUAH9kr3vb4g/eH2hvmPr6jnnC4HbGOKP7K7i/vg46N53QemMYP1IJ96KKAP/Z')



