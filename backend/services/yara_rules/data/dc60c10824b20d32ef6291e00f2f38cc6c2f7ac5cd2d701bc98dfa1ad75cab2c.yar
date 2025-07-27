rule auto_rule_20250726094110_7245 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "dword_475964" wide ascii nocase
  condition:
    all of them
}