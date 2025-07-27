rule auto_rule_20250726161917_4525 {
  strings:
    $o0 = "off_44BCB0" wide ascii nocase
    $o1 = "copy_tail_loop" wide ascii nocase
    $o2 = "dword_44BE64" wide ascii nocase
  condition:
    3 of ($o*)
}