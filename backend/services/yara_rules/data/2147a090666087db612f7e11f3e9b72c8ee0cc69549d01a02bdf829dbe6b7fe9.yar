rule auto_rule_20250726222528_6294 {
  strings:
    $o0 = "_twoToTOS" wide ascii nocase
    $o1 = "dword_41B008" wide ascii nocase
  condition:
    all of them
}