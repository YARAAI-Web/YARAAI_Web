#!/usr/bin/env python3
"""
map_mitre.py: Automated MITRE ATT&CK mapping using capa CLI.

1) Run capa on the PE sample with your own rules & sigs
2) Extract ATT&CK IDs from capa’s JSON output
3) Generate a simple HTML report listing those IDs
"""
import os
import sys
import json
import argparse
import subprocess

def run_capa(sample, tmp_dir, rules_dir, sigs_dir):
    os.makedirs(tmp_dir, exist_ok=True)
    out_json = os.path.join(tmp_dir, os.path.splitext(os.path.basename(sample))[0] + '.capa.json')
    cmd = [
        'capa',
        '-r', rules_dir,
        '-s', sigs_dir,
        '--json', sample
    ]
    with open(out_json, 'w', encoding='utf-8') as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, check=True)
    return out_json

def extract_attack_ids(json_path):
    data = json.load(open(json_path, encoding='utf-8'))
    ids = set()
    for rule in (data.get('rules') or {}).values():
        for attack in rule.get('meta', {}).get('attack', []):
            if isinstance(attack, dict):
                tid = attack.get('id') or attack.get('ID')
                if tid:
                    ids.add(tid)
            elif isinstance(attack, str):
                ids.add(attack)
    return sorted(ids)

def map_mitre(sample):
    tmp_dir = os.path.abspath(r'services\CAPA\capa_json')
    rules_dir = os.path.abspath(r'services\CAPA\capa-rules')
    sigs_dir = os.path.abspath(r'services\CAPA\capa-sigs')

    print(f'→ Running capa on: {sample}')
    json_path = run_capa(sample, tmp_dir, rules_dir, sigs_dir)
    print(f'→ capa JSON: {json_path}')

    ids = extract_attack_ids(json_path)
    print(f'→ ATT&CK IDs: {ids or "None"}')

    return (json_path, ids)

if __name__ == '__main__':
    map_mitre(sys.argv[1])