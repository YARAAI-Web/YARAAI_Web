rule auto_rule_20250726190649_4314 {
  strings:
    $o0 = "dword_40A74C" wide ascii nocase
    $o1 = "dword_40A730" wide ascii nocase
    $o2 = "dword_40A560" wide ascii nocase
    $o3 = "x1810" wide ascii nocase
    $o4 = "x6662" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726190652_8873 {
  strings:
    $o0 = "dword_4100C3" wide ascii nocase
    $o1 = "x7448" wide ascii nocase
    $o2 = "xFFFFECEC" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726190655_0931 {
  condition:
    auto_rule_20250726190649_4314 or auto_rule_20250726190652_8873
}