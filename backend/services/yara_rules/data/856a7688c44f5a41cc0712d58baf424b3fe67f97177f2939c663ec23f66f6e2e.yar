rule auto_rule_20250726194144_2425 {
  strings:
    $o0 = "dword_463E80" wide ascii nocase
    $o1 = "dword_464408" wide ascii nocase
  condition:
    all of them
}