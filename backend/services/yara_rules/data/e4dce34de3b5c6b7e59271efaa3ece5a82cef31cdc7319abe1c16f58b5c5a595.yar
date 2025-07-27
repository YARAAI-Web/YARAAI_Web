rule auto_rule_20250726235319_4641 {
  strings:
    $o0 = "off_457920" wide ascii nocase
    $o1 = "dword_457DD4" wide ascii nocase
  condition:
    all of them
}