rule auto_rule_20250726113218_5123 {
  strings:
    $o0 = "StringTypeA" wide ascii nocase
    $o1 = "GetLocaleInfoA" wide ascii nocase
    $o2 = "UnwindUp2_0" wide ascii nocase
    $o3 = "dword_45CAD4" wide ascii nocase
    $o4 = "dword_428EF8" wide ascii nocase
  condition:
    4 of ($o*)
}