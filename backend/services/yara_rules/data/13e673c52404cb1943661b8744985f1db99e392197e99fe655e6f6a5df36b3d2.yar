rule auto_rule_20250726181843_3530 {
  strings:
    $o0 = "byte_4673C4" wide ascii nocase
    $o1 = "dword_467CC0" wide ascii nocase
    $o2 = "dword_467D10" wide ascii nocase
    $o3 = "dword_467300" wide ascii nocase
  condition:
    4 of ($o*)
}