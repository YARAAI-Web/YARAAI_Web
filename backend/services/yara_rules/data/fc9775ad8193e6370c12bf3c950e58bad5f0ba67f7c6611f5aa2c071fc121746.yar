rule auto_rule_20250726203148_5047 {
  strings:
    $o0 = "xFFFEFFFF" wide ascii nocase
    $o1 = "dword_782D8" wide ascii nocase
    $o2 = "dword_78300" wide ascii nocase
    $o3 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}