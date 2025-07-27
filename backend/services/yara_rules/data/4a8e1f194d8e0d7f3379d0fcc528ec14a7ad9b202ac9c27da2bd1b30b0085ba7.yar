rule auto_rule_20250726233641_0104 {
  strings:
    $o0 = "aKluzksghetriyt" wide ascii nocase
  condition:
    all of them
}