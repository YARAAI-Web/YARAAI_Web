rule auto_rule_20250726084421_9935 {
  strings:
    $o0 = "xE481" wide ascii nocase
    $o1 = "xFFFFFFF7" wide ascii nocase
  condition:
    all of them
}