rule auto_rule_20250726235216_9274 {
  strings:
    $o0 = "dword_14002ECF0" wide ascii nocase
    $o1 = "PyPreConfig_InitIsolatedConfig" wide ascii nocase
  condition:
    all of them
}