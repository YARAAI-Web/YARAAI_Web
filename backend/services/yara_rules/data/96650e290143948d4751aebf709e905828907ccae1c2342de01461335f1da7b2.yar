rule auto_rule_20250726131606_7933 {
  strings:
    $o0 = "a24gop333eya" wide ascii nocase
  condition:
    all of them
}