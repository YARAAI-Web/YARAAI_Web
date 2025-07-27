rule auto_rule_20250726134427_2316 {
  strings:
    $o0 = "dword_4050DA" wide ascii nocase
    $o1 = "dword_405180" wide ascii nocase
  condition:
    all of them
}