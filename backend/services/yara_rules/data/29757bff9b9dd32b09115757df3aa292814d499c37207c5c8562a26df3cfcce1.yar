rule auto_rule_20250726213803_6779 {
  strings:
    $o0 = "dword_403008" wide ascii nocase
    $o1 = "x402DA9" wide ascii nocase
  condition:
    all of them
}