rule auto_rule_20250726105813_8488 {
  strings:
    $o0 = "media" wide ascii nocase
    $o1 = "dword_4321C0" wide ascii nocase
    $o2 = "xFFFF3333" wide ascii nocase
  condition:
    3 of ($o*)
}