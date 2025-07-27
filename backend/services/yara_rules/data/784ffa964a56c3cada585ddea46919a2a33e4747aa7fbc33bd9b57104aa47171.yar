rule auto_rule_20250726194326_9098 {
  strings:
    $o0 = "dword_462F84" wide ascii nocase
    $o1 = "dword_42A008" wide ascii nocase
  condition:
    all of them
}