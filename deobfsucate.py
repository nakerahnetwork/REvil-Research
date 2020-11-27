# cc to OALabs For the Scripts I Just Edited it to make work with current samples :) 

import json 

export_db = {}

def get_api_hash(fn_name):
    result = 0x2b
    for c in fn_name:
        result = result * 0x10f + ord(c);
    return result & 0x1FFFFF


def transform_hash(api_hash):
    result = api_hash << 0x10 ^ api_hash ^ 0x8ffcc902;
    return result & 0x1fffff


def lookup_hash(api_hash):
    t_hash = transform_hash(api_hash)
    return export_db.get(t_hash, "")


def setup(json_file):
    global export_db
    exports_json = json.loads(open(json_file,'rb').read())
    exports_list = exports_json['exports']
    for export in exports_list:
        api_hash = get_api_hash(export)
        export_db[api_hash] = export


def get_imports(base_address):
    for ptr in range(0,0x2dc,4):
        hash_value = idc.Dword(base_address + ptr)
        api_name = lookup_hash(hash_value)
        if api_name == "":
            continue
        idc.MakeName(base_address + ptr, api_name.encode('utf-8'))
