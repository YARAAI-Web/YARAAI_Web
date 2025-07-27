rule auto_rule_20250726102105_1816 {
  strings:
    $o0 = "lpDueTime" wide ascii nocase
    $o1 = "DialogBoxIndirectParamA" wide ascii nocase
  condition:
    all of them
}