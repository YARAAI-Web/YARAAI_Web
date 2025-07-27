rule auto_rule_20250726123754_9626 {
  strings:
    $o0 = "LibraryA" wide ascii nocase
    $o1 = "dword_42405C" wide ascii nocase
  condition:
    all of them
}