rule auto_rule_20250726155608_1037 {
  strings:
    $o0 = "dword_4605E0" wide ascii nocase
    $o1 = "_global_unwind2" wide ascii nocase
  condition:
    all of them
}