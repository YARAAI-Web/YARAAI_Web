rule auto_rule_20250726154034_9692 {
  strings:
    $o0 = "qword_140043F28" wide ascii nocase
    $o1 = "PyConfig_InitIsolatedConfig" wide ascii nocase
  condition:
    all of them
}