rule auto_rule_20250726085830_9966 {
  strings:
    $o0 = "off_454DD4" wide ascii nocase
    $o1 = "dword_4555E4" wide ascii nocase
    $o2 = "dword_454F7C" wide ascii nocase
  condition:
    3 of ($o*)
}