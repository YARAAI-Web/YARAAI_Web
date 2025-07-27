rule auto_rule_20250726092707_5761 {
  strings:
    $o0 = "szUserMessage" wide ascii nocase
    $o1 = "xtoa" wide ascii nocase
    $o2 = "dword_4656C0" wide ascii nocase
  condition:
    3 of ($o*)
}