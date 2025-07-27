rule auto_rule_20250726081650_8903 {
  strings:
    $o0 = "dword_459710" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "dword_4593FC" wide ascii nocase
    $o3 = "dodwords" wide ascii nocase
  condition:
    4 of ($o*)
}