rule auto_rule_20250726211728_7426 {
  strings:
    $o0 = "dword_4642A4" wide ascii nocase
    $o1 = "_cpinfo" wide ascii nocase
    $o2 = "dword_462018" wide ascii nocase
    $o3 = "debug" wide ascii nocase
  condition:
    4 of ($o*)
}