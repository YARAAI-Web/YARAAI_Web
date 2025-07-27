rule auto_rule_20250726104955_5922 {
  strings:
    $o0 = "dword_42B018" wide ascii nocase
    $o1 = "x2781u" wide ascii nocase
    $o2 = "dword_429018" wide ascii nocase
    $o3 = "xF89C8585" wide ascii nocase
  condition:
    4 of ($o*)
}