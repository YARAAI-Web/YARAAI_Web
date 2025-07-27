rule auto_rule_20250726133015_6370 {
  strings:
    $o0 = "dword_42EED4" wide ascii nocase
    $o1 = "aSystemCurrentc" wide ascii nocase
    $o2 = "dword_42EEA8" wide ascii nocase
  condition:
    3 of ($o*)
}