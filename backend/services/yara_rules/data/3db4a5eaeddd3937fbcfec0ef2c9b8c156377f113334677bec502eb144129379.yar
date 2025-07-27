rule auto_rule_20250726062830_1163 {
  strings:
    $o0 = "dword_465D48" wide ascii nocase
    $o1 = "dword_42A028" wide ascii nocase
    $o2 = "dword_465FC8" wide ascii nocase
  condition:
    3 of ($o*)
}