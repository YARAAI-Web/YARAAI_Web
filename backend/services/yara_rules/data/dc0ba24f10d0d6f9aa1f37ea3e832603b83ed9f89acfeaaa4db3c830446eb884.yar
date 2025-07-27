rule auto_rule_20250726182354_7987 {
  strings:
    $o0 = "dword_436412" wide ascii nocase
    $o1 = "dword_436406" wide ascii nocase
    $o2 = "ShowTaskOriginal" wide ascii nocase
    $o3 = "dword_432B30" wide ascii nocase
  condition:
    4 of ($o*)
}