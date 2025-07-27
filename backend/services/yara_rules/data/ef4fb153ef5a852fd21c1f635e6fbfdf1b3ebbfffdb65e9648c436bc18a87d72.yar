rule auto_rule_20250726073633_3130 {
  strings:
    $o0 = "dword_78768" wide ascii nocase
    $o1 = "__readcr0" wide ascii nocase
  condition:
    all of them
}