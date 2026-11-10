import hashlib, json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
def validate(p):
    assert set(p) == {'schema','runtime','id','version','author','license','definition'}, 'unknown package fields'
    assert p['schema'] == 1 and p['runtime'] == 'tlui-custom-v1'
    assert re.fullmatch(r'[a-z][a-z0-9-]{0,39}',p['id']) and re.fullmatch(r'[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}',p['version'])
    assert p['author'] and p['license']
    d=p['definition']
    assert set(d)=={'displayName','groupName','caption','value','base','width','height','primary','secondary','textColor','radius','border','minimum','maximum','layers'}
    assert type(d['base']) is int and 0<=d['base']<=15 and d['minimum']<d['maximum']
    assert 4<=d['width']<=4096 and 4<=d['height']<=4096 and 1<=len(d['layers'])<=64
    for l in d['layers']:
        assert set(l)=={'kind','name','text','binding','x','y','width','height','colorRole','color','param1','param2','style','bindValue','visible'}
        assert type(l['kind']) is int and 0<=l['kind']<=11
        assert type(l['visible']) is bool and type(l['bindValue']) is bool
        assert 4<=l['width']<=100 and 4<=l['height']<=100 and 0<=l['x']<=100 and 0<=l['y']<=100
        assert not l['binding'] or re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]{0,31}',l['binding'])
    return p
entries=[]
for path in sorted((ROOT/'packages').glob('*/*.tluicontrol')):
    data=path.read_bytes();assert len(data)<=256*1024
    p=validate(json.loads(data));assert path.parent.name==p['id'] and path.stem==p['version']
    entries.append(dict(id=p['id'],version=p['version'],name=p['definition']['displayName'],author=p['author'],license=p['license'],runtime=p['runtime'],sha256=hashlib.sha256(data).hexdigest(),url='https://ishnar.github.io/TLUI-Control-Gallery/'+path.relative_to(ROOT).as_posix()))
assert entries, 'at least one package required'
(ROOT/'catalog.json').write_text(json.dumps(dict(schema=1,packages=entries),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Validated',len(entries),'packages; generated catalog.json')
