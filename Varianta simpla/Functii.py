import xml.etree.ElementTree as ET


tree = ET.parse('outputAd.xml')
root = tree.getroot()

def cleaning():
    for node in root.iter('W'):
        node.attrib.pop('Case', None)
        node.attrib.pop('Definiteness', None)
        node.attrib.pop('MSD', None)
        node.attrib.pop('Type', None)
        node.attrib.pop('deprel', None)
        node.attrib.pop('head', None)
        node.attrib.pop('offset', None)
        node.attrib.pop('Person', None)
        node.attrib.pop('Possesor_Number', None)
        node.attrib.pop('Tense', None)
        node.attrib.pop('EXTRA', None)
        node.attrib.pop('Form', None)


def anaphoraFunc():
    for W in root.iter('W'):
        if W.get('POS') == 'NOUN':
            if W.get('Gender') == 'feminine':
                if W.get('Number') == 'singular':
                    sinfem = W.get('id')
                else:
                    plufem = W.get('id')
            else:
                if W.get('Number') == 'singular':
                    sinmasc = W.get('id')
                else:
                    plumasc = W.get('id')

        elif W.get('POS') == 'PRONOUN':
            if W.get('Gender') == 'feminine':
                if W.get('Number') == 'singular':
                    W.set('anaphora', sinfem)
                else:
                    W.set('anaphora', plufem)
            else:
                if W.get('Number') == 'singular':
                    W.set('anaphora', sinmasc)
                else:
                    W.set('anaphora', plumasc)
                    

def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&amp;", "&")
    s = s.replace("&quot;", "\"")
    return s

for node in root.iter('S'):
    node.attrib.pop('offset', None)    


cleaning()
anaphoraFunc()
tree.write('OutputMed2.xml',encoding="UTF-8")
