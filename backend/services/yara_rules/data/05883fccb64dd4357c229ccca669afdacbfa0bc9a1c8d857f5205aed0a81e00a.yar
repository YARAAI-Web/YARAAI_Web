rule auto_rule_20250726131933_7586 {
  strings:
    $o0 = "atexit_0" wide ascii nocase
  condition:
    all of them
}