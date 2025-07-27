rule auto_rule_20250726075902_5169 {
  strings:
    $o0 = "x227Bu" wide ascii nocase
    $o1 = "dword_42863F" wide ascii nocase
    $o2 = "dword_4285EB" wide ascii nocase
  condition:
    3 of ($o*)
}