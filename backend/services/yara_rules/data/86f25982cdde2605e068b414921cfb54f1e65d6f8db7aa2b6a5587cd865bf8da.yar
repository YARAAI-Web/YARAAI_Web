rule auto_rule_20250726214555_5221 {
  strings:
    $o0 = "__file__" wide ascii nocase
    $o1 = "extract" wide ascii nocase
    $o2 = "PyPreConfig_InitIsolatedConfig" wide ascii nocase
  condition:
    3 of ($o*)
}