rule auto_rule_20250727020957_8147 {
  strings:
    $o0 = "a24gop333eya" wide ascii nocase
    $o1 = "x19000u" wide ascii nocase
  condition:
    all of them
}