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
    # JSON 파일 로드
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)

    # (tid, technique, tactic) 삼중 리스트 수집
    ids = []
    for rule in data.get('rules', {}).values():
        for attack in rule.get('meta', {}).get('attack', []):
            if isinstance(attack, dict):
                tid = attack.get('id') or attack.get('ID')
                if not tid:
                    continue
                tech = attack.get('technique') or ''
                tac  = attack.get('tactic')    or ''
                ids.append([tid, tech, tac])
            elif isinstance(attack, str):
                # 문자열만 있는 경우에도 ID로 추가
                ids.append([attack, '', ''])

    # 중복 제거: 리스트 → 튜플 → set → 다시 리스트로
    unique = set(tuple(x) for x in ids)
    return [list(x) for x in unique]

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