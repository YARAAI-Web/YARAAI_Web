rule auto_rule_20250726182107_4597 {
  strings:
    $o0 = "dwDesiredAccess" wide ascii nocase
    $o1 = "x15100u" wide ascii nocase
  condition:
    all of them
}