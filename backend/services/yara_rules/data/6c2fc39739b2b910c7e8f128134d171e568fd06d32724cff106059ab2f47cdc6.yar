rule auto_rule_20250726224137_6948 {
  strings:
    $o0 = "F54h" wide ascii nocase
    $o1 = "dword_640303EC" wide ascii nocase
    $o2 = "dword_6402F590" wide ascii nocase
  condition:
    3 of ($o*)
}