rule auto_rule_20250726082517_7056 {
  strings:
    $o0 = "TargetPath" wide ascii nocase
    $o1 = "x2EF4u" wide ascii nocase
    $o2 = "x4E71" wide ascii nocase
  condition:
    3 of ($o*)
}