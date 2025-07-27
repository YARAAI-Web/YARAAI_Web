rule auto_rule_20250726181524_6527 {
  strings:
    $o0 = "_inc" wide ascii nocase
    $o1 = "dword_469D48" wide ascii nocase
  condition:
    all of them
}