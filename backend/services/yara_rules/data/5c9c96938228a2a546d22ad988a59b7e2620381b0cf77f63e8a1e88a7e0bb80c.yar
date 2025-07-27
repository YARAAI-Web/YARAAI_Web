rule auto_rule_20250726095947_8331 {
  strings:
    $o0 = "GetClipCursor" wide ascii nocase
  condition:
    all of them
}