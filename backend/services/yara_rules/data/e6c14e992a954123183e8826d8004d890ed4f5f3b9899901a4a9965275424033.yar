rule auto_rule_20250726211350_5700 {
  strings:
    $o0 = "dword_4C1138" wide ascii nocase
    $o1 = "dword_4C1714" wide ascii nocase
  condition:
    all of them
}