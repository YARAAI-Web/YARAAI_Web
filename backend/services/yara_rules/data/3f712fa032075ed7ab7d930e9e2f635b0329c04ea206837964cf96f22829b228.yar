rule auto_rule_20250726112341_7761 {
  strings:
    $o0 = "nMinPos" wide ascii nocase
    $o1 = "idInst" wide ascii nocase
    $o2 = "lpchText" wide ascii nocase
    $o3 = "hTemplateFile" wide ascii nocase
  condition:
    4 of ($o*)
}