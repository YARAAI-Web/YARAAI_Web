rule auto_rule_20250726193124_9781 {
  strings:
    $o0 = "pwszBuff" wide ascii nocase
    $o1 = "lpDevMode" wide ascii nocase
    $o2 = "AppendMenuA" wide ascii nocase
  condition:
    3 of ($o*)
}