rule auto_rule_20250726070043_8785 {
  strings:
    $o0 = "a1system32Cscri" wide ascii nocase
    $o1 = "asc_405130" wide ascii nocase
    $o2 = "dword_41D990" wide ascii nocase
    $o3 = "dword_41D978" wide ascii nocase
  condition:
    4 of ($o*)
}