rule auto_rule_20250726221348_1212 {
  strings:
    $o0 = "dword_78518" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}