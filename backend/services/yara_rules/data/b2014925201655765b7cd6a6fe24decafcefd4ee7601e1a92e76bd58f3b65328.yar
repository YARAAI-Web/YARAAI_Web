rule auto_rule_20250726193721_5924 {
  strings:
    $o0 = "x32729Bu" wide ascii nocase
    $o1 = "ChooseFontW" wide ascii nocase
    $o2 = "pbmih" wide ascii nocase
    $o3 = "dword_433727" wide ascii nocase
  condition:
    4 of ($o*)
}