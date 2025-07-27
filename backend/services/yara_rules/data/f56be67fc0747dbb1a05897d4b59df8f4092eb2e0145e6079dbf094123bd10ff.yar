rule auto_rule_20250726202155_7054 {
  strings:
    $o0 = "runtime_typePointers_fastForward" wide ascii nocase
  condition:
    all of them
}