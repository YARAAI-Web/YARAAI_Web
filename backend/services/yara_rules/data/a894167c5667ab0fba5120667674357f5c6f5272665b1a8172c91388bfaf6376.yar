rule auto_rule_20250726091747_1697 {
  strings:
    $o0 = "off_454DA8" wide ascii nocase
    $o1 = "dword_454F94" wide ascii nocase
  condition:
    all of them
}