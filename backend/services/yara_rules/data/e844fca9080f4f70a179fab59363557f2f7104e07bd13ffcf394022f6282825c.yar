rule auto_rule_20250726180115_8041 {
  strings:
    $o0 = "dword_426E91" wide ascii nocase
  condition:
    all of them
}