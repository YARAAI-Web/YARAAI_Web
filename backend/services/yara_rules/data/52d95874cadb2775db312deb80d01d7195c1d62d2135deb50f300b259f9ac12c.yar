rule auto_rule_20250726070409_5728 {
  strings:
    $o0 = "off_405F55" wide ascii nocase
  condition:
    all of them
}