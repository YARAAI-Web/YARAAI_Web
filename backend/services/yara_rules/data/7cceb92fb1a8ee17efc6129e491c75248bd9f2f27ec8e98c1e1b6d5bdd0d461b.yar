rule auto_rule_20250726181315_7557 {
  strings:
    $o0 = "dword_40A52C" wide ascii nocase
    $o1 = "x35u" wide ascii nocase
    $o2 = "dword_40A610" wide ascii nocase
    $o3 = "dword_40A538" wide ascii nocase
    $o4 = "dword_40A5B0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726181318_9005 {
  strings:
    $o0 = "x7CFCuLL" wide ascii nocase
    $o1 = "dword_40A510" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726181323_3111 {
  condition:
    auto_rule_20250726181315_7557 or auto_rule_20250726181318_9005
}