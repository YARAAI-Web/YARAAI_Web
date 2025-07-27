rule auto_rule_20250726160749_0813 {
  strings:
    $o0 = "dword_464BB8" wide ascii nocase
    $o1 = "_aulldiv" wide ascii nocase
    $o2 = "CPtoLCID" wide ascii nocase
  condition:
    3 of ($o*)
}