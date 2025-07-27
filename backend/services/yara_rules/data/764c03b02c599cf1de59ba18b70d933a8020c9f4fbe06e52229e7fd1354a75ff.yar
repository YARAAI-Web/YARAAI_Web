rule auto_rule_20250726123207_0202 {
  strings:
    $o0 = "x3C18" wide ascii nocase
    $o1 = "dword_4D019C" wide ascii nocase
  condition:
    all of them
}