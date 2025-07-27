rule auto_rule_20250726105221_1698 {
  strings:
    $o0 = "dword_78450" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}