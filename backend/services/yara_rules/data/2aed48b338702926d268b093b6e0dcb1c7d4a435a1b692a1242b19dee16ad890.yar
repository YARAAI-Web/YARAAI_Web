rule auto_rule_20250726081153_4720 {
  strings:
    $o0 = "dword_4281F0" wide ascii nocase
    $o1 = "dword_427CFC" wide ascii nocase
    $o2 = "dword_427E50" wide ascii nocase
    $o3 = "off_42752C" wide ascii nocase
    $o4 = "_setenvp" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726081156_4632 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "dword_427CDC" wide ascii nocase
    $o2 = "dword_424018" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726081159_0711 {
  condition:
    auto_rule_20250726081153_4720 or auto_rule_20250726081156_4632
}