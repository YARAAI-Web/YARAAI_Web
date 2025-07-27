rule auto_rule_20250726232820_3976 {
  strings:
    $o0 = "dword_449028" wide ascii nocase
    $o1 = "acmDriverClose" wide ascii nocase
    $o2 = "__heap_select" wide ascii nocase
    $o3 = "dword_44C8F0" wide ascii nocase
    $o4 = "overrun" wide ascii nocase
  condition:
    4 of ($o*)
}