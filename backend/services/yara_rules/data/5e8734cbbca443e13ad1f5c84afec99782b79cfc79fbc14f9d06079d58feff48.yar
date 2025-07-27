rule auto_rule_20250726204252_5868 {
  strings:
    $o0 = "dword_78190" wide ascii nocase
    $o1 = "dword_7810C" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}