rule auto_rule_20250726205617_4193 {
  strings:
    $o0 = "dword_78A64" wide ascii nocase
    $o1 = "dword_78A50" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}