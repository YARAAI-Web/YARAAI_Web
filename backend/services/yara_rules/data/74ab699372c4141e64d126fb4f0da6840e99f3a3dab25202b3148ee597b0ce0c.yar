rule auto_rule_20250726231149_7218 {
  strings:
    $o0 = "dword_411D4C" wide ascii nocase
    $o1 = "off_4118F0" wide ascii nocase
    $o2 = "CodePagea" wide ascii nocase
  condition:
    3 of ($o*)
}