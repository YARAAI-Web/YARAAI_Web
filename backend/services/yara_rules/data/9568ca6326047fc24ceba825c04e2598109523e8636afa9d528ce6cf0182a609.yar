rule auto_rule_20250726140524_0011 {
  strings:
    $o0 = "x6649u" wide ascii nocase
    $o1 = "dwDesiredAccess" wide ascii nocase
  condition:
    all of them
}