rule auto_rule_20250726070841_7244 {
  strings:
    $o0 = "_tmainCRTStartup" wide ascii nocase
    $o1 = "qword_14000E1D8" wide ascii nocase
  condition:
    all of them
}