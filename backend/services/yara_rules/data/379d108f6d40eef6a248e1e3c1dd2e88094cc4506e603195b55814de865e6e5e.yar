rule auto_rule_20250726123913_0990 {
  strings:
    $o0 = "qword_1416C7640" wide ascii nocase
    $o1 = "_vcrt_freefls" wide ascii nocase
  condition:
    all of them
}