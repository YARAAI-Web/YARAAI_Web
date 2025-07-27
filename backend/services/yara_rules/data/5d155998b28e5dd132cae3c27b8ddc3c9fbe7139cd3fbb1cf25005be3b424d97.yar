rule auto_rule_20250726145008_9515 {
  strings:
    $o0 = "dword_465474" wide ascii nocase
    $o1 = "Debug" wide ascii nocase
  condition:
    all of them
}