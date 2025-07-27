rule auto_rule_20250726223023_8132 {
  strings:
    $o0 = "StringTypeA" wide ascii nocase
    $o1 = "dword_45D314" wide ascii nocase
    $o2 = "UnwindUp1_0" wide ascii nocase
  condition:
    3 of ($o*)
}