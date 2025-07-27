rule auto_rule_20250726184636_5131 {
  strings:
    $o0 = "x3BC4" wide ascii nocase
    $o1 = "dword_43645A" wide ascii nocase
    $o2 = "dword_436456" wide ascii nocase
  condition:
    3 of ($o*)
}