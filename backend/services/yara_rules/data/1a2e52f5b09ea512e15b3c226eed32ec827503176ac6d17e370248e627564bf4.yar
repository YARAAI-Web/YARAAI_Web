rule auto_rule_20250726202533_0118 {
  strings:
    $o0 = "dword_45CADC" wide ascii nocase
    $o1 = "off_45C934" wide ascii nocase
  condition:
    all of them
}