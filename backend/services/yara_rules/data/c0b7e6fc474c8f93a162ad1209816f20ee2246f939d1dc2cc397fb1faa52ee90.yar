rule auto_rule_20250726145032_8791 {
  strings:
    $o0 = "nLine" wide ascii nocase
    $o1 = "GetActiveWindow_0" wide ascii nocase
  condition:
    all of them
}