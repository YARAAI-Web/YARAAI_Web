rule auto_rule_20250726153111_4896 {
  strings:
    $o0 = "lstrcatW" wide ascii nocase
    $o1 = "EFFh" wide ascii nocase
  condition:
    all of them
}