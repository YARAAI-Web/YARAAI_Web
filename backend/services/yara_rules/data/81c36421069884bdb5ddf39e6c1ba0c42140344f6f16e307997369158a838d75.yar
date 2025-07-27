rule auto_rule_20250727014620_7934 {
  strings:
    $o0 = "__heap_select" wide ascii nocase
    $o1 = "strcspn" wide ascii nocase
    $o2 = "dword_479960" wide ascii nocase
  condition:
    3 of ($o*)
}