rule auto_rule_20250726154146_6512 {
  strings:
    $o0 = "dword_429B0C" wide ascii nocase
  condition:
    all of them
}