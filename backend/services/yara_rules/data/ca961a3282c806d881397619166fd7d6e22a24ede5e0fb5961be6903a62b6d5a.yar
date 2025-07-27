rule auto_rule_20250726200004_6189 {
  strings:
    $o0 = "dword_7A1F1C" wide ascii nocase
    $o1 = "off_409368" wide ascii nocase
  condition:
    all of them
}