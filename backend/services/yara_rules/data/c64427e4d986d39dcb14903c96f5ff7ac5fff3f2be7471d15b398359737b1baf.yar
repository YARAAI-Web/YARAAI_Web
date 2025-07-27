rule auto_rule_20250726190528_0781 {
  strings:
    $o0 = "byte_444BB0" wide ascii nocase
    $o1 = "UnwindUp5_0" wide ascii nocase
  condition:
    all of them
}