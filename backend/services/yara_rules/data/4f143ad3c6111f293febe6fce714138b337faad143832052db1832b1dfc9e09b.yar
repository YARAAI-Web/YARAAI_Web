rule auto_rule_20250726201551_2071 {
  strings:
    $o0 = "dword_40C1F4" wide ascii nocase
    $o1 = "x140u" wide ascii nocase
    $o2 = "dword_408004" wide ascii nocase
    $o3 = "_positive" wide ascii nocase
  condition:
    4 of ($o*)
}