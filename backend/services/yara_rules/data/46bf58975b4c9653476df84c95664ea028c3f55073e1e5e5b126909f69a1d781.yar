rule auto_rule_20250726081006_3681 {
  strings:
    $o0 = "aPngotane" wide ascii nocase
    $o1 = "dword_77F70" wide ascii nocase
  condition:
    all of them
}