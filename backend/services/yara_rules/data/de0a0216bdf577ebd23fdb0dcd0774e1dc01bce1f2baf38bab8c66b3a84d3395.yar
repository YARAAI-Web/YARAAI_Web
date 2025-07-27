rule auto_rule_20250726221541_7268 {
  strings:
    $o0 = "dword_140050BE8" wide ascii nocase
  condition:
    all of them
}