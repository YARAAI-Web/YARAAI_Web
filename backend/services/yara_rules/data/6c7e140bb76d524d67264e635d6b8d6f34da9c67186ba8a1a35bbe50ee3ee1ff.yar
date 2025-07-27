rule auto_rule_20250726213933_9092 {
  strings:
    $o0 = "a24gop333eya" wide ascii nocase
  condition:
    all of them
}