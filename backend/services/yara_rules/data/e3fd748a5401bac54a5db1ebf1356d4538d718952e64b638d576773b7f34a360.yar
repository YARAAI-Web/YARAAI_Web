rule auto_rule_20250726153954_5878 {
  strings:
    $o0 = "dword_4643E8" wide ascii nocase
    $o1 = "dword_46399C" wide ascii nocase
  condition:
    all of them
}