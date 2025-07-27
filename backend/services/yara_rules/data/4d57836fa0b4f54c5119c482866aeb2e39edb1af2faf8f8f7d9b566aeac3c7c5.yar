rule auto_rule_20250727024736_4551 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "dword_463EC4" wide ascii nocase
    $o2 = "TrailUp3" wide ascii nocase
  condition:
    3 of ($o*)
}