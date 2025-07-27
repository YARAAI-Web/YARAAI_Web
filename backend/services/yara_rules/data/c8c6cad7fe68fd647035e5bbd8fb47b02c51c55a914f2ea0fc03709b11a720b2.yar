rule auto_rule_20250726061027_2677 {
  strings:
    $o0 = "off_449A40" wide ascii nocase
    $o1 = "dword_40B01C" wide ascii nocase
    $o2 = "dword_44A044" wide ascii nocase
  condition:
    3 of ($o*)
}