import re
import urllib.request
from urllib.parse import quote
import html2text

def search(body):
    z = str(body)
    s = 'http://go.mail.ru/search?fm=1&q=' + quote(z)
    doc = urllib.request.urlopen(s).read().decode('cp1251', errors='ignore')

    o = re.compile('"url":"(.*?)"')
    l = o.findall(doc)
    sp = []
    for x in l:
        if ((x.rfind('youtube') == -1) and (x.rfind('yandex') == -1) and (x.rfind('mail.ru') == -1) and (
                x.rfind('.jpg') == -1) and (x.rfind('.png') == -1) and (x.rfind('.gif') == -1)):
            sp.append(x)

    sp = dict(zip(sp, sp)).values()
    sp1 = []
    for s in sp:
        sp1.append(s)
    sp1 = sp1[:2]

    sp = sp1
    text = ""

    for s in sp:
        try:
            # Теперь будем по очереди получать тексты каждой страницы из результатов поиска в переменную doc
            doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
            h = html2text.HTML2Text()
            h.ignore_links = True
            h.body_width = False
            h.ignore_images = True
            doc = h.handle(doc)
            summa = ""
            # Делим текст страницы на абзацы
            ss = doc.split("\n")
            for xx in ss:
                xx = xx.strip()
                # Фильтруем абзацы чтобы они не начинались неправильными символами а кончались на правильные - точку или !?;
                if ((len(xx) > 50) and (xx.startswith('&') == False) and (xx.startswith('>') == False) and (
                        xx.startswith('*') == False) and (xx.startswith('\\') == False) and (
                        xx.startswith('<') == False) and (xx.startswith('(') == False) and (
                        xx.startswith('#') == False) and (
                        xx.endswith('.') or xx.endswith('?') or xx.endswith('!') or xx.endswith(';'))):
                    summa = summa + xx + "\n \n"
            if (len(summa) > 500):
                text += summa
        except Exception:
            pass
        if text == "":
            text = "Простите, но ничего не найдено по этому вопросу."
        elif len(text) > 4096:
            i = 4096
            while text[i] != ".":
                i -= 1
            text = text[:i+1]
        return text
