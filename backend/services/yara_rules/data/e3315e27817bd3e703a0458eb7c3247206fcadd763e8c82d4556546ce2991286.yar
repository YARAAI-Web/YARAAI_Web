rule auto_rule_20250726060914_3483 {
  strings:
    $o0 = "x1809A0813LL" wide ascii nocase
  condition:
    all of them
}