rule auto_rule_20250726180515_5434 {
  strings:
    $o0 = "dword_426ED9" wide ascii nocase
    $o1 = "x472Eu" wide ascii nocase
  condition:
    all of them
}