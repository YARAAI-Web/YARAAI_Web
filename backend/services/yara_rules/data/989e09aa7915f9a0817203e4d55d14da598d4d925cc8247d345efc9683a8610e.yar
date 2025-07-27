rule auto_rule_20250726090112_6779 {
  strings:
    $o0 = "dword_40C8D8" wide ascii nocase
    $o1 = "aFlssetvalue" wide ascii nocase
  condition:
    all of them
}