rule auto_rule_20250726210649_7526 {
  strings:
    $o0 = "xF89C95A5" wide ascii nocase
    $o1 = "xC4A3" wide ascii nocase
    $o2 = "dword_428463" wide ascii nocase
    $o3 = "dword_428EB7" wide ascii nocase
  condition:
    4 of ($o*)
}