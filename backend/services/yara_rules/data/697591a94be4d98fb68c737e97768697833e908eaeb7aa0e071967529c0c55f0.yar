rule auto_rule_20250726105833_7372 {
  strings:
    $o0 = "x4046F1" wide ascii nocase
    $o1 = "dword_468690" wide ascii nocase
    $o2 = "int64_arg" wide ascii nocase
    $o3 = "hpal" wide ascii nocase
  condition:
    4 of ($o*)
}