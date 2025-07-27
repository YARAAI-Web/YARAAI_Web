rule auto_rule_20250726085302_5994 {
  strings:
    $o0 = "dword_467148" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "dword_4672AC" wide ascii nocase
    $o3 = "UnwindUp0_0" wide ascii nocase
    $o4 = "dbgrpt" wide ascii nocase
  condition:
    4 of ($o*)
}