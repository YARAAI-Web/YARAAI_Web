rule auto_rule_20250726194437_6240 {
  strings:
    $o0 = "dword_43B6AB" wide ascii nocase
    $o1 = "x72317700" wide ascii nocase
    $o2 = "x1D532900u" wide ascii nocase
    $o3 = "RegCreateKeyA" wide ascii nocase
    $o4 = "dword_43B085" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726194440_3212 {
  strings:
    $o0 = "dword_43B88E" wide ascii nocase
    $o1 = "dword_43B26C" wide ascii nocase
    $o2 = "dword_43B73D" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726194442_9740 {
  condition:
    auto_rule_20250726194437_6240 or auto_rule_20250726194440_3212
}