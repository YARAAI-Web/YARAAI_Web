rule auto_rule_20250726064856_9038 {
  strings:
    $o0 = "lpchText" wide ascii nocase
    $o1 = "TargetBufferLength" wide ascii nocase
    $o2 = "lpOperation" wide ascii nocase
  condition:
    3 of ($o*)
}